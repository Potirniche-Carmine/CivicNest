from db_connection import connect_to_db, close_connection

# Fetch all latitudes and longitudes into a list
def fetch_latitudes_longitudes(cursor):
    cursor.execute("SELECT latitude, longitude FROM locations")
    locations = cursor.fetchall()  # This returns a list of tuples
    lat_lon_list = [(lat, lon) for lat, lon in locations]  # Convert to a list of tuples (latitude, longitude)
    return lat_lon_list

def get_location_data():
    conn = connect_to_db()
    if conn is None:
        return None
    
    cursor = conn.cursor()
    lat_lon_list = fetch_latitudes_longitudes(cursor)
    close_connection(cursor, conn)
    
    return lat_lon_list

