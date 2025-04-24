#THIS FILE IS ONLY USED TO CREATE NEW TABLES. I'M TOO LAZY TO DO IT ALL IN POSTGRES.

from db_connection import connect_to_db, close_connection

def create_table(cursor):
    try:
        create_table_query = """
        CREATE TABLE IF NOT EXISTS price_cluster (
            id SERIAL PRIMARY KEY,       
            price INT NOT NULL,           
            cluster_label INT NOT NULL    
        );
        """
        cursor.execute(create_table_query)
        print("Table created successfully!")
    except Exception as e:
        print(f"Error creating table: {e}")

def display_all_tables(cursor):
    """
    Displays all the tables in the current database.
    """
    try:
        cursor.execute("""
        SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'public';  -- Filter only 'public' schema tables
        """)
        
        tables = cursor.fetchall()
        
        if tables:
            print("\nList of all tables in the database:")
            for table in tables:
                print(table[0])  #Each table name is stored as a tuple (table_name,)
        else:
            print("No tables found in the database.")
    except Exception as e:
        print(f"Error retrieving tables: {e}")

if __name__ == "__main__":
    conn = connect_to_db()
    if conn:
        cursor = conn.cursor()
        print("Connection established!")
        
        # Create the table
        create_table(cursor)  #Comment out if you want to display only the tables. 
        
        display_all_tables(cursor)
    
        conn.commit()
        
        # Close the connection
        close_connection(cursor, conn)
    else:
        print("Failed to connect.")

