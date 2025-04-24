from db_connection import connect_to_db
from collections import defaultdict
import statistics
import math
from decimal import Decimal

def compute_stats(conn):
    cur = conn.cursor()
    cur.execute("SELECT zipcode, price FROM houses WHERE price IS NOT NULL;")
    rows = cur.fetchall()
    cur.close()
    d = defaultdict(list)
    for z, p in rows:
        d[z].append(p)
    stats = {}
    for z, prices in d.items():
        med = statistics.median(prices)
        sd = statistics.pstdev(prices) if len(prices) > 1 else 0
        stats[z] = (med, sd)
    return stats

def update_table(conn, stats):
    cur = conn.cursor()
    cur.execute("ALTER TABLE final_insights_table ADD COLUMN IF NOT EXISTS standard_deviation_price NUMERIC;")
    cur.execute("ALTER TABLE final_insights_table ADD COLUMN IF NOT EXISTS affordability_ratio NUMERIC;")
    cur.execute("UPDATE final_insights_table SET median_price = NULL, standard_deviation_price = NULL, affordability_ratio = NULL;")
    for z, (med, sd) in stats.items():
        med_val = Decimal(med).quantize(Decimal('0.01'))
        sd_val = Decimal('0') if sd == 0 else Decimal(sd).quantize(Decimal('0.01'))
        cur.execute(
            "UPDATE final_insights_table SET median_price = %s, standard_deviation_price = %s WHERE zipcode = %s;",
            (med_val, sd_val, z)
        )
    cur.execute("""
        UPDATE final_insights_table
        SET affordability_ratio = ROUND(
            CASE WHEN median_price <> 0 
                 THEN avg_payroll / median_price 
                 ELSE NULL 
            END
        ::numeric, 2);
    """)
    conn.commit()
    cur.close()

def zip_predictions():
    conn = connect_to_db()
    if not conn:
        return
    stats = compute_stats(conn)
    update_table(conn, stats)
    conn.close()

if __name__ == "__main__":
    zip_predictions()








