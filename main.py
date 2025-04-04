# from house_data import fetch_price_data, store_cluster_centroids, store_house_cluster_assignments, fetch_house_ids
# from cluster_data import cluster_data
# import numpy as np 

# price_list = fetch_price_data()
# house_ids = fetch_house_ids() 

# if price_list is None or house_ids is None:
#     print("Missing data to cluster.")
# else:
#     try:
#         price_array = np.array(price_list).reshape(-1, 1)  # Reshape to (n_samples, 1) for single feature (this sucked)
        
#         labels, centroids = cluster_data(price_array, k=4)

#         #print("\nCluster centers (centroids) for price data:")
#         for idx, centroid in enumerate(centroids):
#             print(f"Cluster {idx + 1}: Price: {centroid[0]}")

#         print("\nPrice clusters:")
#         for i, label in enumerate(labels):
#            print(f"House ID: {house_ids[i]}, Price: ${price_list[i]} is in Cluster {label + 1}")
        
#         cluster_counts = {}
#         for label in labels:
#             cluster_counts[label + 1] = cluster_counts.get(label + 1, 0) + 1
        
#         print("\nHouses per cluster:")
#         for cluster_id, count in sorted(cluster_counts.items()):
#             print(f"Cluster {cluster_id}: {count} houses")

#         store_cluster_centroids(centroids)
#         store_house_cluster_assignments(house_ids, labels)

#     except ValueError as e:
#         print(f"Error while clustering price data: {e}")

from house_data import fetch_price_data, store_cluster_centroids, store_house_cluster_assignments, fetch_house_ids, fetch_house_zipcodes
from cluster_data import cluster_data
import numpy as np 
from collections import Counter

price_list = fetch_price_data()
house_ids = fetch_house_ids() 
zipcodes = fetch_house_zipcodes()  # Fetch zip codes

if price_list is None or house_ids is None or zipcodes is None:
    print("Missing data to cluster.")
else:
    try:
        price_array = np.array(price_list).reshape(-1, 1)  # Reshape to (n_samples, 1) for single feature (this sucked)
        
        labels, centroids = cluster_data(price_array, k=4)

        # Print centroids
        for idx, centroid in enumerate(centroids):
            print(f"Cluster {idx + 1}: Price: {centroid[0]}")

        cluster_counts = {}
        for label in labels:
            cluster_counts[label + 1] = cluster_counts.get(label + 1, 0) + 1
        
        print("\nHouses per cluster:")
        for cluster_id, count in sorted(cluster_counts.items()):
            print(f"Cluster {cluster_id}: {count} houses")

        # Find and print most common zip code per cluster
        cluster_zipcodes = {}
        for i, label in enumerate(labels):
            cluster_zipcodes.setdefault(label, []).append(zipcodes[i])
        
        print("\nMost common zip code per cluster:")
        for cluster_id, zipcodes_in_cluster in cluster_zipcodes.items():
            most_common_zip = Counter(zipcodes_in_cluster).most_common(1)[0][0]
            print(f"Cluster {cluster_id}: Most common zip code: {most_common_zip}")

        store_cluster_centroids(centroids)
        store_house_cluster_assignments(house_ids, labels)

    except ValueError as e:
        print(f"Error while clustering price data: {e}")
