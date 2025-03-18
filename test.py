import unittest
from unittest.mock import patch
import numpy as np
from cluster_data import KMeans

class TestClusterData(unittest.TestCase):
    @patch('fetch_location.get_location_data')# Mock fetch_location.get_location_data to return sample data
    def test_location_clustering(self, mock_fetch_location):
        # Mocki data
        mock_fetch_location.return_value = [
            [39.5296, -119.8138],
            [39.5541, -119.7674],
            [39.4851, -119.7555],
            [39.5442, -119.7324],
            [39.5227, -119.7987],
            [39.5395, -119.7818]
        ]

        lat_long_list = mock_fetch_location.return_value
        is_Large_Enough = self.assertEqual(len(lat_long_list), 6)  # Check that there are 6 locations
        # if (is_Large_Enough == 0): # If there isn't enough data
        #     print("Not enough data!")
        #     exit()#Not needed because self.assertEqual does it for us

        lat_long_array = np.array(lat_long_list) # Numpy array conversion
        KMeans.fit(lat_long_array) #KMeans model

        self.assertEqual(KMeans.n_clusters, 3)

        centroids = KMeans.cluster_centers_
        self.assertEqual(len(centroids), 3) 

        # Print out the cluster centers for verification
        print("\nCluster centers (centroids):")
        for idx, centroid in enumerate(centroids):
            print(f"Cluster {idx+1}: Latitude: {centroid[0]}, Longitude: {centroid[1]}")

  ####### Verify that the clustering assigns correct labels
        labels = KMeans.labels_
        self.assertEqual(len(labels), 6)


        for label in labels:
            self.assertIn(label, range(3)) 

    # Test when fetch_location returns None
    @patch('fetch_location.get_location_data')
    def test_no_data(self, mock_fetch_location):
        mock_fetch_location.return_value = None
        lat_long_list = mock_fetch_location.return_value
        self.assertIsNone(lat_long_list)  # Assert that lat_long_list is None
        with self.assertRaises(SystemExit): # If there's no data, the program should exit
            KMeans.fit(lat_long_list)  # This line should exit if no data is found

if __name__ == '__main__':
    unittest.main()

