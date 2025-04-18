import matplotlib.pyplot as plt
import pandas as pd
from db_connection import connect_to_db, close_connection

def plot_price_boxplots():
    conn = connect_to_db()
    if not conn:
        print("[ERROR] Failed to connect to DB.")
        return

    cur = conn.cursor()
    cur.execute("""
        SELECT ct.cluster_id, h.price
        FROM cluster_table ct
        JOIN houses h ON ct.zpid = h.zpid
        WHERE h.price IS NOT NULL
        ORDER BY ct.cluster_id;
    """)
    rows = cur.fetchall()
    close_connection(cur, conn)

    # Convert to DataFrame
    df = pd.DataFrame(rows, columns=["cluster_id", "price"])
    df["price"] = df["price"].astype(float)

    # Create boxplot
    plt.figure(figsize=(10, 6))
    df.boxplot(column="price", by="cluster_id", grid=True)
    plt.title("House Price Distribution by Cluster")
    plt.suptitle("")
    plt.xlabel("Cluster ID")
    plt.ylabel("Price ($)")
    plt.xticks(rotation=0)
    plt.tight_layout()
    plt.show()
plot_price_boxplots()