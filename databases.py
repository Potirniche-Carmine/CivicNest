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

properties = houses_API.DataCollection()
schools = schools_API.schools()


cur = conn.cursor() # Cursor object


#Kaleo Sanchez helped with the queries for Table Creation
# Tables:
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
                    long FLOAT,
                    city VARCHAR(255) NOT NULL,
                    state VARCHAR(255) NOT NULL,
                    zipcod INT,
                    price_change NUMERIC NOT NULL,
                    price_per_sqft NUMERIC NOT NULL
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
    price = property["value"]
    lat = property["latitude"]
    long = property["longitude"]
    city = property["city"]
    state = property["state"]
    zipcode = property["state"]
    price_change = property["priceChange"]
    price_per_sqft = property["pricePerSquareFoot"]
    cur.execute('''INSERT INTO houses (zpid, address, price, lat, long, city, state, zipcode, price_change, price_per_sqft)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (zpid) DO UPDATE SET 
            address = EXCLUDED.address, price = EXCLUDED.price, lat = EXCLUDED.lat, long = EXCLUDED.long''', # This is incase we have no zpid
            (zpid, address, price,lat,long,city,state,zipcode,price_change,price_per_sqft))


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
