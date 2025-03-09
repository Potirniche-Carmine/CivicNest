import numpy as np
from sklearn.cluster import KMeans
import fetch_location
import fetch_prices
from db_connection import connect_to_db, close_connection  # Import database connection functions

# Fetch data (data, price, or otherwise if needed)
lat_long_list = fetch_location.get_location_data()
# lat_long_list = fetch_prices.get_location_data()  # Should be price list

if lat_long_list is None:
    print("No data to cluster.")
    exit()

lat_long_array = np.array(lat_long_list)  # Convert the list into a numpy array (required for scikit-learn)

# adaboost might be better
# Switch to GPU, maybe use Pytorch or tensorflow

k = 3  # Using 3 clusters as an example. Might be changed? runtime for this algorithm is terrible
kmeans = KMeans(n_clusters=k, random_state=42)

kmeans.fit(lat_long_array)

# Get the cluster labels (which cluster each point belongs to)
labels = kmeans.labels_

# Get the centroid of each cluster
centroids = kmeans.cluster_centers_

print("\nCluster centers (centroids):")
for idx, centroid in enumerate(centroids):
    print(f"Cluster {idx + 1}: Latitude: {centroid[0]}, Longitude: {centroid[1]}")

print("\nLocation clusters:")
for i, label in enumerate(labels):
    print(f"Location {lat_long_list[i]} is in Cluster {label + 1}")

# Connect to the database
conn = connect_to_db()
if conn:
    cursor = conn.cursor()

    # Create the cluster_table if it doesn't exist
    create_table_query = """
    CREATE TABLE IF NOT EXISTS cluster_table (
        id SERIAL PRIMARY KEY,
        cluster_id INT NOT NULL,
        latitude FLOAT NOT NULL,
        longitude FLOAT NOT NULL
    );
    """
    cursor.execute(create_table_query)

    delete_query = "DELETE FROM cluster_table;"# Empties the cluster_table before inserting new data
    cursor.execute(delete_query)

    insert_query = """
    INSERT INTO cluster_table (cluster_id, latitude, longitude)
    VALUES (%s, %s, %s);
    """
    for idx, centroid in enumerate(centroids):
        cursor.execute(insert_query, (idx + 1, centroid[0], centroid[1]))

    conn.commit()

    print("\nCluster centers (centroids) inserted into cluster_table:")
    for idx, centroid in enumerate(centroids):
        print(f"Cluster {idx + 1}: Latitude: {centroid[0]}, Longitude: {centroid[1]}")

    # Query to fetch all rows from the cluster_table
    fetch_query = """
    SELECT * FROM cluster_table;
    """
    
    cursor.execute(fetch_query)
    all_rows = cursor.fetchall()  # Fetch all rows from the result

    # Check if any rows were found and display them
    if all_rows:
        print("\nAll entries from the cluster_table:")
        for row in all_rows:
            # Print out the entire row to debug its structure
            print(f"Row data: {row}")
            # Now print individual elements safely
            try:
                print(f"ID: {row[0]}, Cluster ID: {row[1]}, Latitude: {row[2]}, Longitude: {row[3]}")
            except IndexError:
                print("Row doesn't match expected format. Columns may be different.")
    else:
        print("No clusters found in the cluster_table.")

    # Close the connection
    close_connection(cursor, conn)
else:
    print("Failed to connect to the database.")

