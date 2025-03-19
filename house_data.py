from db_connection import connect_to_db, close_connection

def fetch_house_data(cursor):
    cursor.execute("SELECT zpid, price FROM houses")
    houses = cursor.fetchall()
    return houses

def get_house_data():
    conn = connect_to_db()
    if conn is None:
        print("Failed to connect to the database.")
        return None
    
    cursor = conn.cursor()
    houses = fetch_house_data(cursor)
    close_connection(cursor, conn)

    return houses

def fetch_price_data():
    houses = get_house_data()
    if houses is None or len(houses) == 0:
        print("No house data found.")
        return None
    
    price_list = [house[1] for house in houses]
    return price_list

def fetch_house_ids():
    houses = get_house_data()
    if houses is None or len(houses) == 0:
        print("No house data found.")
        return None
    
    id_list = [house[0] for house in houses]
    return id_list

def store_cluster_centroids(centroids):
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        
        cursor.execute("DELETE FROM cluster_centroids")
        
        insert_query = """
        INSERT INTO cluster_centroids (cluster_id, price)
        VALUES (%s, %s);
        """
        
        for idx, centroid in enumerate(centroids):
            if hasattr(centroid, '__iter__') and not isinstance(centroid, str):
                price = float(centroid[0])
            else:
                price = float(centroid)
                
            cursor.execute(insert_query, (idx + 1, price))

        conn.commit()
        print(f"Stored {len(centroids)} cluster centroids in database")
        
        close_connection(cursor, conn)
    else:
        print("Failed to connect to the database.")

def store_house_cluster_assignments(house_ids, cluster_assignments):
    if len(house_ids) != len(cluster_assignments):
        print("Error: Number of house IDs doesn't match number of cluster assignments")
        return False
    
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        
        cursor.execute("DELETE FROM house_clusters")
        
        insert_query = """
        INSERT INTO house_clusters (house_id, cluster_id)
        VALUES (%s, %s);
        """
        
        for house_id, cluster_id in zip(house_ids, cluster_assignments):
            cursor.execute(insert_query, (house_id, int(cluster_id) + 1))

        conn.commit()
        print(f"Stored cluster assignments for {len(house_ids)} houses")
        
        close_connection(cursor, conn)
        return True
    else:
        print("Failed to connect to the database.")
        return False

def fetch_cluster_results():
    conn = connect_to_db()
    if conn is None:
        print("Failed to connect to the database.")
        return None
    
    cursor = conn.cursor()
    
    cursor.execute("SELECT cluster_id, price FROM cluster_centroids ORDER BY cluster_id")
    centroids = cursor.fetchall()
    
    cursor.execute("""
        SELECT h.id, h.price, hc.cluster_id 
        FROM houses h
        JOIN house_clusters hc ON h.id = hc.house_id
        ORDER BY hc.cluster_id, h.price
    """)
    house_clusters = cursor.fetchall()
    
    close_connection(cursor, conn)
    
    return {
        'centroids': centroids,
        'house_clusters': house_clusters
    }

if __name__ == "__main__":
    prices = fetch_price_data()
    if prices:
        print(f"Retrieved {len(prices)} house prices")
        print(f"Price range: ${min(prices):.2f} - ${max(prices):.2f}")