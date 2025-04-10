import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd
from db_connection import connect_to_db, close_connection

def fetch_employment_data():
    conn = connect_to_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT zipcode, avg_employment, avg_annual_payroll, avg_employment_roc
                FROM employment_averages;
            """)
            data = cursor.fetchall()
            return data
        except Exception as e:
            print(f"Error fetching employment data: {e}")
            return None
        finally:
            close_connection(cursor, conn)
    else:
        print("Unable to connect to the database.")
        return None

def forecast_employment(zipcodes, avg_employment, avg_employment_roc, years_ahead=1):
    future_employment = []
    model = LinearRegression()

    #Only using linear regression
    for i in range(len(zipcodes)):
        x = np.array([[avg_employment_roc[i]]])
        y = np.array([avg_employment[i]])
        
        model.fit(x, y)
        future_employment_value = model.predict(np.array([[avg_employment_roc[i]]]))[0] + years_ahead * avg_employment_roc[i]
        future_employment.append(future_employment_value)
    
    return future_employment

def regional_employment_trends():
    data = fetch_employment_data()

    if data is None or len(data) == 0:
        print("No employment data found to analyze.")
        return

    zipcodes = [item[0] for item in data]
    avg_employment = np.array([item[1] for item in data])
    avg_annual_payroll = np.array([item[2] for item in data])
    avg_employment_roc = np.array([item[3] for item in data])
    highest_employment_idx = np.argmax(avg_employment)
    lowest_employment_idx = np.argmin(avg_employment)

    print(f"ZIP Code with highest employment: {zipcodes[highest_employment_idx]} - Employment: {avg_employment[highest_employment_idx]}")
    print(f"ZIP Code with lowest employment: {zipcodes[lowest_employment_idx]} - Employment: {avg_employment[lowest_employment_idx]}")

    # Identify regions with the highest and lowest growth rates in employment
    highest_growth_idx = np.argmax(avg_employment_roc)
    lowest_growth_idx = np.argmin(avg_employment_roc)

    print(f"ZIP Code with highest employment growth: {zipcodes[highest_growth_idx]} - Growth Rate: {avg_employment_roc[highest_growth_idx]}")
    print(f"ZIP Code with lowest employment growth: {zipcodes[lowest_growth_idx]} - Growth Rate: {avg_employment_roc[lowest_growth_idx]}")

    #Compare wage disparities
    high_wage_region_idx = np.argmax(avg_annual_payroll)
    low_wage_region_idx = np.argmin(avg_annual_payroll)

    print(f"ZIP Code with highest annual pay: {zipcodes[high_wage_region_idx]} - Annual Payroll: {avg_annual_payroll[high_wage_region_idx]}")
    print(f"ZIP Code with lowest annual pay: {zipcodes[low_wage_region_idx]} - Annual Payroll: {avg_annual_payroll[low_wage_region_idx]}")

    # List zip codes with significant employment growth
    significant_growth_threshold = 0.05  # 5% growth rate as significant
    significant_growth_zipcodes = [zipcodes[i] for i, growth in enumerate(avg_employment_roc) if growth > significant_growth_threshold]

    print("\nZIP codes with significant employment growth:")
    for zip_code in significant_growth_zipcodes:
        print(zip_code)
        
    print("\nForecasting future employment for the next year...")
    future_employment = forecast_employment(zipcodes, avg_employment, avg_employment_roc, years_ahead=1)
    
    print("\nPredicted Employment for the Next Year:")
    for i, zip_code in enumerate(zipcodes):
        print(f"ZIP Code {zip_code}: Predicted Employment = {future_employment[i]:.2f}")

if __name__ == "__main__":
    regional_employment_trends()