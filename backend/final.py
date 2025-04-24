from db_connection import connect_to_db, close_connection

def create_final_insights_table(cursor):
    cursor.execute("DROP TABLE IF EXISTS final_insights_table;")
    cursor.execute("""
        CREATE TABLE final_insights_table (
            zipcode VARCHAR PRIMARY KEY,
            pct_cluster_1 NUMERIC,
            pct_cluster_2 NUMERIC,
            pct_cluster_3 NUMERIC,
            pct_cluster_4 NUMERIC,
            assigned_cluster INTEGER
        );
    """)

def populate_final_insights_table(cursor):
    cursor.execute("""
        WITH cluster_zip_counts AS (
            SELECT 
                h.zipcode,
                ct.cluster_id,
                COUNT(*) AS house_count
            FROM houses h
            JOIN cluster_table ct ON h.zpid = ct.zpid
            GROUP BY h.zipcode, ct.cluster_id
        ),
        total_zip_counts AS (
            SELECT zipcode, SUM(house_count) AS total
            FROM cluster_zip_counts
            GROUP BY zipcode
        ),
        percentages AS (
            SELECT 
                c.zipcode,
                c.cluster_id,
                ROUND(100.0 * c.house_count / t.total, 2) AS pct
            FROM cluster_zip_counts c
            JOIN total_zip_counts t ON c.zipcode = t.zipcode
        ),
        pivoted AS (
            SELECT 
                zipcode,
                MAX(CASE WHEN cluster_id = 1 THEN pct ELSE 0 END) AS pct_cluster_1,
                MAX(CASE WHEN cluster_id = 2 THEN pct ELSE 0 END) AS pct_cluster_2,
                MAX(CASE WHEN cluster_id = 3 THEN pct ELSE 0 END) AS pct_cluster_3,
                MAX(CASE WHEN cluster_id = 4 THEN pct ELSE 0 END) AS pct_cluster_4
            FROM percentages
            GROUP BY zipcode
        )
        SELECT 
            zipcode,
            pct_cluster_1,
            pct_cluster_2,
            pct_cluster_3,
            pct_cluster_4,
            CASE 
                WHEN pct_cluster_1 >= GREATEST(pct_cluster_2, pct_cluster_3, pct_cluster_4) THEN 1
                WHEN pct_cluster_2 >= GREATEST(pct_cluster_1, pct_cluster_3, pct_cluster_4) THEN 2
                WHEN pct_cluster_3 >= GREATEST(pct_cluster_1, pct_cluster_2, pct_cluster_4) THEN 3
                ELSE 4
            END AS assigned_cluster
        FROM pivoted;
    """)
    rows = cursor.fetchall()

    for row in rows:
        cursor.execute("""
            INSERT INTO final_insights_table (
                zipcode, pct_cluster_1, pct_cluster_2, pct_cluster_3, pct_cluster_4, assigned_cluster
            ) VALUES (%s, %s, %s, %s, %s, %s)
        """, row)

    print("final_insights_table created and populated.")

def generate_final_insights():
    conn = connect_to_db()
    if not conn:
        print("Failed to connect to the database.")
        return
    cursor = conn.cursor()

    create_final_insights_table(cursor)
    populate_final_insights_table(cursor)

    conn.commit()
    close_connection(cursor, conn)

if __name__ == "__main__":
    generate_final_insights()



