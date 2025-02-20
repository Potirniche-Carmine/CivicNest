# fetch_data.py
import psycopg2

#import API files at some point between now and May (that's only a joke)


# These five lines can be added to a script to make the testing process easier
DB_NAME = "my_location_db"  # Dummy database
DB_USER = "postgres"
DB_PASSWORD = "Admit#762SQL"  # Should be changed
DB_HOST = "localhost" # THe transition from local to actual should be easy, I hope
DB_PORT = "5432"  

# Connect to the PostgreSQL database
def connect_to_db():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        print("Connected to the database successfully!")
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

#fetch all latitudes and longitudes into a list
def fetch_latitudes_longitudes(cursor):
    cursor.execute("SELECT latitude, longitude FROM locations")
    locations = cursor.fetchall()  # This returns a list of tuples
    lat_lon_list = [(lat, lon) for lat, lon in locations]  # Convert to a list of tuples (latitude, longitude)
    return lat_lon_list

def close_connection(cursor, conn):
    cursor.close()
    conn.close()

# Main function to get latitudes and longitudes from the database
def get_location_data():
    conn = connect_to_db()
    if conn is None:
        return None
    
    cursor = conn.cursor()
    lat_lon_list = fetch_latitudes_longitudes(cursor)
    close_connection(cursor, conn)
    
    return lat_lon_list
