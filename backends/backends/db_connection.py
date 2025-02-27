import psycopg2

#DB credentials
DB_NAME = "dcaimsa6md4201"  
DB_USER = "ub23idbf5fs4n9" # There's a 9 at the end
DB_PASSWORD = "pc2bb30cd6a4689cab33cc7a5833a754114d1a191680a4b9a26f8855e75f08b4a"
DB_HOST = "c586ehe1mt2hev.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com"
DB_PORT = "5432"

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

def close_connection(cursor, conn):
    cursor.close()
    conn.close()

if __name__ == "__main__":
    conn = connect_to_db()  # This will only return the connection, makes the unpacking nice and easy
    if conn:
        cursor = conn.cursor()  # Now create the cursor separately, otherwise there will be a tuple error
        print("Connection established!")
        close_connection(cursor, conn)
    else:
        print("Failed to connect.")

# Tables in the database:
# User
# crimes
# houses, has columns zpid, price, lat, long, address
# schools
# users, probably redundant