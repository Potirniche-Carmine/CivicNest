import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()
#DB credentials
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")

def connect_to_db():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
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
        close_connection(cursor, conn)
    else:
        print("No connection established.")


