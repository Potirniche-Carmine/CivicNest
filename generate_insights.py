import os
import json
import sys
from dotenv import load_dotenv
import google.generativeai as genai
from decimal import Decimal

from db_connection import connect_to_db

MODEL_NAME = "gemini-2.0-flash"

load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')


def fetch_numerical_data(conn):
    print("Fetching fresh numerical data from database...")
    if not conn:
        print("Error: No database connection available.", file=sys.stderr)
        return None

    numerical_data = []
    with conn.cursor() as cur:
        try:
            numerical_data_query = """
                SELECT cluster_id, avg_payroll::text, avg_price::text, employment_growth, affordability_ratio
                FROM insights_table
                ORDER BY cluster_id;
            """
            cur.execute(numerical_data_query)
            rows = cur.fetchall()

            if not rows:
                print("Warning: No data found in insights_table.")
                return []

            for row in rows:
                affordability_ratio = row[4]
                if isinstance(affordability_ratio, Decimal):
                    ratio_str = str(affordability_ratio.quantize(Decimal("0.0001")))
                elif isinstance(affordability_ratio, (int, float)):
                    ratio_str = f"{affordability_ratio:.4f}"
                else:
                    ratio_str = str(affordability_ratio) # Basic string conversion as fallback

                numerical_data.append({
                    "cluster": row[0],
                    "payroll": row[1],  # Already text from query cast
                    "price": row[2],    # Already text from query cast
                    "ratio": ratio_str, # Processed ratio
                    "growth": str(row[3]) # Ensure growth is also a string
                })

            print(f"Processed {len(numerical_data)} rows of numerical data.")
            return numerical_data

        except Exception as e:
            print(f"Error fetching data from database: {e}", file=sys.stderr)
            conn.rollback() # Rollback any potential transaction changes on error
            return None # Indicate failure

def generate_insights_from_ai(data):
    if not GOOGLE_API_KEY:
        print("ERROR: GOOGLE_API_KEY environment variable is not set.", file=sys.stderr)
        return None

    if not data:
        print("Skipping AI generation as no data was provided.")
        return None

    print("Constructing prompt for AI...")
    prompt = f"""
Analyze the following real estate market cluster data:
{json.dumps(data, indent=2)}

Based ONLY on the provided data, generate 4 concise key market insights covering different aspects like investment potential, employment growth trends, affordability issues, or market balance.
For each insight:
1. Provide a short, relevant title (e.g., "Investment Hotspot", "Growth Leaders", "Affordability Concern", "Balanced Market").
2. Write a brief explanation (1-2 sentences) directly referencing the data points (cluster numbers, ratios, employment growth rates) that support the insight.
3. Format the output STRICTLY as a JSON array of objects, where each object has a "title" (string) and "explanation" (string) property. Example: [{{"title": "Example Title", "explanation": "Example explanation referencing data."}}]
Do not include any introductory text, concluding text, markdown formatting (like ```json), or anything else outside the pure JSON array structure.
Ensure the output is valid JSON.
Make sure all of the prices are correctly formatted such as $123,456.78 and all the ratios are formatted as 0.1234 and also the growth rate is an employment growth rate not a housing price growth rate and make sure you format it correctly with a % sign.
Add html tags to bold the clusters number and important numbers in the explanation.
"""

    print("Calling Google Generative AI API...")
    try:
        genai.configure(api_key=GOOGLE_API_KEY)
        model = genai.GenerativeModel(MODEL_NAME)

        generation_config = genai.types.GenerationConfig(
             temperature=0.7,
             top_k=1,
             top_p=1,
             max_output_tokens=1024
        )

        response = model.generate_content(
            prompt,
            generation_config=generation_config,
        )

        if not response.candidates:
             block_reason = response.prompt_feedback.block_reason if response.prompt_feedback else "Unknown"
             error_message = f"AI content generation blocked. Reason: {block_reason}."
             if hasattr(response, 'parts') and response.parts:
                  error_message += f" Parts: {response.parts}"
             print(f"ERROR: {error_message}", file=sys.stderr)
             print(f"Prompt Feedback: {response.prompt_feedback}", file=sys.stderr)
             return None


        if len(response.candidates) > 0 and len(response.candidates[0].content.parts) > 0:
             response_text = response.text
        else:
             print("Warning: AI response was present but contained no processable text content.", file=sys.stderr)
             print(f"Full AI Response object: {response}", file=sys.stderr)
             return None
        print("Received AI response.")
        try:
            cleaned_response_text = response_text.strip().strip('```json').strip('```').strip()
            generated_insights = json.loads(cleaned_response_text)

            if not isinstance(generated_insights, list):
                raise ValueError("Parsed JSON is not a list.")

            if not all(
                isinstance(item, dict) and
                'title' in item and isinstance(item['title'], str) and item['title'] and
                'explanation' in item and isinstance(item['explanation'], str) and item['explanation']
                for item in generated_insights
            ):
                 raise ValueError("Parsed JSON list does not contain objects with non-empty 'title' and 'explanation' strings.")

            print("Successfully parsed and validated AI response.")
            return generated_insights

        except json.JSONDecodeError as e:
            print(f"ERROR: Failed to parse AI response as JSON: {e}", file=sys.stderr)
            print("--- Raw AI Response Text ---", file=sys.stderr)
            print(response_text, file=sys.stderr)
            print("--- End Raw AI Response Text ---", file=sys.stderr)
            return None
        except ValueError as e:
             print(f"ERROR: Failed validation of parsed AI response structure: {e}", file=sys.stderr)
             print("--- Parsed JSON Object ---", file=sys.stderr)
             try:
                 print(json.dumps(json.loads(cleaned_response_text), indent=2), file=sys.stderr)
             except Exception:
                 print("(Could not display parsed object)", file=sys.stderr)
             print("--- End Parsed JSON Object ---", file=sys.stderr)
             return None

    except StopIteration: #
         print("ERROR: AI generation stopped unexpectedly. Check prompt feedback.", file=sys.stderr)
         try:
              print(f"Prompt Feedback: {response.prompt_feedback}", file=sys.stderr)
         except Exception:
              print("(Could not retrieve prompt feedback)", file=sys.stderr)
         return None
    except Exception as e:
        print(f"ERROR during Google Generative AI API call: {e}", file=sys.stderr)
        if hasattr(e, 'response') and e.response:
            print(f"API Response Status Code: {e.response.status_code}", file=sys.stderr)
            print(f"API Response Text: {e.response.text}", file=sys.stderr)
        return None

def save_generated_insights(conn, insights):
    print("Saving generated insights to PostgreSQL database...")
    if not conn:
        print("Error: No database connection available for saving.", file=sys.stderr)
        return False
    if not insights:
        print("No insights were generated, skipping database save.")
        return False

    with conn.cursor() as cur:
        try:
            insights_json = json.dumps(insights)
            insert_query = """
                INSERT INTO generated_market_insights (insights_content)
                VALUES (%s)
                RETURNING id, generated_at;
            """
            cur.execute(insert_query, (insights_json,))
            result = cur.fetchone()

            conn.commit() #

            if result:
                print(f"Successfully saved insights with ID: {result[0]} at {result[1]}")
                return True
            else:
                print("Warning: Insert query executed but did not return expected ID/timestamp.", file=sys.stderr)
                return False #

        except Exception as e:
            print(f"Error saving insights to database: {e}", file=sys.stderr)
            conn.rollback()
            return False

def main():
    print("Starting market insight generation process...")
    conn = None #
    exit_code = 0

    try:
        conn = connect_to_db()
        if not conn:
            raise ConnectionError("Failed to establish database connection.")

        numerical_data = fetch_numerical_data(conn)
        if numerical_data is None:
            raise RuntimeError("Failed to fetch numerical data from the database.")
        elif not numerical_data:
             print("No numerical data found. Process might stop here depending on requirements.")

        generated_insights = generate_insights_from_ai(numerical_data)
        if generated_insights is None:
            raise RuntimeError("Failed to generate insights using AI.")

        if not save_generated_insights(conn, generated_insights):
             raise RuntimeError("Failed to save generated insights to the database.")

        print("Market insight generation process completed successfully.")

    except (ConnectionError, RuntimeError, Exception) as e:
        print(f"\n--- ERROR during insight generation process ---", file=sys.stderr)
        print(f"{type(e).__name__}: {e}", file=sys.stderr)
        exit_code = 1
    finally:
        if conn:
            conn.close()
        print("Script finished.")
        sys.exit(exit_code)

if __name__ == "__main__":
    main()