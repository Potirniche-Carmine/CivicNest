from sklearn.tree import DecisionTreeRegressor
import matplotlib.pyplot as plt
import numpy as np
from db_connection import connect_to_db, close_connection

def fetch_employment_data():
    conn = connect_to_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT zipcode, avg_employment, avg_employment_roc
                FROM employment_averages;
            """)
            data = cursor.fetchall()
            return data
        except Exception as e:
            print(f"Error fetching data: {e}")
            return None
        finally:
            close_connection(cursor, conn)
    else:
        print("Unable to connect to the database.")
        return None

def forecast_employment(zipcodes, avg_employment, avg_employment_roc, years_ahead=5):
    future_employment = []
    model = DecisionTreeRegressor(random_state=0)

    for i in range(len(zipcodes)):
        x = np.array([avg_employment_roc[i]]).reshape(-1, 1)  # roc is the feature/independent variable
        y = np.array([avg_employment[i]])  #avg employment is dependent variable

        model.fit(x, y)
        future_roc = avg_employment_roc[i] + years_ahead
        predicted = model.predict(np.array([[future_roc]]))[0]
        future_employment.append(np.floor(predicted))  #Floor the prediction since ha;f a person can't work, no matter how much Bill Gates wants to try

        roc_range = np.linspace(min(avg_employment_roc) - 0.03, max(avg_employment_roc) + 0.03, 100).reshape(-1, 1)
        fitted_values = model.predict(roc_range)

        plt.figure(figsize=(6, 4))
        plt.plot(roc_range, fitted_values, label='Decision Tree Fit', color='blue')
        plt.scatter(avg_employment_roc[i], avg_employment[i], color='black', label='Current Data')
        plt.scatter(future_roc, predicted, color='red', label='Forecasted Point')
        plt.title(f"ZIP {zipcodes[i]}: Employment Forecast")
        plt.xlabel("Employment Rate of Change")
        plt.ylabel("Average Employment")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

    return future_employment

if __name__ == "__main__":
    print("Fetching data and forecasting employment using Decision Trees...")

    data = fetch_employment_data()
    if not data:
        print("No data available.")
    else:
        zipcodes = [str(row[0]) for row in data]
        avg_employment = np.array([row[1] for row in data])
        avg_employment_roc = np.array([row[2] for row in data])

        future_employment = forecast_employment(zipcodes, avg_employment, avg_employment_roc, years_ahead=1)
        print("\nForecasted Employment Values:")
        for i, zip_code in enumerate(zipcodes):
            print(f"ZIP Code {zip_code}: Current = {int(avg_employment[i])}, Forecast = {int(future_employment[i])}")



