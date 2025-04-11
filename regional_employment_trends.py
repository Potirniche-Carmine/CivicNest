# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from db_connection import connect_to_db, close_connection

# def fetch_employment_data():
#     conn = connect_to_db()
#     if conn:
#         try:
#             cursor = conn.cursor()
#             cursor.execute("""
#                 SELECT zipcode, avg_employment, avg_annual_payroll, avg_employment_roc
#                 FROM employment_averages;
#             """)
#             data = cursor.fetchall()
#             return data
#         except Exception as e:
#             print(f"Error fetching employment data: {e}")
#             return None
#         finally:
#             close_connection(cursor, conn)
#     else:
#         print("Unable to connect to the database.")
#         return None

# def forecast_employment(zipcodes, avg_employment, avg_employment_roc, years_ahead=1):
#     future_employment = []

#     for i in range(len(zipcodes)):
#         employment_now = avg_employment[i]
#         roc = avg_employment_roc[i]
#         future_value = employment_now * ((1 + roc) ** years_ahead)
#         future_employment.append(np.floor(future_value))  # Round down

#     return future_employment

# def save_forecasts_to_db(zipcodes, current_employment, future_employment):
#     conn = connect_to_db()
#     if not conn:
#         print("Database connection failed.")
#         return

#     try:
#         cursor = conn.cursor()
#         cursor.execute("""
#             CREATE TABLE IF NOT EXISTS employment_prediction (
#                 zipcode TEXT PRIMARY KEY,
#                 current NUMERIC,
#                 future NUMERIC
#             );
#         """)

#         cursor.execute("DELETE FROM employment_prediction;")

#         for i in range(len(zipcodes)):
#             cursor.execute("""
#                 INSERT INTO employment_prediction (zipcode, current, future)
#                 VALUES (%s, %s, %s);
#             """, (zipcodes[i], int(current_employment[i]), int(future_employment[i]))) # Can't hire half a dude

#         conn.commit()


#     except Exception as e:
#         print(f"Error saving forecast data: {e}")
#         conn.rollback()
#     finally:
#         close_connection(cursor, conn)

# def regional_employment_trends():
#     data = fetch_employment_data()

#     if data is None or len(data) == 0:
#         print("No employment data found to analyze.")
#         return

#     zipcodes = [item[0] for item in data]
#     avg_employment = np.array([item[1] for item in data])
#     avg_annual_payroll = np.array([item[2] for item in data])
#     avg_employment_roc = np.array([item[3] for item in data])

#     highest_employment_idx = np.argmax(avg_employment)
#     lowest_employment_idx = np.argmin(avg_employment)

#     print(f"ZIP Code with highest employment: {zipcodes[highest_employment_idx]} - Employment: {avg_employment[highest_employment_idx]}")
#     print(f"ZIP Code with lowest employment: {zipcodes[lowest_employment_idx]} - Employment: {avg_employment[lowest_employment_idx]}")

#     highest_growth_idx = np.argmax(avg_employment_roc)
#     lowest_growth_idx = np.argmin(avg_employment_roc)

#     print(f"ZIP Code with highest employment growth: {zipcodes[highest_growth_idx]} - Growth Rate: {avg_employment_roc[highest_growth_idx]}")
#     print(f"ZIP Code with lowest employment growth: {zipcodes[lowest_growth_idx]} - Growth Rate: {avg_employment_roc[lowest_growth_idx]}")

#     high_wage_region_idx = np.argmax(avg_annual_payroll)
#     low_wage_region_idx = np.argmin(avg_annual_payroll)

#     print(f"ZIP Code with highest annual pay: {zipcodes[high_wage_region_idx]} - Annual Payroll: {avg_annual_payroll[high_wage_region_idx]}")
#     print(f"ZIP Code with lowest annual pay: {zipcodes[low_wage_region_idx]} - Annual Payroll: {avg_annual_payroll[low_wage_region_idx]}")

#     significant_growth_threshold = 0.05
#     significant_growth_zipcodes = [zipcodes[i] for i, growth in enumerate(avg_employment_roc) if growth > significant_growth_threshold]

#     print("\nZIP codes with significant employment growth:")
#     for zip_code in significant_growth_zipcodes:
#         print(zip_code)

#     print("\nForecasting future employment for the next year...")
#     future_employment = forecast_employment(zipcodes, avg_employment, avg_employment_roc, years_ahead=1)

#     print("\nPredicted Employment for the Next Year:")
#     for i, zip_code in enumerate(zipcodes):
#         print(f"ZIP Code {zip_code}: Current = {avg_employment[i]:.2f}, Predicted = {future_employment[i]:.0f}")

#     #Save to database
#     save_forecasts_to_db(zipcodes, avg_employment, future_employment)

# if __name__ == "__main__":
#     regional_employment_trends()


import numpy as np
import pandas as pd
from db_connection import connect_to_db, close_connection

def fetch_employment_averages_data():
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
            print(f"Error fetching employment averages data: {e}")
            return None
        finally:
            close_connection(cursor, conn)
    else:
        print("Unable to connect to the database.")
        return None

def fetch_employment_data_for_forecasting():
    conn = connect_to_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT zipcode, year, employment, employment_roc
                FROM employment
                ORDER BY zipcode, year;
            """)
            data = cursor.fetchall()
            return data
        except Exception as e:
            print(f"Error fetching employment data for forecasting: {e}")
            return None
        finally:
            close_connection(cursor, conn)
    else:
        print("Unable to connect to the database.")
        return None

def analyze_employment_statistics(zipcodes, avg_employment, avg_annual_payroll, avg_employment_roc):
    highest_employment_idx = np.argmax(avg_employment)
    lowest_employment_idx = np.argmin(avg_employment)

    print(f"ZIP Code with highest employment: {zipcodes[highest_employment_idx]} - Employment: {avg_employment[highest_employment_idx]}")
    print(f"ZIP Code with lowest employment: {zipcodes[lowest_employment_idx]} - Employment: {avg_employment[lowest_employment_idx]}")

    highest_growth_idx = np.argmax(avg_employment_roc)
    lowest_growth_idx = np.argmin(avg_employment_roc)

    print(f"ZIP Code with highest employment growth: {zipcodes[highest_growth_idx]} - Growth Rate: {avg_employment_roc[highest_growth_idx]}")
    print(f"ZIP Code with lowest employment growth: {zipcodes[lowest_growth_idx]} - Growth Rate: {avg_employment_roc[lowest_growth_idx]}")

    high_wage_region_idx = np.argmax(avg_annual_payroll)
    low_wage_region_idx = np.argmin(avg_annual_payroll)

    print(f"ZIP Code with highest annual pay: {zipcodes[high_wage_region_idx]} - Annual Payroll: {avg_annual_payroll[high_wage_region_idx]}")
    print(f"ZIP Code with lowest annual pay: {zipcodes[low_wage_region_idx]} - Annual Payroll: {avg_annual_payroll[low_wage_region_idx]}")

    significant_growth_threshold = 0.05
    significant_growth_zipcodes = [zipcodes[i] for i, growth in enumerate(avg_employment_roc) if growth > significant_growth_threshold]

    print("\nZIP codes with significant employment growth:")
    for zip_code in significant_growth_zipcodes:
        print(zip_code)

def forecast_employment(zipcodes, current_employment, employment_roc, years_ahead=1):
    future_employment = []

    for i in range(len(zipcodes)):
        employment_now = current_employment[i]
        roc = employment_roc[i]
        future_value = employment_now * ((1 + roc) ** years_ahead)  # Applying the growth rate
        future_employment.append(np.floor(future_value))  # Round down

    return future_employment

def save_forecasts_to_db(zipcodes, current_employment, future_employment):
    conn = connect_to_db()
    if not conn:
        print("Database connection failed.")
        return

    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS employment_prediction (
                zipcode TEXT PRIMARY KEY,
                current NUMERIC,
                future NUMERIC
            );
        """)

        cursor.execute("DELETE FROM employment_prediction;")

        for i in range(len(zipcodes)):
            cursor.execute("""
                INSERT INTO employment_prediction (zipcode, current, future)
                VALUES (%s, %s, %s);
            """, (zipcodes[i], int(current_employment[i]), int(future_employment[i])))  # Can't hire half a dude

        conn.commit()

    except Exception as e:
        print(f"Error saving forecast data: {e}")
        conn.rollback()
    finally:
        close_connection(cursor, conn)

def forecast_and_save(zipcodes, current_employment, employment_roc):
    print("\nForecasting future employment for the next year...")
    future_employment = forecast_employment(zipcodes, current_employment, employment_roc, years_ahead=1)

    print("\nPredicted Employment for the Next Year:")
    for i, zip_code in enumerate(zipcodes):
        print(f"ZIP Code {zip_code}: Current = {current_employment[i]:.2f}, Predicted = {future_employment[i]:.0f}")

    save_forecasts_to_db(zipcodes, current_employment, future_employment)

def regional_employment_trends():
    averages_data = fetch_employment_averages_data()

    if averages_data is None or len(averages_data) == 0:
        print("No employment averages data found to analyze.")
    else:
        zipcodes = [item[0] for item in averages_data]
        avg_employment = np.array([item[1] for item in averages_data])
        avg_annual_payroll = np.array([item[2] for item in averages_data])
        avg_employment_roc = np.array([item[3] for item in averages_data])

        analyze_employment_statistics(zipcodes, avg_employment, avg_annual_payroll, avg_employment_roc)

    forecasting_data = fetch_employment_data_for_forecasting()

    if forecasting_data is None or len(forecasting_data) == 0:
        print("No employment data found for forecasting.")
    else:
        zip_data = {}
        for row in forecasting_data:
            zipcode, year, employment, employment_roc = row
            if zipcode not in zip_data:
                zip_data[zipcode] = {'years': [], 'employment': [], 'employment_roc': []}
            zip_data[zipcode]['years'].append(year)
            zip_data[zipcode]['employment'].append(employment)
            zip_data[zipcode]['employment_roc'].append(employment_roc)

        current_zipcodes = []
        current_employment = []
        current_roc = []
        for zipcode, data in zip_data.items():
            current_year_idx = np.argmax(data['years'])
            current_zipcodes.append(zipcode)
            current_employment.append(data['employment'][current_year_idx])
            current_roc.append(data['employment_roc'][current_year_idx])

        # Forecast and save data for each zipcode using the current recent year data
        forecast_and_save(current_zipcodes, current_employment, current_roc)

if __name__ == "__main__":
    regional_employment_trends()

