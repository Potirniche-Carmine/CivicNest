from db_connection import connect_to_db, close_connection

def make_schema(c):
    c.execute("""
        CREATE TABLE IF NOT EXISTS final_insights_table (
            zipcode           INTEGER PRIMARY KEY,
            pct_cluster_1     NUMERIC,
            pct_cluster_2     NUMERIC,
            pct_cluster_3     NUMERIC,
            pct_cluster_4     NUMERIC,
            assigned_cluster  INTEGER,
            avg_payroll       NUMERIC,
            affordability_ratio NUMERIC,
            employment_growth NUMERIC
        );
    """)

def truncate_table(c):
    c.execute("TRUNCATE TABLE final_insights_table;")

def populate_table(c):
    c.execute("""
        WITH cluster_zip_counts AS (
            SELECT h.zipcode::INT AS zipcode, ct.cluster_id, COUNT(*) AS house_count
            FROM houses h
            JOIN cluster_table ct ON h.zpid = ct.zpid
            GROUP BY h.zipcode::INT, ct.cluster_id
        ),
        total_zip_counts AS (
            SELECT zipcode, SUM(house_count) AS total
            FROM cluster_zip_counts
            GROUP BY zipcode
        ),
        percentages AS (
            SELECT c.zipcode,
                   c.cluster_id,
                   ROUND(100.0 * c.house_count / t.total, 1) AS pct
            FROM cluster_zip_counts c
            JOIN total_zip_counts t USING (zipcode)
        ),
        pivoted AS (
            SELECT zipcode,
                   MAX(CASE WHEN cluster_id = 1 THEN pct ELSE 0 END) AS pct1,
                   MAX(CASE WHEN cluster_id = 2 THEN pct ELSE 0 END) AS pct2,
                   MAX(CASE WHEN cluster_id = 3 THEN pct ELSE 0 END) AS pct3,
                   MAX(CASE WHEN cluster_id = 4 THEN pct ELSE 0 END) AS pct4
            FROM percentages
            GROUP BY zipcode
        ),
        with_cluster AS (
            SELECT *,
                   CASE
                       WHEN pct1 >= GREATEST(pct2, pct3, pct4) THEN 1
                       WHEN pct2 >= GREATEST(pct1, pct3, pct4) THEN 2
                       WHEN pct3 >= GREATEST(pct1, pct2, pct4) THEN 3
                       ELSE 4
                   END AS cluster_id
            FROM pivoted
        )
        INSERT INTO final_insights_table
            (zipcode,
             pct_cluster_1, pct_cluster_2, pct_cluster_3, pct_cluster_4,
             assigned_cluster, avg_payroll, affordability_ratio, employment_growth)
        SELECT
            w.zipcode, w.pct1, w.pct2, w.pct3, w.pct4, w.cluster_id,
            i.avg_payroll, i.affordability_ratio, i.employment_growth
        FROM with_cluster w
        JOIN insights_table i ON i.cluster_id = w.cluster_id;
    """)

def final_insights():
    conn = connect_to_db()
    if not conn:
        return
    cur = conn.cursor()
    make_schema(cur)
    truncate_table(cur)
    populate_table(cur)
    conn.commit()
    close_connection(conn, cur)

if __name__ == "__main__":
    final_insights()