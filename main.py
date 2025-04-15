from collections import Counter
import numpy as np
from house_data import fetch_price_data, fetch_house_ids, fetch_house_zipcodes
from cluster_data import cluster_data
from regional_employment_trends import regional_employment_trends
from better_predictions import better_predictions

def main():
    # #House price clustering logic
    # price_list = fetch_price_data()
    # house_ids = fetch_house_ids() 
    # zipcodes = fetch_house_zipcodes()  # Fetch zip codes for houses

    # if price_list is None or house_ids is None or zipcodes is None:
    #     print("Missing house data to cluster.")
    # else:
    #     try:
    #         price_array = np.array(price_list).reshape(-1, 1)  # Reshape to (n_samples, 1) for single feature (price)
            
    #         labels, centroids = cluster_data(price_array, k=4)

    #         print("House Price Clustering Results:")
    #         for idx, centroid in enumerate(centroids):
    #             print(f"Cluster {idx + 1}: Price: {centroid[0]}")

    #         cluster_counts = {}
    #         for label in labels:
    #             cluster_counts[label + 1] = cluster_counts.get(label + 1, 0) + 1
            
    #         print("\nHouses per cluster:")
    #         for cluster_id, count in sorted(cluster_counts.items()):
    #             print(f"Cluster {cluster_id}: {count} houses")

    #         cluster_zipcodes = {}
    #         for i, label in enumerate(labels):
    #             cluster_zipcodes.setdefault(label, []).append(zipcodes[i])
            
    #         print("\nMost common zip code per house cluster:")
    #         for cluster_id, zipcodes_in_cluster in cluster_zipcodes.items():
    #             most_common_zip = Counter(zipcodes_in_cluster).most_common(1)[0][0]
    #             print(f"Cluster {cluster_id}: Most common zip code: {most_common_zip}")

    #     except ValueError as e:
    #         print(f"Error while clustering house data: {e}")

    # #Employment data clustering
    # # data = get_employment_data()

    # # if data is None or len(data) == 0:
    # #     print("Missing employment data to cluster.")
    # # else:
    # #     try:
    # #         zipcodes = [item[0] for item in data]
    # #         avg_annual_pay = np.array([item[1] for item in data]).reshape(-1, 1)  # Reshape to 2D array
            
    # #         labels, centroids = cluster_data(avg_annual_pay, k=4)
            
    # #         print("\nEmployment Data Clustering Results:")
    # #         for idx, centroid in enumerate(centroids):
    # #             print(f"Cluster {idx + 1}: Avg. Annual Pay: {centroid[0]}")

    # #         cluster_counts = {}
    # #         for label in labels:
    # #             cluster_counts[label + 1] = cluster_counts.get(label + 1, 0) + 1
            
    # #         print("\nZip codes per employment cluster:")
    # #         for cluster_id, count in sorted(cluster_counts.items()):
    # #             print(f"Cluster {cluster_id}: {count} zip codes")

    # #         cluster_zipcodes = {}
    # #         for i, label in enumerate(labels):
    # #             cluster_zipcodes.setdefault(label, []).append(zipcodes[i])
            
    # #         print("\nMost common zip code per employment cluster:")
    # #         for cluster_id, zipcodes_in_cluster in cluster_zipcodes.items():
    # #             most_common_zip = Counter(zipcodes_in_cluster).most_common(1)[0][0]
    # #             print(f"Cluster {cluster_id}: Most common zip code: {most_common_zip}")

    # #     except ValueError as e:
    # #         print(f"Error while clustering employment data: {e}")
    
    #regional_employment_trends()  # Call the regional employment trends function to run the analysis
    better_predictions()

if __name__ == "__main__":
    main()  # This will ensure the script runs when executing "python main.py"
