import os
import sys
import json
import time
import hashlib
from decimal import Decimal
from dotenv import load_dotenv
import google.generativeai as genai

try:
    from db_connection import connect_to_db
except ImportError:
    print("ERROR: Ensure 'db_connection.py' exists and contains a 'connect_to_db()' function.", file=sys.stderr)
    sys.exit(1)

load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
MODEL_NAME = "gemini-2.0-flash"
API_CALL_DELAY = 1.5

def format_decimal_or_float(value, precision=4):
    if isinstance(value, Decimal):
        return format(value, f'.{precision}f')
    elif isinstance(value, (int, float)):
        return f"{value:.{precision}f}"
    elif value is None:
        return None
    else:
        try:
             num_val = float(value)
             return f"{num_val:.{precision}f}"
        except (ValueError, TypeError):
             return str(value)


def fetch_overall_zipcode_and_cluster_growth_data(conn):
    print("\n--- Fetching Zipcode Data & Cluster Growth for Overall Insights ---")
    if not conn:
        print("Error: No database connection available.", file=sys.stderr)
        return None

    overall_data = []
    try:
        with conn.cursor() as cur:
            cluster_growth = {}
            cur.execute("SELECT cluster_id,median_price, employment_growth FROM cluster_insights;")
            for row in cur.fetchall():
                cluster_id = row[0]
                cluster_median_price = row[1]
                growth_val = row[2]
                formatted_growth = format_decimal_or_float(growth_val, 1)
                if formatted_growth is not None:
                    cluster_growth[cluster_id] = f"{formatted_growth}%"
                else:
                    cluster_growth[cluster_id] = "N/A"

            cur.execute("""
                SELECT
                    zipcode::text,
                    median_price::text,
                    assigned_cluster
                FROM final_insights_table
                WHERE
                    zipcode IS NOT NULL
                    AND median_price IS NOT NULL
                    AND assigned_cluster IS NOT NULL
                ORDER BY zipcode;
            """)
            rows = cur.fetchall()
            if not rows:
                print("Warning: No zip code data found in final_insights_table for overall insights.")
                return []

            for row in rows:
                zipcode, median_price, cluster_id = row
                growth = cluster_growth.get(cluster_id, "N/A")

                overall_data.append({
                    "zipcode": zipcode,
                    "median_price": median_price,
                    "assigned_cluster_id": str(cluster_id),
                    "cluster_employment_growth": growth,
                    "cluster_median_price": format_decimal_or_float(cluster_median_price),
                })

        print(f"Fetched combined data for {len(overall_data)} zipcodes for overall summary.")
        return overall_data

    except Exception as e:
        print(f"Error fetching combined zipcode/cluster growth data: {e}", file=sys.stderr)
        conn.rollback()
        return None

def generate_overall_insights_from_ai(zipcode_level_data):
    print("--- Generating Overall Market Insights (Zipcode-Based Summary) via AI ---")
    if not GOOGLE_API_KEY:
        print("ERROR: GOOGLE_API_KEY not set.", file=sys.stderr)
        return None
    if not zipcode_level_data:
        print("Skipping overall AI generation: No combined zipcode data provided.")
        return None

    prompt_data = []
    for item in zipcode_level_data:
        clean_item = {k: v for k, v in item.items() if v is not None}
        if clean_item.get("zipcode"):
            prompt_data.append(clean_item)

    if not prompt_data:
        print("Skipping overall AI generation: No valid zipcode data after filtering.")
        return None

    prompt = f"""
Analyze the following dataset containing individual zip codes within the market, their median house prices, the market cluster they belong to, and the employment growth rate associated with that cluster:
{json.dumps(prompt_data, indent=2)}

Based ONLY on this provided list of zip codes and their associated data, generate 4 concise key insights summarizing the *overall market state*. Focus on trends across *all zip codes*. Consider aspects like:
- The general range and distribution of median house prices across the listed zip codes.
- The relationship between median house prices and the assigned cluster's employment growth (e.g., are higher-priced zip codes generally in higher-growth clusters, or are there exceptions?).
- Identification of any zip codes or groups of zip codes that stand out due to their price/cluster growth combination (e.g., high price & high growth, high price & low growth, etc.).
- General observations about market segmentation based on price points and associated cluster growth potential.

Do NOT use any external data or metrics not present in the provided dataset (like payroll or affordability ratios for this specific summary).

For each insight:
1. Provide a short, relevant title (e.g., "Price Distribution Overview", "Growth vs. Price Relationship", "Notable Zip Code Areas", "Market Segments by Price/Growth").
2. Write a brief explanation (1-2 sentences) directly referencing specific examples or trends observed across the zip codes in the dataset (e.g., "Zip codes such as <b>89XXX</b> command top market prices (around $X,XXX,XXX) and benefit from high cluster employment growth (<b>Y.Y%</b>).", "A significant number of zip codes fall into the $AAA,AAA - $BBB,BBB price range, often associated with clusters showing moderate growth (<b>Z.Z%</b>).", "Interestingly, zip code <b>89YYY</b> shows relatively high prices despite being in a cluster with lower growth (<b>W.W%</b>).").
3. Format the output STRICTLY as a JSON array of objects, where each object has a "title" (string) and "explanation" (string) property. Example: [{{"title": "Example Title", "explanation": "Example explanation referencing data trends across zip codes."}}]
4. Format currency values like $XXX,XXX. Ensure employment growth rates are shown with the % sign as provided (e.g., 3.5%).
5. Add HTML bold tags (`<b>...</b>`) around specific zip code numbers, cluster IDs, growth rates, and price points mentioned in the explanation for emphasis.
6. When referencing clusters use the format "Cluster <b>(median_price_of_cluster)</b> instead of Cluster 1, Cluster 2, etc. (e.g., "Cluster <b>$XXX,XXX</b>").
6. Do not include any introductory text, concluding text, markdown formatting (like ```json), or anything else outside the pure JSON array structure. Ensure the output is valid JSON.
"""

    print("Calling AI for overall insights (zipcode summary)...")
    try:
        genai.configure(api_key=GOOGLE_API_KEY)
        model = genai.GenerativeModel(MODEL_NAME)
        generation_config = genai.types.GenerationConfig(
            temperature=0.7, top_k=1, top_p=1, max_output_tokens=1536
        )
        response = model.generate_content(prompt, generation_config=generation_config)

        if not response.candidates:
            block_reason = response.prompt_feedback.block_reason if response.prompt_feedback else "Unknown"
            safety_ratings = response.prompt_feedback.safety_ratings if response.prompt_feedback else "N/A"
            print(f"ERROR: Overall insight generation blocked. Reason: {block_reason}. Safety: {safety_ratings}", file=sys.stderr)
            return None

        if not (response.candidates and response.candidates[0].content.parts):
             print("Warning: AI response for overall insights empty.", file=sys.stderr)
             return None

        response_text = response.text
        print("Received overall AI response.")
        try:
            cleaned_response_text = response_text.strip().strip('```json').strip('```').strip()
            start_index = cleaned_response_text.find('[')
            end_index = cleaned_response_text.rfind(']')
            if start_index != -1 and end_index != -1 and end_index > start_index:
                json_text = cleaned_response_text[start_index:end_index+1]
            else:
                if cleaned_response_text.startswith('{') and cleaned_response_text.endswith('}'):
                     json_text = f"[{cleaned_response_text}]"
                else:
                     raise json.JSONDecodeError("Could not find valid JSON array structure", cleaned_response_text, 0)

            generated_insights = json.loads(json_text)

            if not isinstance(generated_insights, list) or not all(
                isinstance(item, dict) and
                item.get('title') and isinstance(item.get('title'), str) and
                item.get('explanation') and isinstance(item.get('explanation'), str)
                for item in generated_insights
            ):
                 raise ValueError("Parsed JSON is not a list of valid insight objects.")

            print("Successfully parsed and validated overall AI response.")
            return generated_insights

        except (json.JSONDecodeError, ValueError) as e:
            print(f"ERROR: Failed to parse/validate overall AI response: {e}", file=sys.stderr)
            print("--- Raw AI Response Text ---", file=sys.stderr)
            print(response_text, file=sys.stderr)
            print("--- End Raw AI Response Text ---", file=sys.stderr)
            return None

    except Exception as e:
        print(f"ERROR during overall AI call: {e}", file=sys.stderr)
        return None

def save_overall_insights(conn, insights):
    print("--- Saving Overall Market Insights ---")
    if not conn:
        print("Error: No database connection for saving.", file=sys.stderr)
        return False
    if not insights:
        print("No overall insights generated, skipping save.")
        return True

    with conn.cursor() as cur:
        try:
            insights_json = json.dumps(insights)
            print("Clearing previous overall insights...")
            cur.execute("DELETE FROM generated_market_insights;")
            insert_query = """
                INSERT INTO generated_market_insights (insights_content, generated_at)
                VALUES (%s, CURRENT_TIMESTAMP)
                RETURNING id, generated_at;
            """
            cur.execute(insert_query, (insights_json,))
            result = cur.fetchone()
            conn.commit()
            if result:
                print(f"Successfully saved overall insights (ID: {result[0]}) at {result[1]}")
                return True
            else:
                print("Warning: Insert query for overall insights executed but no ID returned.", file=sys.stderr)
                return False
        except Exception as e:
            print(f"Error saving overall insights: {e}", file=sys.stderr)
            conn.rollback()
            return False


def get_all_zipcodes(conn):
    if not conn: return []
    zipcodes = []
    print("Fetching unique zipcodes (as text)...")
    with conn.cursor() as cur:
        try:
            cur.execute("""
                SELECT DISTINCT zipcode::text
                FROM final_insights_table
                WHERE zipcode IS NOT NULL
                ORDER BY zipcode::text;
            """)
            rows = cur.fetchall()
            zipcodes = [row[0] for row in rows]
            print(f"Found {len(zipcodes)} unique zipcodes.")
            return zipcodes
        except Exception as e:
            print(f"Error fetching zipcodes: {e}", file=sys.stderr)
            return []

def fetch_zipcode_specific_data(conn, zipcode):
    if not conn: return None, None
    zip_data = {"zipcode": zipcode}
    try:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT median_price::text, assigned_cluster, affordability_ratio
                FROM final_insights_table WHERE zipcode = %s;
            """, (zipcode,))
            final_row = cur.fetchone()
            if final_row:
                zip_data["median_price"] = final_row[0]
                zip_data["assigned_cluster"] = str(final_row[1]) if final_row[1] is not None else None
                zip_data["affordability_ratio"] = format_decimal_or_float(final_row[2], 4)

            cur.execute("""
                SELECT col_index, medain_age, enrollment, num_of_schools,
                       schools_rated_1_or_2, num_of_1_or_2_es, num_of_1_or_2_ms, num_of_1_or_2_hs
                FROM non_census_data WHERE zipcode = %s;
            """, (zipcode,))
            non_census_row = cur.fetchone()
            if non_census_row:
                zip_data["cost_of_living_index"] = format_decimal_or_float(non_census_row[0], 1)
                zip_data["median_age"] = format_decimal_or_float(non_census_row[1], 1)
                zip_data["school_enrollment"] = str(non_census_row[2]) if non_census_row[2] is not None else None
                zip_data["total_schools"] = str(non_census_row[3]) if non_census_row[3] is not None else None
                zip_data["low_rated_schools"] = str(non_census_row[4]) if non_census_row[4] is not None else None
                zip_data["low_rated_elementary"] = str(non_census_row[5]) if non_census_row[5] is not None else None
                zip_data["low_rated_middle"] = str(non_census_row[6]) if non_census_row[6] is not None else None
                zip_data["low_rated_high"] = str(non_census_row[7]) if non_census_row[7] is not None else None

            if len(zip_data) <= 1:
                print(f"Warning: No data found for zipcode {zipcode} in relevant tables.")
                return None, None

            hash_data = {k: v for k, v in zip_data.items() if k != 'zipcode'}
            hashed_string = json.dumps(hash_data, sort_keys=True)
            data_hash = hashlib.sha256(hashed_string.encode('utf-8')).hexdigest()
            return zip_data, data_hash

    except Exception as e:
        print(f"Error fetching data for zipcode {zipcode}: {e}", file=sys.stderr)
        if conn: conn.rollback()
        return None, None

def check_if_regeneration_needed(conn, zipcode, current_data_hash):
     if not conn or not current_data_hash: return True
     with conn.cursor() as cur:
          try:
               cur.execute("SELECT source_data_hash FROM generated_zipcode_insights WHERE zipcode = %s", (zipcode,))
               result = cur.fetchone()
               if result and result[0] == current_data_hash:
                    return False
               return True
          except Exception as e:
               print(f"Error checking hash for zipcode {zipcode}: {e}. Assuming regeneration needed.", file=sys.stderr)
               try:
                   conn.rollback()
               except Exception as rb_e:
                   print(f"Error during rollback after hash check failure: {rb_e}", file=sys.stderr)
               return True

def generate_zipcode_insights_from_ai(zipcode_data):
    if not GOOGLE_API_KEY:
        print("ERROR: GOOGLE_API_KEY not set.", file=sys.stderr)
        return None
    if not zipcode_data or not zipcode_data.get("zipcode"):
        print("Skipping AI generation: No valid zipcode data provided.")
        return None

    zipcode = zipcode_data.get("zipcode")
    prompt_data = {k: v for k, v in zipcode_data.items() if v is not None}
    if len(prompt_data) <= 1:
         print(f"Skipping AI generation for {zipcode}: Insufficient data after filtering.")
         return None

    prompt = f"""
Analyze the following specific data for the real estate market in zipcode {zipcode}:
{json.dumps(prompt_data, indent=2)}

Based ONLY on the provided data for zipcode {zipcode}, generate 3-4 concise key insights covering different aspects like housing affordability, local demographics (age), school quality indicators, cost of living, and potential investment considerations for this specific area.

For each insight:
1. Provide a short, relevant title (e.g., "Affordability Challenge", "Younger Demographic", "School Quality Note", "Living Costs", "Investment Angle").
2. Write a brief explanation (1-2 sentences) directly referencing specific data points from the provided {zipcode} data (e.g., median price, affordability ratio, median age, number of low-rated schools, cost of living index).
3. Format the output STRICTLY as a JSON array of objects, where each object has a "title" (string) and "explanation" (string) property. Example: [{{"title": "Example Title", "explanation": "Example explanation referencing data for {zipcode}."}}]
4. Format currency values like $XXX,XXX. Format ratios to 4 decimals (e.g., 0.1234). Format index/age values clearly. Mention school counts directly (e.g., "<b>{prompt_data.get('low_rated_schools', 'N/A')}</b> low-rated schools out of <b>{prompt_data.get('total_schools', 'N/A')}</b> total").
5. Add HTML bold tags (`<b>...</b>`) around the zipcode number ({zipcode}) and key numerical data points mentioned in the explanation for emphasis.
6. Do not include any introductory text, concluding text, markdown formatting (like ```json), or anything else outside the pure JSON array structure. Ensure the output is valid JSON.
"""

    try:
        genai.configure(api_key=GOOGLE_API_KEY)
        model = genai.GenerativeModel(MODEL_NAME)
        generation_config = genai.types.GenerationConfig(
            temperature=0.6, top_k=1, top_p=1, max_output_tokens=800
        )
        response = model.generate_content(prompt, generation_config=generation_config)

        if not response.candidates:
             block_reason = response.prompt_feedback.block_reason if response.prompt_feedback else "Unknown"
             safety_ratings = response.prompt_feedback.safety_ratings if response.prompt_feedback else "N/A"
             print(f"ERROR: AI generation blocked for {zipcode}. Reason: {block_reason}. Safety: {safety_ratings}", file=sys.stderr)
             return None

        if not (response.candidates and response.candidates[0].content.parts):
            print(f"Warning: AI response for {zipcode} was present but empty.", file=sys.stderr)
            return None

        response_text = response.text
        try:
            cleaned_response_text = response_text.strip().strip('```json').strip('```').strip()
            start_index = cleaned_response_text.find('[')
            end_index = cleaned_response_text.rfind(']')
            if start_index != -1 and end_index != -1 and end_index > start_index:
                json_text = cleaned_response_text[start_index:end_index+1]
            else:
                if cleaned_response_text.startswith('{') and cleaned_response_text.endswith('}'):
                     json_text = f"[{cleaned_response_text}]"
                else:
                    raise json.JSONDecodeError("Could not find valid JSON array structure", cleaned_response_text, 0)

            generated_insights = json.loads(json_text)

            if not isinstance(generated_insights, list) or not all(
                isinstance(item, dict) and
                item.get('title') and isinstance(item.get('title'), str) and
                item.get('explanation') and isinstance(item.get('explanation'), str)
                for item in generated_insights
            ):
                raise ValueError("Parsed JSON is not a list of valid insight objects.")

            return generated_insights

        except (json.JSONDecodeError, ValueError) as e:
            print(f"ERROR: Failed to parse/validate AI response for {zipcode}: {e}", file=sys.stderr)
            print("--- Raw AI Response Text ---", file=sys.stderr)
            print(response_text, file=sys.stderr)
            print("--- End Raw AI Response Text ---", file=sys.stderr)
            return None

    except Exception as e:
        print(f"ERROR during AI call for {zipcode}: {e}", file=sys.stderr)
        return None


def save_zipcode_insights(conn, zipcode, insights, source_hash):
    if not conn: return False
    if not insights: return False

    with conn.cursor() as cur:
        try:
            insights_json = json.dumps(insights)
            upsert_query = """
                INSERT INTO generated_zipcode_insights
                    (zipcode, insights_content, source_data_hash, generated_at)
                VALUES (%s, %s, %s, CURRENT_TIMESTAMP)
                ON CONFLICT (zipcode)
                DO UPDATE SET
                    insights_content = EXCLUDED.insights_content,
                    source_data_hash = EXCLUDED.source_data_hash,
                    generated_at = CURRENT_TIMESTAMP;
            """
            cur.execute(upsert_query, (str(zipcode), insights_json, source_hash))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error saving insights for zipcode {zipcode}: {e}", file=sys.stderr)
            try:
                conn.rollback()
            except Exception as rb_e:
                 print(f"Error during rollback after save failure for {zipcode}: {rb_e}", file=sys.stderr)
            return False


def main():
    start_time_total = time.time()
    print("Starting full market insight generation process...")
    print(f"Using AI Model: {MODEL_NAME}")
    print(f"Current Time: {time.strftime('%Y-%m-%d %H:%M:%S %Z')}")

    conn = None
    exit_code = 0
    overall_success = False
    zip_success_count = 0
    zip_skipped_count = 0
    zip_error_count = 0
    zip_total_count = 0

    try:
        conn = connect_to_db()
        if not conn:
            raise ConnectionError("Failed to establish database connection.")

        overall_zip_data = fetch_overall_zipcode_and_cluster_growth_data(conn)
        if overall_zip_data is not None:
            overall_insights = generate_overall_insights_from_ai(overall_zip_data)
            if overall_insights:
                if save_overall_insights(conn, overall_insights):
                    overall_success = True
                else:
                    print("ERROR: Failed to save overall insights.", file=sys.stderr)
            else:
                 print("ERROR: Failed to generate overall insights.", file=sys.stderr)
        else:
             print("ERROR: Failed to fetch data for overall insights. Skipping overall generation.", file=sys.stderr)

        print("\n--- Starting Zipcode-Specific Insight Generation ---")
        zipcodes_to_process = get_all_zipcodes(conn)
        zip_total_count = len(zipcodes_to_process)

        if not zipcodes_to_process:
            print("No zipcodes found to process for specific insights.")
        else:
            print(f"Processing {zip_total_count} zipcodes...")
            for i, zipcode in enumerate(zipcodes_to_process):
                progress = f"({i+1}/{zip_total_count})"
                zipcode_data, data_hash = fetch_zipcode_specific_data(conn, zipcode)

                if zipcode_data and data_hash:
                    if not check_if_regeneration_needed(conn, zipcode, data_hash):
                        zip_skipped_count += 1
                        print(f"Skipped {zipcode} {progress} (data unchanged)")
                        continue

                    print(f"Generating for {zipcode} {progress}...")
                    generated_insights = generate_zipcode_insights_from_ai(zipcode_data)

                    if generated_insights:
                        if save_zipcode_insights(conn, zipcode, generated_insights, data_hash):
                            zip_success_count += 1
                        else:
                            zip_error_count += 1
                            print(f"-> FAILED SAVE {zipcode} {progress}")
                    else:
                        zip_error_count += 1
                        print(f"-> FAILED GENERATE {zipcode} {progress}")
                elif zipcode_data is None and data_hash is None:
                     zip_error_count += 1
                     print(f"-> FAILED FETCH {zipcode} {progress}")
                else:
                     zip_error_count += 1
                     print(f"-> UNEXPECTED FETCH RESULT {zipcode} {progress}")

                if API_CALL_DELAY > 0:
                    time.sleep(API_CALL_DELAY)

        print("\n--- Full Process Summary ---")
        if overall_success:
             print("Overall Market Insights: Generated and Saved Successfully.")
        else:
             print("Overall Market Insights: FAILED or Skipped.")

        print("\nZipcode Specific Insights:")
        print(f"  Successfully Generated/Updated: {zip_success_count}")
        print(f"  Skipped (Data Unchanged):     {zip_skipped_count}")
        print(f"  Errors (Fetch/Generate/Save): {zip_error_count}")
        print(f"  Total Zipcodes Found:         {zip_total_count}")

        if zip_error_count > 0 or not overall_success :
             exit_code = 1
             print("\n*** Process completed with errors. Check logs above. ***")
        elif zip_skipped_count == zip_total_count and overall_success:
             print("\nProcess completed. No zipcode insights needed regeneration.")
        else:
             print("\nProcess completed successfully.")

    except (ConnectionError, Exception) as e:
        print(f"\n--- FATAL ERROR during insight generation process ---", file=sys.stderr)
        print(f"{type(e).__name__}: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc(file=sys.stderr)
        exit_code = 1
    finally:
        if conn:
            try:
                conn.close()
                print("Database connection closed.")
            except Exception as close_e:
                print(f"Error closing database connection: {close_e}", file=sys.stderr)
        end_time_total = time.time()
        print(f"Total script execution time: {end_time_total - start_time_total:.2f} seconds.")

if __name__ == "__main__":
    if not GOOGLE_API_KEY:
        print("CRITICAL ERROR: GOOGLE_API_KEY environment variable is not set.", file=sys.stderr)
        sys.exit(1)
    print("Attempting initial database connection...")
    temp_conn = connect_to_db()
    if not temp_conn:
        print("CRITICAL ERROR: Failed initial database connection. Check credentials/db status.", file=sys.stderr)
        sys.exit(1)
    else:
        temp_conn.close()
        print("Initial database connection successful.")

    main()