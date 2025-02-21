# db_connection.py
import psycopg2

# Database connection details
DB_NAME = "my_location_db"   # Change when ready
DB_USER = "postgres"
DB_PASSWORD = "Admit#762SQL" #This too
DB_HOST = "localhost" # I hope switching to online database is easy 
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
    
def close_connection(cursor, conn):
    cursor.close()
    conn.close()
