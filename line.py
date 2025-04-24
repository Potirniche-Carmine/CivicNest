
import matplotlib.pyplot as plt
import pandas as pd
from db_connection import connect_to_db, close_connection

def fetch_employment_with_roc():
    conn = connect_to_db()
    if conn:
        try:
            query = """
                SELECT zipcode, year, employment, employment_roc
                FROM employment
                ORDER BY zipcode, year;
            """
            df = pd.read_sql(query, conn)
            return df
        except Exception as e:
            print(f"Error fetching data: {e}")
            return None
        finally:
            conn.close()
    else:
        print("Unable to connect to the database.")
        return None

def plot_employment_trends_with_projection():
    df = fetch_employment_with_roc()

    if df is None or df.empty:
        print("No data available for plotting.")
        return

    plt.figure(figsize=(12, 8))

    for zipcode, group in df.groupby("zipcode"):
        group = group.sort_values("year")
        
        # Historical values
        years = group["year"].tolist()
        employment = group["employment"].tolist()

        #extrapolate based on the most recent year's ROC
        last_year = years[-1]
        last_employment = employment[-1]
        last_roc = group["employment_roc"].iloc[-1]

        projected_employment = last_employment * (1 + last_roc)
        projected_year = last_year + 1 # The model only seems to be relatively accurate give or take a year

        forecast_years = years + [projected_year]
        forecast_employment = employment + [projected_employment]

        plt.plot(forecast_years, forecast_employment, label=f"ZIP {zipcode}", alpha=0.5)
        plt.scatter([projected_year], [projected_employment], color='red', edgecolors='black')

    plt.title("Employment Trends with 1-Year Forecast by ZIP Code")
    plt.xlabel("Year")
    plt.ylabel("Employment")
    plt.grid(True)
    plt.legend(loc="upper left", fontsize="small", ncol=2)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_employment_trends_with_projection()



