import psycopg2

# Connect to the database server
conn = psycopg2.connect(
    host="localhost",
    database="civicnest_db",
    user="brand",
    password="Admit#762SQL"
)

# Create a cursor object
cur = conn.cursor()

# Create a table
cur.execute('''CREATE TABLE IF NOT EXISTS users (
                    account SERIAL PRIMARY KEY,
                    first_name TEXT,
                    last_name TEXT,
                    created_on date
                )''')

# Commit the changes
conn.commit()

# Close the connection
cur.close()
conn.close()