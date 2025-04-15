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
    for row in results:
        zipc = row[0]
        cluster_id = row[1]
        count = row[2]
        percent = row[3]
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
    for row in results:
        cluster_id = row[0]
        avg_emp = row[1]
        avg_pay_per_worker = row[2]
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
    results = cur.fetchall()

    print("\nPayroll-to-House-Price Ratio by Cluster")
    for row in results:
        cluster_id = row[0]
        avg_pay_per_worker = row[1]
        avg_house_price = row[2]
        ratio = row[3]
        print(f"Cluster: {cluster_id}, Avg Payroll per Worker: ${avg_pay_per_worker}, "
              f"Avg House Price: ${avg_house_price}, Payroll-to-Price Ratio: {ratio}")

    

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
    #Gives us house's cluster id and zip code

    cur.execute(sql)
    results = cur.fetchall()

    print("\nProjected Employment Growth by Cluster")
    for row in results:
        cluster_id = row[0]
        avg_growth = row[1]
        print(f"Cluster {cluster_id}: Avg Employment Growth = {avg_growth}%")


#MODIFY THIS CODE SO THAT IT DISPLAYS THE AVG PAYROLL PER WORKER FROM ABOVE
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
    for row in results:
        cluster_id = row[0]
        avg_growth = row[1]
        avg_payroll = row[2]
        avg_price = row[3]

        print(f"Cluster {cluster_id}:")
        print(f"Avg Growth: {avg_growth}%")
        #print(f"Avg Salary for Resident: ${some_table_element}")
        print(f"Avg Payroll: ${avg_payroll}")
        print(f"Avg House Price: ${avg_price}\n")


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
        payroll_vs_price_ratio_by_cluster(conn, cur)
        predicted_employment_growth_by_cluster(conn, cur)
        growth_vs_payroll_and_price(conn, cur)
    
    close_connection(cur, conn)

if __name__ == "__main__":
    better_predictions()