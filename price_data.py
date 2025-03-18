from db_connection import connect_to_db, close_connection

def fetch_prices(cursor):
    cursor.execute("SELECT price FROM houses")
    prices = cursor.fetchall()
    price_list = [price[0] for price in prices]
    print(price_list)
    return price_list

def get_price_data():
    conn = connect_to_db()
    if conn is None:
        return None
    
    cursor = conn.cursor()
    price_list = fetch_prices(cursor)
    close_connection(cursor, conn)

    return price_list


def fetch_price_data():
    price_list = get_price_data()
    if price_list is None:
        print("No price data found.")
        return None
    return price_list


def store_cluster_centroids(centroids):
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        insert_query = """
        INSERT INTO cluster_table (cluster_id, price)
        VALUES (%s, %s);
        """
        for idx, centroid in enumerate(centroids):
            price = centroid[0]  #Modification, numpy array with single value
            cursor.execute(insert_query, (idx + 1, price))

        conn.commit()
        print("\nCluster centers (centroids) inserted into price_cluster_table:")

        fetch_query = """
        SELECT * FROM cluster_table;
        """
        cursor.execute(fetch_query)
        all_rows = cursor.fetchall()

        if all_rows:
            print("\nAll entries from the price_cluster_table:")
            for row in all_rows:
                try:
                    print(f"Cluster ID: {row[0]}, Price: {row[1]}")
                except IndexError:
                    print("Row doesn't match expected format. Columns may be different.")
        else:
            print("No clusters found in the cluster_table.")

        # Close the connection
        close_connection(cursor, conn)
    else:
        print("Failed to connect to the database.")
