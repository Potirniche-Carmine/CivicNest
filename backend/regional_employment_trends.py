import numpy as np
import pandas as pd
from db_connection import connect_to_db, close_connection


def fetch_employment_averages_data():
    conn = connect_to_db()
    if not conn:
        print("Could not connect to DB.")
        return None

    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT zipcode, avg_employment, avg_annual_payroll, avg_employment_roc
            FROM employment_averages;
        """)
        data = cursor.fetchall()
        return data

    except Exception as e:
        print("Something went wrong while getting averages:", e)
        return None
    finally:
        close_connection(cursor, conn)

def fetch_employment_data_for_forecasting():
    conn = connect_to_db()
    if not conn:
        print("DB connection failed.")
        return None

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
        print("Error getting employment data for forecast:", e)
        return None
    finally:
        close_connection(cursor, conn)

def analyze_employment_statistics(zipcodes, avg_employment, avg_annual_payroll, avg_employment_roc):
    print("Analyzing employment stats:")

    # max and min employment
    max_emp = max(avg_employment)
    min_emp = min(avg_employment)
    max_emp_idx = avg_employment.tolist().index(max_emp)
    min_emp_idx = avg_employment.tolist().index(min_emp)

    print(f"Highest employment: {zipcodes[max_emp_idx]} with {max_emp}")
    print(f"Lowest employment: {zipcodes[min_emp_idx]} with {min_emp}")

    # growth rate
    max_growth = max(avg_employment_roc)
    min_growth = min(avg_employment_roc)
    high_growth_idx = avg_employment_roc.tolist().index(max_growth)
    low_growth_idx = avg_employment_roc.tolist().index(min_growth)

    print(f"Best employment growth: {zipcodes[high_growth_idx]} at {max_growth}")
    print(f"Worst employment growth: {zipcodes[low_growth_idx]} at {min_growth}")

    # wages
    max_pay = max(avg_annual_payroll)
    min_pay = min(avg_annual_payroll)
    high_pay_idx = avg_annual_payroll.tolist().index(max_pay)
    low_pay_idx = avg_annual_payroll.tolist().index(min_pay)

    print(f"Highest payroll: {zipcodes[high_pay_idx]} with ${max_pay}")
    print(f"Lowest payroll: {zipcodes[low_pay_idx]} with ${min_pay}")

    # significant growth, greater than 5 percent 
    print("\nZIPs with strong growth (>5%):")
    for i in range(len(zipcodes)):
        if avg_employment_roc[i] > 0.05:
            print(zipcodes[i])

# project future employment using ROC
def forecast_employment(zipcodes, current_employment, employment_roc, years_ahead=1):
    forecasts = []

    for i in range(len(zipcodes)):
        emp = current_employment[i]
        growth = employment_roc[i]
        projected = emp * ((1 + growth) ** years_ahead)
        forecasts.append(int(projected))

    return forecasts

# save forecast into DB
def save_forecasts_to_db(zipcodes, current_employment, future_employment):
    conn = connect_to_db()
    if not conn:
        print("Can't connect to DB to save forecasts.")
        return

    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS employment_prediction (
                zipcode TEXT PRIMARY KEY,
                percent_change NUMERIC
            );
        """)
        cursor.execute("DELETE FROM employment_prediction;")

        for i in range(len(zipcodes)):
            curr = current_employment[i]
            fut = future_employment[i]
            if curr == 0:
                pct_change = 0
            else:
                pct_change = ((fut - curr) / curr) * 100

            cursor.execute("""
                INSERT INTO employment_prediction (zipcode, percent_change)
                VALUES (%s, %s);
            """, (zipcodes[i], round(pct_change, 2)))

        conn.commit()

    except Exception as e:
        print("Error while saving forecasts:", e)
        conn.rollback()
    finally:
        close_connection(cursor, conn)

# wraping to do forecast and save
def forecast_and_save(zipcodes, current_employment, employment_roc):
    print("\nStarting forecast...")

    future_vals = forecast_employment(zipcodes, current_employment, employment_roc)

    print("Future employment predictions:")
    for i in range(len(zipcodes)):
        print(f"{zipcodes[i]}: now = {current_employment[i]}, future = {future_vals[i]}")

    save_forecasts_to_db(zipcodes, current_employment, future_vals)

def regional_employment_trends():
    print("Fetching average employment data:")
    averages = fetch_employment_averages_data()

    if not averages:
        print("No average data found.")
    else:
        zipcodes = [row[0] for row in averages]
        avg_emp = np.array([row[1] for row in averages])
        avg_pay = np.array([row[2] for row in averages])
        avg_roc = np.array([row[3] for row in averages])

        analyze_employment_statistics(zipcodes, avg_emp, avg_pay, avg_roc)

    print("\nFetching forecasting data:")
    forecast_data = fetch_employment_data_for_forecasting()

    if not forecast_data:
        print("No forecast data found.")
        return

    zip_dict = {}

    for row in forecast_data:
        zipc, yr, emp, roc = row
        if zipc not in zip_dict:
            zip_dict[zipc] = {'years': [], 'employment': [], 'roc': []}
        zip_dict[zipc]['years'].append(yr)
        zip_dict[zipc]['employment'].append(emp)
        zip_dict[zipc]['roc'].append(roc)

    zips, curr_emp, curr_roc = [], [], []

    for zipc, vals in zip_dict.items():
        idx = vals['years'].index(max(vals['years']))
        zips.append(zipc)
        curr_emp.append(vals['employment'][idx])
        curr_roc.append(vals['roc'][idx])

    forecast_and_save(zips, curr_emp, curr_roc)

if __name__ == "__main__":
    regional_employment_trends()
