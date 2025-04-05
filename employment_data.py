from db_connection import connect_to_db, close_connection
from cluster_data import cluster_data
import numpy as np

def fetch_employment_data(cursor):
    cursor.execute("""
        SELECT zipcode, avg_annual_pay
        FROM employment_averages
    """)
    data = cursor.fetchall()
    return data

def get_employment_data():
    conn = connect_to_db()
    if conn is None:
        print("Failed to connect to the database.")
        return None
    
    cursor = conn.cursor()
    data = fetch_employment_data(cursor)
    close_connection(cursor, conn)

    return data

# def store_cluster_results(cluster_assignments, zipcodes):
#     # Store the cluster results in the database
#     conn = connect_to_db()
#     if conn:
#         cursor = conn.cursor()
        
#         # Optionally, clear previous cluster assignments
#         cursor.execute("DELETE FROM cluster_table")
        
#         # Insert new cluster assignments
#         insert_query = """
#         INSERT INTO cluster_table (zipcode, cluster_id)
#         VALUES (%s, %s);
#         """
        
#         data_to_insert = [(zipcode, int(cluster_id) + 1) for zipcode, cluster_id in zip(zipcodes, cluster_assignments)]
#         cursor.executemany(insert_query, data_to_insert)
        
#         conn.commit()
#         print(f"Successfully stored cluster assignments for {len(data_to_insert)} zip codes.")
        
#         close_connection(cursor, conn)
#     else:
#         print("Failed to connect to the database.")

def cluster_employment_data():
    data = get_employment_data()
    
    if data is None or len(data) == 0:
        print("No employment data available to cluster.")
        return None, None, None
    
    zipcodes = [item[0] for item in data]
    avg_annual_pay = [item[1] for item in data]
    
    print("Average Annual Pay (before reshaping):", avg_annual_pay)
    
    # Ensure avg_annual_pay is a 1D list of floats/ints
    try:
        avg_annual_pay = np.array(avg_annual_pay)
    except Exception as e:
        print(f"Error converting avg_annual_pay to numpy array: {e}")
        return None, None, None
    
    #Check for any NaN
    if np.any(np.isnan(avg_annual_pay)) or np.any(np.isinf(avg_annual_pay)):
        print("Data contains NaN or infinite values.")
        return None, None, None
    
    #Reshape avg_annual_pay to be a 2D array with one feature
    try:
        avg_annual_pay_reshaped = avg_annual_pay.reshape(-1, 1)
        print("Reshaped Average Annual Pay:", avg_annual_pay_reshaped)
    except Exception as e:
        print(f"Error reshaping data: {e}")
        return None, None, None
    
    try:
        labels, centroids = cluster_data(avg_annual_pay_reshaped, k=4)
        print("Cluster Labels:", labels)
        print("Centroids:", centroids)
    except Exception as e:
        print(f"Error while clustering: {e}")
        return None, None, None

    return labels, centroids, zipcodes



