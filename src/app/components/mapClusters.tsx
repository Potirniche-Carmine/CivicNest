import { useEffect, useState } from 'react';
import { useTheme } from "next-themes";
import * as turf from '@turf/turf';

export interface Cluster {
  cluster_id: number;
  latitude: number;
  longitude: number;
}

export interface ClustersCollection {
  type: "FeatureCollection";
  features: any[];
}

export const useClusterCircles = (): { clustersGeoJSON: ClustersCollection | null, isLoading: boolean } => {
  const [clusters, setClusters] = useState<Cluster[]>([]);
  const [clustersGeoJSON, setClustersGeoJSON] = useState<ClustersCollection | null>(null);
  const [isLoading, setIsLoading] = useState<boolean>(true);
  
  const { theme, systemTheme } = useTheme();
  const isDarkMode = theme === "system" 
    ? systemTheme === "dark"
    : theme === "dark";

  useEffect(() => {
    const fetchClusters = async () => {
      setIsLoading(true);
      try {
        const response = await fetch('/api/clusters');
        
        if (!response.ok) {
          throw new Error(`API returned status: ${response.status}`);
        }
        
        const data = await response.json();
        
        if (data.cluster_table) {
          setClusters(data.cluster_table);
        }
      } catch (error) {
        console.error('Error fetching clusters:', error);
      } finally {
        setIsLoading(false);
      }
    };

    fetchClusters();
  }, []);

  useEffect(() => {
    if (clusters.length > 0) {
      const features = clusters.map(cluster => {
        const center = [cluster.longitude, cluster.latitude];
        
        const radius = 1; // 2 km radius
        
        // Golden ratio color distribution
        const colorHue = (cluster.cluster_id * 137.5) % 360;
        
        const circle = turf.circle(center, radius, {
          steps: 64,
          units: 'kilometers',
          properties: {
            cluster_id: cluster.cluster_id,
            color: isDarkMode 
              ? `hsla(${colorHue}, 70%, 60%, 0.6)` 
              : `hsla(${colorHue}, 70%, 40%, 0.5)`
          }
        });
        
        return circle;
      });
      
      setClustersGeoJSON({
        type: "FeatureCollection",
        features
      });
    }
  }, [clusters, isDarkMode]);

  return { clustersGeoJSON, isLoading };
};