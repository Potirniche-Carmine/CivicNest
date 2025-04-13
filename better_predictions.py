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

    for r in results:
        zipc = r[0]
        year = r[1]
        emp = r[2]
        est = r[3]
        payroll = r[4]
        workers_per_est = r[5]
        payroll_per_est = r[6]
        payroll_per_worker = r[7]
        print(f"Zip: {zipc}, Year: {year}, Avg Workers per Business: {workers_per_est:.2f}, "
              f"Avg Payroll per Business: {payroll_per_est:.2f}, Avg Payroll per Worker: {payroll_per_worker:.2f}")

    close_connection(cur, conn)

def main():
    conn = connect_to_db()
    if conn is None:
        print("Connection failed.")
        return

    workers_per_zip_code(conn)

if __name__ == "__main__":
    main()
