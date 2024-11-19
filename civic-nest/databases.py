import psycopg2

# Connect to the database server
conn = psycopg2.connect(
    host="localhost",
    database="civicnest_db",
    user="brand",
    password="Admit#762SQL"
)

cur = conn.cursor() # Cursor object

# Tables:
cur.execute('''CREATE TABLE IF NOT EXISTS users (
                    account TEXT PRIMARY KEY,
                    first_name TEXT,
                    last_name TEXT,
                    created_on date
                )''')

cur.execute('''CREATE TABLE IF NOT EXISTS crimes (
                    crime_id SERIAL PRIMARY KEY,
                    type TEXT,
                    description TEXT,
                    location TEXT,
                    date_reported date
                )''')

cur.execute('''CREATE TABLE IF NOT EXISTS houses (
                    house_address TEXT PRIMARY KEY,
                    type TEXT,
                    num_rooms INT,
                    size FLOAT,
                    price FLOAT
                )''')

cur.execute('''CREATE TABLE IF NOT EXISTS schools (
                    school_address TEXT PRIMARY KEY,
                    type TEXT,
                    isPublic BOOLEAN,
                    rating FLOAT,
                    location TEXT
                )''')

# Commit the changes
conn.commit()

# Close the connection
cur.close()
conn.close()