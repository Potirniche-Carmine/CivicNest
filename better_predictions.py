from db_connection import connect_to_db, close_connection

#######Util Functions
def format_val(val, as_currency=False):
    if val is None:
        return "N/A"
    return f"${val:.2f}" if as_currency else f"{val:.2f}"

#########Employment summary per ZIP code
def employment_stats_by_zip(conn, cur):
    query = """
    SELECT zipcode, year, employment, establishments, annual_payroll,
        CASE WHEN establishments > 0 THEN employment::FLOAT / establishments ELSE NULL END AS avg_workers,
        CASE WHEN establishments > 0 THEN annual_payroll::FLOAT / establishments ELSE NULL END AS payroll_per_establishment,
        CASE WHEN employment > 0 THEN annual_payroll::FLOAT / employment ELSE NULL END AS payroll_per_worker
    FROM employment;
    """
    cur.execute(query)
    rows = cur.fetchall()

    print("Employment Stats by ZIP Code:")
    for row in rows:
        zipc, yr, emp, est, payroll, workers_avg, payroll_est, payroll_worker = row
        print(f"ZIP: {zipc}, Year: {yr} → "
                f"Avg Workers/Business: {format_val(workers_avg)}, "
                f"Payroll/Business: {format_val(payroll_est, True)}, "
                f"Payroll/Worker: {format_val(payroll_worker, True)}")

#########Cluster distribution breakdown
def cluster_dist_by_zip(conn, cur):
    query = """
    SELECT 
        h.zipcode,
        ct.cluster_id,
        COUNT(*) AS house_count,
        ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (PARTITION BY h.zipcode), 2) AS pct_within_zip
    FROM houses h
    JOIN cluster_table ct ON h.zpid = ct.zpid
    GROUP BY h.zipcode, ct.cluster_id
    ORDER BY h.zipcode, ct.cluster_id;
    """
    cur.execute(query)
    data = cur.fetchall()

    print("\nCluster Breakdown by ZIP Code:")
    for zipc, cid, count, pct in data:
        print(f"ZIP: {zipc} → Cluster {cid}: {count} homes ({pct}%)")

#########Employment + Payroll by cluster
def employment_by_cluster(conn, cur):
    sql = """
    SELECT 
        ct.cluster_id,
        ROUND(AVG(ea.avg_employment)::numeric, 2),
        ROUND(AVG(CASE 
            WHEN ea.avg_employment > 0 THEN ea.avg_annual_payroll::FLOAT / ea.avg_employment
            ELSE NULL END)::numeric, 2)
    FROM cluster_table ct
    JOIN houses h ON ct.zpid = h.zpid
    JOIN employment_averages ea ON h.zipcode::INT = ea.zipcode
    GROUP BY ct.cluster_id
    ORDER BY ct.cluster_id;
    """
    cur.execute(sql)
    results = cur.fetchall()

    print("\nEmployment + Payroll per Worker by Cluster:")
    for cid, avg_emp, avg_ppw in results:
        print(f"Cluster {cid} → Avg Employment: {avg_emp}, Payroll/Worker: {format_val(avg_ppw, True)}")
    
    return results

########Payroll vs House Price Ratio
def payroll_price_ratio(conn, cur):
    query = """
    SELECT 
        ct.cluster_id,
        ROUND(AVG(ea.avg_annual_payroll::FLOAT / NULLIF(ea.avg_employment, 0))::numeric, 2) AS payroll_per_worker,
        ROUND(AVG(h.price)::numeric, 2) AS avg_price,
        ROUND((AVG(ea.avg_annual_payroll::FLOAT / NULLIF(ea.avg_employment, 0)) / NULLIF(AVG(h.price), 0))::numeric, 4) AS ratio
    FROM cluster_table ct
    JOIN houses h ON ct.zpid = h.zpid
    JOIN employment_averages ea ON h.zipcode::INT = ea.zipcode
    GROUP BY ct.cluster_id
    ORDER BY ct.cluster_id;
    """
    cur.execute(query)
    rows = cur.fetchall()

    print("\nPayroll to House Price Ratio:")
    for cid, pay_worker, price, ratio in rows:
        print(f"Cluster {cid}: Payroll/Worker = {format_val(pay_worker, True)}, "
                f"House Price = {format_val(price, True)}, Ratio = {ratio}")
    return rows

# ####### Employment Growth Predictions
def predicted_growth(conn, cur):
    query = """
    SELECT 
        ct.cluster_id,
        ROUND(AVG(ep.percent_change)::numeric, 2)
    FROM cluster_table ct
    JOIN houses h ON ct.zpid = h.zpid
    JOIN employment_prediction ep ON h.zipcode = ep.zipcode::TEXT
    GROUP BY ct.cluster_id
    ORDER BY ct.cluster_id;
    """
    cur.execute(query)
    data = cur.fetchall()

    print("\nPredicted Employment Growth:")
    for cid, growth in data:
        print(f"Cluster {cid}: +{growth}%")

    return data

########Growth vs Payroll vs Price
def growth_vs_others(conn, cur):
    query = """
    SELECT 
        ct.cluster_id,
        ROUND(AVG(ep.percent_change)::numeric, 2),
        ROUND(AVG(ea.avg_annual_payroll)::numeric, 2),
        ROUND(AVG(cc.price)::numeric, 2)
    FROM cluster_table ct
    JOIN houses h ON ct.zpid = h.zpid
    JOIN employment_prediction ep ON h.zipcode = ep.zipcode::TEXT
    JOIN employment_averages ea ON h.zipcode = ea.zipcode::TEXT
    JOIN cluster_centroids cc ON ct.cluster_id = cc.cluster_id
    GROUP BY ct.cluster_id
    ORDER BY ct.cluster_id;
    """
    cur.execute(query)
    data = cur.fetchall()

    print("\nGrowth vs Payroll vs Price:")
    for cid, growth, payroll, price in data:
        print(f"Cluster {cid}: Growth={growth}%, Payroll={format_val(payroll, True)}, Price={format_val(price, True)}")


def update_insights(conn, cur, cluster_vals):
    #Just in case we need to add another value
    # cur.execute("""
    #     ALTER TABLE insights_table
    #     ADD COLUMN IF NOT EXISTS employment_growth NUMERIC;
    # """)
    
    cur.execute("""
    CREATE TABLE IF NOT EXISTS insights_table (
        cluster_id INTEGER PRIMARY KEY,
        avg_payroll NUMERIC,
        avg_price NUMERIC,
        affordability_ratio NUMERIC,
        employment_growth NUMERIC
    );
    """)

    cur.execute("DELETE FROM insights_table;")

    for cid, payroll, price, ratio, growth in cluster_vals:
        cur.execute("""
            INSERT INTO insights_table (cluster_id, avg_payroll, avg_price, affordability_ratio, employment_growth)
            VALUES (%s, %s, %s, %s, %s)
        """, (cid, payroll, price, ratio, growth))

    conn.commit()
    print("insights_table updated.")


def better_predictions():
    conn = connect_to_db()
    if not conn:
        print("[ERROR] DB connection failed.")
        return

    cur = conn.cursor()

    employment_stats_by_zip(conn, cur)
    cluster_dist_by_zip(conn, cur)
    employment_by_cluster(conn, cur)
    ratio_data = payroll_price_ratio(conn, cur)
    predicted_growth_data = predicted_growth(conn, cur)
    growth_vs_others(conn, cur)

    combined = [r + (g[1],) for r, g in zip(ratio_data, predicted_growth_data)]
    update_insights(conn, cur, combined)

    close_connection(cur, conn)


if __name__ == "__main__":
    better_predictions()
