from db_connection import connect_to_db, close_connection
# Table houses, has columns zpid, price, lat, long, address
# Fetch all latitudes and longitudes into a list
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
    lat_lon_list = fetch_latitudes_longitudes(cursor)
    close_connection(cursor, conn)

    return lat_lon_list

