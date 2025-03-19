import pandas as pd
from house_data import fetch_price_data
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

prices = fetch_price_data()
if prices is None:
    print("No location data to cluster.")
else:
        price_df = pd.DataFrame(prices, columns=["price"])
        
        # elbow method to find optimal k
        sse = {}
        for k in range (1, 40):
            kmeans = KMeans(n_clusters=k, max_iter=1000).fit(price_df)
            price_df["clusters"] = kmeans.labels_
            sse[k] = kmeans.inertia_
        
        # plotting it
        plt.figure()
        plt.plot(list(sse.keys()), list(sse.values()))
        plt.xlabel('Number of cluster')
        plt.ylabel('SSE')
        plt.title('The Elbow Method showing the optimal k')
        plt.show()
