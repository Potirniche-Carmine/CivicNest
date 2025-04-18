from db_connection import connect_to_db, close_connection
from collections import defaultdict
import pandas as pd

def display_cluster_distribution_by_zip(cursor):
    query = """
    SELECT h.zipcode, ct.cluster_id, COUNT(*) AS num_homes,
    ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (PARTITION BY h.zipcode), 2) AS percentage
    FROM houses h
    JOIN cluster_table ct ON h.zpid = ct.zpid
    GROUP BY h.zipcode, ct.cluster_id
    ORDER BY h.zipcode, ct.cluster_id
    """
    cursor.execute(query)
    for zipcode, cluster_id, home_count, percentage in cursor.fetchall():
        print(f"ZIP: {zipcode} | Cluster {cluster_id}: {home_count} homes ({percentage}%)")

def fetch_employment_growth_by_cluster(cursor):
    query = """
    SELECT ct.cluster_id, ROUND(AVG(ep.percent_change)::numeric, 2)
    FROM cluster_table ct
    JOIN houses h ON ct.zpid = h.zpid
    JOIN employment_prediction ep ON h.zipcode = ep.zipcode::TEXT
    GROUP BY ct.cluster_id
    ORDER BY ct.cluster_id
    """
    cursor.execute(query)
    return dict(cursor.fetchall())

def calculate_weighted_cluster_averages(cursor):
    query = """
    WITH house_counts AS (
        SELECT ct.cluster_id, h.zipcode, COUNT(*) AS home_count
        FROM cluster_table ct
        JOIN houses h ON ct.zpid = h.zpid
        GROUP BY ct.cluster_id, h.zipcode
    ),
    zip_metrics AS (
        SELECT ea.zipcode,
            AVG(ea.avg_annual_payroll / NULLIF(ea.avg_employment, 0)) AS payroll_per_worker,
            AVG(h.price) AS average_price
        FROM employment_averages ea
        JOIN houses h ON h.zipcode = ea.zipcode::TEXT
        GROUP BY ea.zipcode
    ),
    weighted_data AS (
        SELECT hc.cluster_id, hc.home_count, zm.payroll_per_worker, zm.average_price,
               hc.home_count * zm.payroll_per_worker AS weighted_payroll,
               hc.home_count * zm.average_price AS weighted_price
        FROM house_counts hc
        JOIN zip_metrics zm ON hc.zipcode::INT = zm.zipcode
    )
    SELECT cluster_id,
           ROUND((SUM(weighted_payroll) / NULLIF(SUM(home_count), 0))::numeric, 2) AS avg_payroll,
           ROUND((SUM(weighted_price) / NULLIF(SUM(home_count), 0))::numeric, 2) AS avg_price,
           ROUND((SUM(weighted_payroll) / NULLIF(SUM(weighted_price), 0))::numeric, 4) AS affordability_ratio
    FROM weighted_data
    GROUP BY cluster_id
    ORDER BY cluster_id
    """
    cursor.execute(query)
    return cursor.fetchall()

def calculate_price_distribution_stats(cursor):
    cursor.execute("""
    SELECT ct.cluster_id, h.price
    FROM cluster_table ct
    JOIN houses h ON ct.zpid = h.zpid
    WHERE h.price IS NOT NULL
    """)
    price_data_by_cluster = defaultdict(list)
    for cluster_id, price in cursor.fetchall():
        price_data_by_cluster[cluster_id].append(float(price))
    
    stats_by_cluster = {}
    for cluster_id, prices in price_data_by_cluster.items():
        series = pd.Series(prices)
        median_price = round(series.median(), 2)
        iqr = round(series.quantile(0.75) - series.quantile(0.25), 2)
        total_range = round(max(prices) - min(prices), 2)
        stats_by_cluster[cluster_id] = (median_price, iqr, total_range)
        print(f"Cluster {cluster_id} | Median: ${median_price}, IQR: ${iqr}, Range: ${total_range}")
    return stats_by_cluster

def update_insights_table(cursor, connection, insight_data):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS insights_table (
        cluster_id INTEGER PRIMARY KEY,
        median_price NUMERIC,
        avg_payroll NUMERIC,
        affordability_ratio NUMERIC,
        employment_growth NUMERIC,
        iqr_price NUMERIC,
        total_range NUMERIC
    )
    """)
    cursor.execute("DELETE FROM insights_table")

    insert_query = """
    INSERT INTO insights_table (
        cluster_id, median_price, avg_payroll,
        affordability_ratio, employment_growth, iqr_price, total_range
    ) VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    for row in insight_data:
        cursor.execute(insert_query, row)

    connection.commit()
    print("insights_table updated.")

def better_predictions():
    connection = connect_to_db()
    if not connection:
        print("Failed to connect to the database.")
        return

    cursor = connection.cursor()

    display_cluster_distribution_by_zip(cursor)
    employment_growth = fetch_employment_growth_by_cluster(cursor)
    weighted_averages = calculate_weighted_cluster_averages(cursor)
    price_stats = calculate_price_distribution_stats(cursor)

    combined_insights = []
    for cluster_id, avg_payroll, avg_price, ratio in weighted_averages:
        median_price, iqr, price_range = price_stats.get(cluster_id, (None, None, None))
        growth = employment_growth.get(cluster_id)
        combined_insights.append((
            cluster_id,
            median_price,
            avg_payroll,
            ratio,
            growth,
            iqr,
            price_range
        ))

    update_insights_table(cursor, connection, combined_insights)
    close_connection(cursor, connection)

if __name__ == "__main__": # This is in case I don't want to run from main
    better_predictions()

