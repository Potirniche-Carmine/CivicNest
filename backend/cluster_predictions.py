from db_connection import connect_to_db, close_connection

def update_cluster_insights_table(cursor, conn, averages, growth):
    cursor.execute("""
      CREATE TABLE IF NOT EXISTS cluster_insights (
        cluster_id INTEGER PRIMARY KEY,
        avg_payroll NUMERIC,
        median_price NUMERIC,
        employment_growth NUMERIC
      );
    """)
    cursor.execute("DELETE FROM cluster_insights;")
    insert_sql = """
      INSERT INTO cluster_insights
        (cluster_id, avg_payroll, median_price, employment_growth)
      VALUES (%s, %s, %s, %s);
    """
    for cid, avg_pay, med_pr in averages:
        emp = growth.get(cid)
        cursor.execute(insert_sql, (cid, avg_pay, med_pr, emp))
    conn.commit()

def display_cluster_zipcode_percentages(cursor):
    zip_to_cluster = {}
    assigned_zips = set()
    cursor.execute("""
      SELECT ct.cluster_id, h.zipcode,
             COUNT(*) AS house_count,
             ROUND(100.0 * COUNT(*) 
               / SUM(COUNT(*)) OVER (PARTITION BY ct.cluster_id), 2)
               AS pct_within_cluster
      FROM houses h
      JOIN cluster_table ct ON h.zpid = ct.zpid
      GROUP BY ct.cluster_id, h.zipcode
      ORDER BY ct.cluster_id, h.zipcode;
    """)
    for cluster_id, zipcode, count, pct in cursor.fetchall():
        print(f"Cluster {cluster_id} → ZIP {zipcode}: {count} homes ({pct}%)")
    cursor.execute("""
      SELECT h.zipcode, ct.cluster_id, COUNT(*) AS house_count
      FROM houses h
      JOIN cluster_table ct ON h.zpid = ct.zpid
      GROUP BY h.zipcode, ct.cluster_id
      ORDER BY h.zipcode, house_count DESC;
    """)
    for zipcode, cluster_id, _ in cursor.fetchall():
        if zipcode not in assigned_zips:
            zip_to_cluster[zipcode] = cluster_id
            assigned_zips.add(zipcode)
    print("\nAssigned ZIP → Cluster:")
    for z,c in zip_to_cluster.items():
        print(f"{z} → {c}")

def cluster_house_counts(cursor):
    cursor.execute("""
      SELECT ct.cluster_id, COUNT(*) AS house_count
      FROM houses h
      JOIN cluster_table ct ON h.zpid = ct.zpid
      GROUP BY ct.cluster_id
      ORDER BY ct.cluster_id;
    """)
    for cid, count in cursor.fetchall():
        print(f"Cluster {cid}: {count} homes")

def fetch_employment_growth_by_cluster(cursor):
    cursor.execute("""
      SELECT ct.cluster_id, ROUND(AVG(ep.percent_change)::numeric, 2)
      FROM cluster_table ct
      JOIN houses h ON ct.zpid = h.zpid
      JOIN employment_prediction ep ON h.zipcode = ep.zipcode::TEXT
      GROUP BY ct.cluster_id
      ORDER BY ct.cluster_id;
    """)
    return dict(cursor.fetchall())

def calculate_cluster_averages(cursor):
    cursor.execute("""
      SELECT ct.cluster_id,
             ROUND(AVG(ea.avg_annual_payroll/NULLIF(ea.avg_employment,0))::numeric, 2) AS avg_payroll,
             ROUND(AVG(h.price)::numeric, 2)                                   AS median_price
      FROM cluster_table ct
      JOIN houses h ON ct.zpid = h.zpid
      JOIN employment_averages ea ON h.zipcode::TEXT = ea.zipcode::TEXT
      GROUP BY ct.cluster_id
      ORDER BY ct.cluster_id;
    """)
    return cursor.fetchall()  # list of (cluster_id, avg_payroll, median_price)

def cluster_predictions():
    conn = connect_to_db()
    cur = conn.cursor()
    cluster_house_counts(cur)
    growth = fetch_employment_growth_by_cluster(cur)
    averages = calculate_cluster_averages(cur)
    update_cluster_insights_table(cur, conn, averages, growth)
    display_cluster_zipcode_percentages(cur)
    close_connection(cur, conn)

if __name__ == "__main__":
    cluster_predictions()