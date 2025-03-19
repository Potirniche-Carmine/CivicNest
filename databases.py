import psycopg2
import houses_API

DB_NAME = "dcaimsa6md4201"  
DB_USER = "ub23idbf5fs4n9" # There's a 9 at the end
DB_PASSWORD = "pc2bb30cd6a4689cab33cc7a5833a754114d1a191680a4b9a26f8855e75f08b4a"
DB_HOST = "c586ehe1mt2hev.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com"
DB_PORT = "5432"

# Connect to the database server
conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)

properties = houses_API.DataCollection()



cur = conn.cursor() # Cursor object


#Kaleo Sanchez helped with the queries for Table Creation
# Tables:
cur.execute('''DROP TABLE IF EXISTS houses CASCADE''')

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
                    zipcode VARCHAR(255),
                    price_change NUMERIC,
                    price_per_sqft NUMERIC
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
    city = property["city"]
    state = property["state"]
    zipcode = property["zipcode"]
    price_change = property["priceChange"]
    price_per_sqft = property["pricePerSquareFoot"]
    cur.execute('''INSERT INTO houses (zpid, address, price, lat, long, city, state, zipcode, price_change, price_per_sqft)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (zpid) DO UPDATE SET 
            address = EXCLUDED.address, price = EXCLUDED.price, lat = EXCLUDED.lat, long = EXCLUDED.long''', # This is incase we have no zpid
            (zpid, address, price,lat,long,city,state,zipcode,price_change,price_per_sqft))


# Commit the changes
conn.commit()

# Close the connection
cur.close()
conn.close()
