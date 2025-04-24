import matplotlib.pyplot as plt
from db_connection import connect_to_db, close_connection
from collections import defaultdict

def plot_price_histograms_by_cluster():
    conn = connect_to_db()
    if not conn:
        print("[ERROR] Failed to connect to the database.")
        return
    
    cur = conn.cursor()

    # Get house prices and clusters
    cur.execute("""
        SELECT ct.cluster_id, h.price
        FROM cluster_table ct
        JOIN houses h ON ct.zpid = h.zpid
        WHERE h.price IS NOT NULL
        ORDER BY ct.cluster_id;
    """)
    rows = cur.fetchall()

    close_connection(cur, conn)

    # Group prices by cluster
    cluster_prices = defaultdict(list)
    for cluster_id, price in rows:
        cluster_prices[cluster_id].append(price)

    # Plot histogram per cluster
    for cluster_id, prices in cluster_prices.items():
        plt.figure(figsize=(8, 5))
        plt.hist(prices, bins=20, edgecolor='black', color='skyblue')
        plt.title(f"House Price Distribution - Cluster {cluster_id}")
        plt.xlabel("Price ($)")
        plt.ylabel("Frequency")
        plt.grid(True)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    plot_price_histograms_by_cluster()

