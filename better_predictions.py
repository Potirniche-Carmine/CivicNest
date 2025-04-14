from db_connection import connect_to_db, close_connection

def workers_per_zip_code(conn):
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
        zipc = r[0]
        year = r[1]
        emp = r[2]
        est = r[3]
        payroll = r[4]
        workers_per_est = r[5]
        payroll_per_est = r[6]
        payroll_per_worker = r[7]
        print(f"Zip: {zipc}, Year: {year}, Avg Workers per Business: {safe_format(workers_per_est)}, "
              f"Avg Payroll per Business: {safe_format(payroll_per_est)}, Avg Payroll per Worker: {safe_format(payroll_per_worker)}")

    close_connection(cur, conn)

def cluster_distribution_by_zipcode(conn):
    cur = conn.cursor()

    sql = """
    SELECT 
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
    for row in results:
        zipc = row[0]
        cluster_id = row[1]
        count = row[2]
        percent = row[3]
        print(f"Zip: {zipc}, Cluster: {cluster_id}, Houses: {count}, Percentage of houses in this ZIP code that belong to this price cluster: {percent}%")

    close_connection(cur, conn)

def employment_and_payroll_by_cluster(conn):
    cur = conn.cursor()

    sql = """
    SELECT 
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
    for row in results:
        cluster_id = row[0]
        avg_emp = row[1]
        avg_pay_per_worker = row[2]
        print(f"Cluster: {cluster_id}, Avg Employment per ZIP: {avg_emp}, Avg Payroll per Worker: {avg_pay_per_worker}")

    close_connection(cur, conn)

def main():
    conn = connect_to_db()
    if conn is None:
        print("Connection failed.")
        return

    workers_per_zip_code(conn)

    conn = connect_to_db()
    if conn is not None:
        cluster_distribution_by_zipcode(conn)

    conn = connect_to_db()
    if conn is not None:
        employment_and_payroll_by_cluster(conn)

if __name__ == "__main__":
    main()


