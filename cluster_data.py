import numpy as np
from sklearn.cluster import KMeans

def cluster_data(data, k):
    if data is None or len(data) == 0:
        raise ValueError("No data to cluster.")

    data_array = np.array(data) # Convert the data to a numpy array

    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(data_array)
    
    return kmeans.labels_, kmeans.cluster_centers_

