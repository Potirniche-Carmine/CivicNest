import numpy as np
from sklearn.cluster import KMeans
import fetch_location

# Fetch the latitude and longitude data using the function from main function
lat_long_list = fetch_location.get_location_data()

if lat_long_list is None:
    print("No data to cluster.")
    exit()

lat_long_array = np.array(lat_long_list)# Convert the list into a numpy array (required for scikit-learn)

k = 3  #Uisng 3 clusters as an example. SHOULD BE CHANGED, runtime for this algorithm is terrible
kmeans = KMeans(n_clusters=k, random_state=42)


kmeans.fit(lat_long_array) # Fit the KMeans model to the data

# Get the cluster labels (which cluster each point belongs to)
labels = kmeans.labels_

# Get the centroid of each cluster
centroids = kmeans.cluster_centers_

print("\nCluster centers (centroids):")
for idx, centroid in enumerate(centroids):
    print(f"Cluster {idx+1}: Latitude: {centroid[0]}, Longitude: {centroid[1]}")

print("\nLocation clusters:")
for i, label in enumerate(labels):
    print(f"Location {lat_long_list[i]} is in Cluster {label+1}")

