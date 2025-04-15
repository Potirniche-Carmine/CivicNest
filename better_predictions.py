from db_connection import connect_to_db, close_connection

def workers_per_zip_code(conn, cur):
    cur = conn.cursor()
    sql = """
    SELECT zipcode, year, employment, establishments, annual_payroll,
    CASE 
        WHEN establishments > 0 THEN employment::FLOAT / establishments
        ELSE NULL
    END as workers_per_zip_code,
    CASE 
        WHEN establishments > 0 THEN annual_payroll::FLOAT / establishments
        ELSE NULL
    END as avg_payroll_per_establishment,
    CASE 
        WHEN employment > 0 THEN annual_payroll::FLOAT / employment
        ELSE NULL
    END as avg_payroll_per_worker
    FROM employment;
    """
    cur.execute(sql)
    results = cur.fetchall()

    def safe_format(val):
        return f"{val:.2f}" if val is not None else "N/A"

    for r in results:
        zipc, year, emp, est, payroll, workers_per_est, payroll_per_est, payroll_per_worker = r
        print(f"Zip: {zipc}, Year: {year}, Avg Workers per Business: {safe_format(workers_per_est)}, "
              f"Avg Payroll per Business: {safe_format(payroll_per_est)}, Avg Payroll per Worker: {safe_format(payroll_per_worker)}")

def cluster_distribution_by_zipcode(conn, cur):
    cur = conn.cursor()
    sql = """SELECT 
        h.zipcode,
        ct.cluster_id,
        COUNT(*) AS house_count,
        ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (PARTITION BY h.zipcode), 2) AS percent_within_zipcode
    FROM houses h
    JOIN cluster_table ct ON h.zpid = ct.zpid
    GROUP BY h.zipcode, ct.cluster_id
    ORDER BY h.zipcode, ct.cluster_id;
    """
    cur.execute(sql)
    results = cur.fetchall()

    print("\nCluster Distribution per Zip Code")
    for zipc, cluster_id, count, percent in results:
        print(f"Zip: {zipc}, Cluster: {cluster_id}, Houses: {count}, Percentage of houses in this ZIP code that belong to this price cluster: {percent}%")

def employment_and_payroll_by_cluster(conn, cur):
    cur = conn.cursor()
    sql = """SELECT 
        ct.cluster_id,
        ROUND(AVG(ea.avg_employment)::numeric, 2) AS avg_employment_in_cluster,
        ROUND(AVG(
            CASE 
                WHEN ea.avg_employment > 0 THEN ea.avg_annual_payroll::FLOAT / ea.avg_employment
                ELSE NULL
            END
        )::numeric, 2) AS avg_payroll_per_worker_in_cluster
    FROM cluster_table ct
    JOIN houses h ON ct.zpid = h.zpid
    JOIN employment_averages ea ON h.zipcode::INT = ea.zipcode
    GROUP BY ct.cluster_id
    ORDER BY ct.cluster_id;
    """
    cur.execute(sql)
    results = cur.fetchall()

    print("\nAverage Employment and Payroll per Worker by Cluster")
    for cluster_id, avg_emp, avg_pay_per_worker in results:
        print(f"Cluster: {cluster_id}, Avg Employment per ZIP: {avg_emp}, Avg Payroll per Worker: {avg_pay_per_worker}")

def payroll_vs_price_ratio_by_cluster(conn, cur):
    cur = conn.cursor()
    sql = """
    SELECT 
        ct.cluster_id,
        ROUND(AVG(ea.avg_annual_payroll::FLOAT / NULLIF(ea.avg_employment, 0))::numeric, 2) AS avg_pay_per_worker,
        ROUND(AVG(h.price)::numeric, 2) AS avg_house_price,
        ROUND((
            AVG(ea.avg_annual_payroll::FLOAT / NULLIF(ea.avg_employment, 0)) 
            / NULLIF(AVG(h.price), 0)
        )::numeric, 4) AS payroll_to_price_ratio
    FROM cluster_table ct
    JOIN houses h ON ct.zpid = h.zpid
    JOIN employment_averages ea ON h.zipcode::INT = ea.zipcode
    GROUP BY ct.cluster_id
    ORDER BY ct.cluster_id;
    """
    cur.execute(sql)
    return cur.fetchall()

def predicted_employment_growth_by_cluster(conn, cur):
    cur = conn.cursor()
    sql = """
    SELECT 
        ct.cluster_id,
        ROUND(AVG(ep.percent_change)::numeric, 2) AS avg_predicted_employment_growth
    FROM cluster_table ct
    JOIN houses h ON ct.zpid = h.zpid
    JOIN employment_prediction ep ON h.zipcode = ep.zipcode::TEXT
    GROUP BY ct.cluster_id
    ORDER BY ct.cluster_id;
    """
    cur.execute(sql)
    results = cur.fetchall()

    print("\nProjected Employment Growth by Cluster")
    for cluster_id, avg_growth in results:
        print(f"Cluster {cluster_id}: Avg Employment Growth = {avg_growth}%")

def growth_vs_payroll_and_price(conn, cur):
    cur = conn.cursor()
    sql = """
    SELECT 
        ct.cluster_id,
        ROUND(AVG(ep.percent_change)::numeric, 2) AS avg_growth,
        ROUND(AVG(ea.avg_annual_payroll)::numeric, 2) AS avg_payroll,
        ROUND(AVG(cc.price)::numeric, 2) AS avg_cluster_price
    FROM cluster_table ct
    JOIN houses h ON ct.zpid = h.zpid
    JOIN employment_prediction ep ON h.zipcode = ep.zipcode::TEXT
    JOIN employment_averages ea ON h.zipcode = ea.zipcode::TEXT
    JOIN cluster_centroids cc ON ct.cluster_id = cc.cluster_id
    GROUP BY ct.cluster_id
    ORDER BY ct.cluster_id;
    """
    cur.execute(sql)
    results = cur.fetchall()

    print("\nProjected Employment Growth vs Payroll and Price (by Cluster)")
    for cluster_id, avg_growth, avg_payroll, avg_price in results:
        print(f"Cluster {cluster_id}:")
        print(f"Avg Growth: {avg_growth}%")
        print(f"Avg Payroll: ${avg_payroll}")
        print(f"Avg House Price: ${avg_price}\n")

def update_insights_table(conn, cur, values):
    cur.execute("""
    CREATE TABLE IF NOT EXISTS insights_table (
        cluster_id INTEGER PRIMARY KEY,
        avg_payroll NUMERIC,
        avg_price NUMERIC,
        affordability_ratio NUMERIC
    );
    """)

    cur.execute("DELETE FROM insights_table;")

    for cluster_id, avg_payroll, avg_price, ratio in values:
        cur.execute("""
            INSERT INTO insights_table (cluster_id, avg_payroll, avg_price, affordability_ratio)
            VALUES (%s, %s, %s, %s)
        """, (cluster_id, avg_payroll, avg_price, ratio))

    conn.commit()
    print("\ninsights_table updated successfully.")

def better_predictions():
    conn = connect_to_db()
    cur = conn.cursor()
    if conn is None:
        print("Connection failed.")
        return

    workers_per_zip_code(conn, cur)

    if conn is not None:
        cluster_distribution_by_zipcode(conn, cur)
        employment_and_payroll_by_cluster(conn, cur)
        results = payroll_vs_price_ratio_by_cluster(conn, cur)
        predicted_employment_growth_by_cluster(conn, cur)
        growth_vs_payroll_and_price(conn, cur)
        update_insights_table(conn, cur, results)

    close_connection(cur, conn)

if __name__ == "__main__":
    better_predictions()
