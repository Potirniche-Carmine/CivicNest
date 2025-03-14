from db_connection import connect_to_db, close_connection

# fetches latitudes and longitudes from the "houses" table
def fetch_latitudes_longitudes(cursor):
    cursor.execute("SELECT lat, long FROM houses")
    locations = cursor.fetchall()  # This returns a list of tuples
    lat_long_list = [(lat, long) for lat, long in locations]  # Convert to a list of tuples (latitude, longitude)
    print(lat_long_list)
    return lat_long_list

def get_location_data():
    conn = connect_to_db()
    if conn is None:
        return None
    
    cursor = conn.cursor()
    lat_long_list = fetch_latitudes_longitudes(cursor)
    close_connection(cursor, conn)

    return lat_long_list


def fetch_location_data():
    lat_long_list = get_location_data()
    if lat_long_list is None:
        print("No location data found.")
        return None
    return lat_long_list


def store_cluster_centroids(centroids):
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()

        create_table_query = """
        CREATE TABLE IF NOT EXISTS cluster_table (
            cluster_id SERIAL PRIMARY KEY,
            latitude FLOAT NOT NULL,
            longitude FLOAT NOT NULL
        );
        """
        cursor.execute(create_table_query)

        delete_query = "DELETE FROM cluster_table;"
        cursor.execute(delete_query)

        insert_query = """
        INSERT INTO cluster_table (cluster_id, latitude, longitude)
        VALUES (%s, %s, %s);
        """
        for idx, centroid in enumerate(centroids):
            cursor.execute(insert_query, (idx + 1, centroid[0], centroid[1]))

        conn.commit()
        print("\nCluster centers (centroids) inserted into cluster_table:")

        fetch_query = """
        SELECT * FROM cluster_table;
        """
        cursor.execute(fetch_query)
        all_rows = cursor.fetchall()

        if all_rows:
            print("\nAll entries from the cluster_table:")
            for row in all_rows:
                try:
                    print(f"Cluster ID: {row[0]}, Latitude: {row[1]}, Longitude: {row[2]}")
                except IndexError:
                    print("Row doesn't match expected format. Columns may be different.")
        else:
            print("No clusters found in the cluster_table.")

        # Close the connection
        close_connection(cursor, conn)
    else:
        print("Failed to connect to the database.")

