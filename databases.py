import psycopg2
import houses_API
import schools_API

# Connect to the database server
conn = psycopg2.connect(
    host="localhost",
    database="civicnest_db",
    user="brand",
    password="Admit#762SQL"
)

properties = houses_API.houses()
schools = schools_API.schools()


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
                    zpid SERIAL UNIQUE PRIMARY KEY,
                    address VARCHAR(255) NOT NULL,
                    price NUMERIC NOT NULL,
                    lat FLOAT,
                    long FLOAT
                )''')

cur.execute('''CREATE TABLE IF NOT EXISTS schools (
                    name VARCHAR(200) UNIQUE PRIMARY KEY,
                    grades VARCHAR(25),
                    rating INT
                )''')

#Go through house API contents
for property in properties:
    zpid = property["zpid"]
    address = property["address"]
    price = property["price"]
    lat = property["latitude"]
    long = property["longitude"]
    cur.execute('''INSERT INTO houses (zpid, address, price,lat,long)
            VALUES (%s, %s, %s)
            ON CONFLICT (zpid) DO UPDATE''', # This is incase we have no zpid
            (zpid, address, price,lat,long))


for school in schools:
    name = school["name"]
    grades = school["grades"]
    rating = school["rating"]

    cur.execute('''INSERT INTO schools (name, grades, rating)
        VALUES (%s, %s, %s)
        ON CONFLICT (name) DO NOTHING''',
        (name, grades, rating))



# Commit the changes
conn.commit()

# Close the connection
cur.close()
conn.close()
