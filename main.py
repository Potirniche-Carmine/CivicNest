from location_data import fetch_location_data, store_cluster_centroids as store_location_centroids
from cluster_data import cluster_data
from price_data import fetch_price_data, store_cluster_centroids as store_price_centroids
import numpy as np  # Import numpy to reshape the array

# Fetch the location data
lat_long_list = fetch_location_data()
if lat_long_list is None:
    print("No location data to cluster.")
else:
    try:
        lat_long_array = np.array(lat_long_list)  # Convert to numpy array
        labels, centroids = cluster_data(lat_long_array, k=50)
        
        #print("\nCluster centers (centroids) for location data:")
        #for idx, centroid in enumerate(centroids):
            #print(f"Cluster {idx + 1}: Latitude: {centroid[0]}, Longitude: {centroid[1]}")

        #print("\nLocation clusters:")
        #for i, label in enumerate(labels):
        #   print(f"Location {lat_long_list[i]} is in Cluster {label + 1}")

        store_location_centroids(centroids)

    except ValueError as e:
        print(f"Error while clustering location data: {e}")

# Fetch the price data
price_list = fetch_price_data()
if price_list is None:
    print("No price data to cluster.")
else:
    try:
        # Reshape the price data to be a 2D array (n_samples, 1)
        price_array = np.array(price_list).reshape(-1, 1)  # Reshape to (n_samples, 1) for single feature (this sucked)
        
        labels, centroids = cluster_data(price_array, k=3)

        #print("\nCluster centers (centroids) for price data:")
        #for idx, centroid in enumerate(centroids):
        #    print(f"Cluster {idx + 1}: Price: {centroid[0]}")

        #print("\nPrice clusters:")
        #for i, label in enumerate(labels):
        #    print(f"Price {price_list[i]} is in Cluster {label + 1}")

        store_price_centroids(centroids)

    except ValueError as e:
        print(f"Error while clustering price data: {e}")




