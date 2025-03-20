"use client";

import React, { useEffect, useRef, useState } from "react";
import mapboxgl from 'mapbox-gl';
import { useTheme } from "next-themes";
import { X } from 'lucide-react';
import ReactDOM from 'react-dom/client';
import HouseSelect, { houses } from './house_select';
import { Skeleton } from "@/app/components/ui/skeleton";

mapboxgl.accessToken = process.env.NEXT_PUBLIC_MAPBOX_ACCESS_TOKEN || "";

const DEFAULT_ZOOM = 11;
const DEFAULT_CENTER: [number, number] = [-119.8143, 39.5299];

const generateClusterColors = (numClusters: number) => {
    const goldenRatio = 0.618033988749895;
    const colors = [];
    let hue = Math.random();
    
    for (let i = 0; i < numClusters; i++) {
        hue += goldenRatio;
        hue %= 1;
        
        const h = hue * 360;
        const s = 0.7;
        const v = 0.9;
        
        const hi = Math.floor(h / 60) % 6;
        const f = h / 60 - Math.floor(h / 60);
        const p = v * (1 - s);
        const q = v * (1 - f * s);
        const t = v * (1 - (1 - f) * s);
        
        let r, g, b;
        if (hi === 0) [r, g, b] = [v, t, p];
        else if (hi === 1) [r, g, b] = [q, v, p];
        else if (hi === 2) [r, g, b] = [p, v, t];
        else if (hi === 3) [r, g, b] = [p, q, v];
        else if (hi === 4) [r, g, b] = [t, p, v];
        else [r, g, b] = [v, p, q];
        
        const rgb = `rgb(${Math.floor(r * 255)}, ${Math.floor(g * 255)}, ${Math.floor(b * 255)})`;
        colors.push(rgb);
    }
    
    return colors;
};

export function Map() {
    const mapRef = useRef<HTMLDivElement>(null);
    const mapInstanceRef = useRef<mapboxgl.Map | null>(null);
    const activePopupRef = useRef<mapboxgl.Popup | null>(null);
    const [houses, setHouses] = useState<houses[]>([]);
    const [clusters, setClusters] = useState<any[]>([]);
    const [clusterColors, setClusterColors] = useState<string[]>([]);
    const [, setSelectedHouse] = useState<houses | null>(null);
    const [selectedClusterId, setSelectedClusterId] = useState<number | null>(null);
    const [isLoading, setIsLoading] = useState(true);
    const { theme, systemTheme } = useTheme();

    const isDarkMode = theme === "system" 
        ? systemTheme === "dark"
        : theme === "dark";

    const resetMapView = () => {
        if (mapInstanceRef.current) {
            mapInstanceRef.current.flyTo({
                center: DEFAULT_CENTER,
                zoom: DEFAULT_ZOOM,
                essential: true
            });
            setSelectedClusterId(null);
            updateHouseOpacity(null);
            if (activePopupRef.current) {
                activePopupRef.current.remove();
            }
        }
    }

    useEffect(() => {
        const fetchData = async () => {
            setIsLoading(true);
            try {
                const locationResponse = await fetch('/api/locations');
                const locationData = await locationResponse.json();
                setHouses(locationData.houses || []);
                
                const clusterResponse = await fetch('/api/clusters');
                const clusterData = await clusterResponse.json();
                
                const clustersArray = clusterData.clusters || [];
                setClusters(clustersArray);
                
                if (clustersArray.length > 0) {
                    const colors = generateClusterColors(clustersArray.length);
                    setClusterColors(colors);
                }
            } catch (error) {
                console.error('Error fetching data:', error);
                setHouses([]);
                setClusters([]);
                setClusterColors([]);
            } finally {
                setIsLoading(false);
            }
        };

        fetchData();
    }, []);

    const housesWithClusterInfo = houses.map(house => {
        const houseCluster = clusters.find(cluster => 
            cluster.houses.some((h: any) => h.zpid === house.zpid)
        );
        
        const houseInCluster = houseCluster ? 
            houseCluster.houses.find((h: any) => h.zpid === house.zpid) : 
            null;
        
        const clusterIndex = houseCluster ? clusters.indexOf(houseCluster) : -1;
        const clusterColor = clusterIndex >= 0 ? clusterColors[clusterIndex] : isDarkMode ? "#f56565" : "#e53e3e";
        
        return {
            ...house,
            bathrooms: houseInCluster?.bathrooms || house.bathrooms,
            bedrooms: houseInCluster?.bedrooms || house.bedrooms,
            cluster_id: houseCluster?.cluster_id || null,
            cluster_avg_price: houseCluster?.avg_price || null,
            color: clusterColor
        };
    });

    const housesGeoJSON = {
        type: "FeatureCollection",
        features: housesWithClusterInfo.map(house => ({
            type: "Feature",
            properties: { 
                id: house.zpid, 
                address: house.address,
                price: house.price,
                cluster_id: house.cluster_id,
                bathrooms: house.bathrooms,
                bedrooms: house.bedrooms,
                cluster_avg_price: house.cluster_avg_price,
                color: house.color
            },
            geometry: {
                type: "Point",
                coordinates: [house.long, house.lat]
            }
        }))
    } as GeoJSON.FeatureCollection<GeoJSON.Point>;

    const updateHouseOpacity = (clusterId: number | null) => {
        if (!mapInstanceRef.current) return;

        if (mapInstanceRef.current.getLayer('houses-layer')) {
            if (clusterId === null) {
                mapInstanceRef.current.setPaintProperty('houses-layer', 'circle-opacity', 1);
                mapInstanceRef.current.setPaintProperty('houses-layer', 'circle-radius', 4);
            } else {
                mapInstanceRef.current.setPaintProperty(
                    'houses-layer',
                    'circle-opacity',
                    ['case', ['==', ['get', 'cluster_id'], clusterId], 1, 0.05]
                );
                
                mapInstanceRef.current.setPaintProperty(
                    'houses-layer',
                    'circle-radius',
                    ['case', ['==', ['get', 'cluster_id'], clusterId], 7, 4]
                );
            }
        }
    };

    const createCustomPopup = (coordinates: [number, number], properties: any) => {
        if (!mapInstanceRef.current) return;
        if (activePopupRef.current) {
            activePopupRef.current.remove();
        }
        
        const formattedPrice = new Intl.NumberFormat('en-US', {
            style: 'currency',
            currency: 'USD',
            minimumFractionDigits: 0
        }).format(properties.price);
        
        const formattedClusterAvgPrice = new Intl.NumberFormat('en-US', {
            style: 'currency',
            currency: 'USD',
            minimumFractionDigits: 0
        }).format(properties.cluster_avg_price);
        
        const popupContainer = document.createElement('div');
        popupContainer.className = `popup-container ${isDarkMode ? 'dark-popup' : 'light-popup'}`;
        
        const popupContent = document.createElement('div');
        popupContent.className = 'popup-content';
        popupContent.style.position = 'relative';
        popupContent.style.padding = '16px';
        popupContent.style.borderRadius = '8px';
        popupContent.style.minWidth = '250px';
        popupContent.style.backgroundColor = isDarkMode ? '#2b1f66' : '#d5ccff';
        popupContent.style.color = isDarkMode ? '#f3f4f6' : '#111827';
        popupContent.style.boxShadow = '0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)';
        
        const addressElement = document.createElement('h3');
        addressElement.innerText = properties.address;
        addressElement.style.fontWeight = 'bold';
        addressElement.style.marginBottom = '8px';
        addressElement.style.paddingRight = '24px';
        
        const priceElement = document.createElement('p');
        priceElement.innerText = `Price: ${formattedPrice}`;
        priceElement.style.marginBottom = '8px';

        const bedroomElement = document.createElement('p');
        bedroomElement.innerText = `Bedrooms: ${properties.bedrooms}`;
        bedroomElement.style.marginBottom = '8px';
        
        const bathroomElement = document.createElement('p');
        bathroomElement.innerText = `Bathrooms: ${properties.bathrooms}`;
        bathroomElement.style.marginBottom = '8px';

        const divider = document.createElement('div');
        divider.style.height = '1px';
        divider.style.backgroundColor = isDarkMode ? '#374151' : '#e5e7eb';
        divider.style.margin = '8px 0';
        
        const clusterAvgPrice = document.createElement('p');
        clusterAvgPrice.innerText = `Cluster Average: ${formattedClusterAvgPrice}`;
        
        const closeButtonContainer = document.createElement('div');
        closeButtonContainer.className = 'close-button-container';
        closeButtonContainer.style.position = 'absolute';
        closeButtonContainer.style.top = '16px';
        closeButtonContainer.style.right = '10px';
        closeButtonContainer.style.cursor = 'pointer';
        
        popupContent.appendChild(addressElement);
        popupContent.appendChild(priceElement);
        popupContent.appendChild(bedroomElement);
        popupContent.appendChild(bathroomElement);
        popupContent.appendChild(divider);
        popupContent.appendChild(clusterAvgPrice);
        popupContent.appendChild(closeButtonContainer);
        popupContainer.appendChild(popupContent);
        
        const popup = new mapboxgl.Popup({
            closeButton: false,
            closeOnClick: false,
            maxWidth: '300px',
            className: 'custom-mapbox-popup'
        })
            .setLngLat(coordinates)
            .setDOMContent(popupContainer)
            .addTo(mapInstanceRef.current);
        
        // Render using REACTDOM the lucidereact X icon
        const root = ReactDOM.createRoot(closeButtonContainer);
        root.render(
            <X 
                size={20} 
                onClick={() => {
                    popup.remove();
                }} 
                color={isDarkMode ? '#e5e7eb' : '#4b5563'} 
                style={{
                    cursor: 'pointer',
                    padding: '2px',
                    borderRadius: '4px',
                    backgroundColor: isDarkMode ? 'rgba(255,255,255,0.1)' : 'rgba(0,0,0,0.05)'
                }}
            />
        );
        
        activePopupRef.current = popup;
        
        setSelectedClusterId(properties.cluster_id);
        updateHouseOpacity(properties.cluster_id);
        
        return popup;
    };

    const handleHouseSelect = (house: houses) => {
        setSelectedHouse(house);
        
        const houseWithCluster = housesWithClusterInfo.find(h => h.zpid === house.zpid);
        
        if (mapInstanceRef.current && houseWithCluster) {
            mapInstanceRef.current.flyTo({
                center: [houseWithCluster.long, houseWithCluster.lat],
                zoom: 15,
                essential: true
            });
            
            setTimeout(() => {
                const properties = {
                    address: houseWithCluster.address,
                    price: houseWithCluster.price,
                    bedrooms: houseWithCluster.bedrooms,
                    bathrooms: houseWithCluster.bathrooms,
                    cluster_id: houseWithCluster.cluster_id,
                    cluster_avg_price: houseWithCluster.cluster_avg_price
                };
                
                createCustomPopup([houseWithCluster.long, houseWithCluster.lat], properties);
            }, 1000);
        }
    };

    useEffect(() => {
        if (!mapRef.current) return;

        const initializeMap = () => {
            if (!mapInstanceRef.current) {
                mapInstanceRef.current = new mapboxgl.Map({
                    container: mapRef.current as HTMLElement,
                    style: isDarkMode
                        ? "mapbox://styles/mapbox/dark-v11"
                        : "mapbox://styles/mapbox/light-v11",
                    center: DEFAULT_CENTER,
                    zoom: DEFAULT_ZOOM,
                });

                mapInstanceRef.current.on('load', () => {
                    if (!mapInstanceRef.current) return;

                    const style = document.createElement('style');
                    style.textContent = `
                        .custom-mapbox-popup .mapboxgl-popup-content {
                            padding: 0;
                            overflow: visible;
                            background: transparent;
                            border-radius: 8px;
                            box-shadow: none;
                        }
                        .custom-mapbox-popup .mapboxgl-popup-tip {
                            border-top-color: ${isDarkMode ? '#01368a' : '#4287f5'};
                        }
                    `;
                    document.head.appendChild(style);

                    mapInstanceRef.current.addSource('houses', {
                        type: 'geojson',
                        data: housesGeoJSON,
                    });

                    mapInstanceRef.current.addLayer({
                        id: 'houses-layer',
                        type: 'circle',
                        source: 'houses',
                        paint: {
                            'circle-radius': 4,
                            'circle-color': ['get', 'color'],
                            'circle-stroke-width': 1,
                            'circle-stroke-color': isDarkMode ? '#ffffff' : '#000000',
                        },
                    });

                    // Add popup on house click
                    mapInstanceRef.current.on('click', 'houses-layer', (e) => {
                        if (e.features && e.features[0] && e.features[0].properties) {
                            const coordinates = (e.features[0].geometry as GeoJSON.Point).coordinates.slice();
                            const props = e.features[0].properties;
                            
                            createCustomPopup(
                                coordinates as [number, number], 
                                props
                            );
                        }
                    });

                    mapInstanceRef.current.on('mouseenter', 'houses-layer', () => {
                        if (mapInstanceRef.current) {
                            mapInstanceRef.current.getCanvas().style.cursor = 'pointer';
                        }
                    });

                    mapInstanceRef.current.on('mouseleave', 'houses-layer', () => {
                        if (mapInstanceRef.current) {
                            mapInstanceRef.current.getCanvas().style.cursor = '';
                        }
                    });
                });
            } else {
                mapInstanceRef.current.setStyle(
                    isDarkMode
                        ? "mapbox://styles/mapbox/dark-v11"
                        : "mapbox://styles/mapbox/light-v11"
                );

                mapInstanceRef.current.once('style.load', () => {
                    if (!mapInstanceRef.current) return;

                    if (!mapInstanceRef.current.getSource('houses')) {
                        mapInstanceRef.current.addSource('houses', {
                            type: 'geojson',
                            data: housesGeoJSON,
                        });

                        mapInstanceRef.current.addLayer({
                            id: 'houses-layer',
                            type: 'circle',
                            source: 'houses',
                            paint: {
                                'circle-radius': 4,
                                'circle-color': ['get', 'color'],
                                'circle-stroke-width': 1,
                                'circle-stroke-color': isDarkMode ? '#ffffff' : '#000000',
                            },
                        });
                    } else {
                        (mapInstanceRef.current.getSource('houses') as mapboxgl.GeoJSONSource)
                            .setData(housesGeoJSON);
                    }
                    if (selectedClusterId !== null) {
                        updateHouseOpacity(selectedClusterId);
                    }
                });
            }
        };

        initializeMap();

        return () => {
            // Clean up any active popups
            if (activePopupRef.current) {
                activePopupRef.current.remove();
                activePopupRef.current = null;
            }
            
            mapInstanceRef.current?.remove();
            mapInstanceRef.current = null;
        };
    }, [isDarkMode, houses, clusters, clusterColors]);

    useEffect(() => {
        if (mapInstanceRef.current && mapInstanceRef.current.getSource('houses')) {
            (mapInstanceRef.current.getSource('houses') as mapboxgl.GeoJSONSource)
                .setData(housesGeoJSON);
                
            if (selectedClusterId !== null) {
                updateHouseOpacity(selectedClusterId);
            }
        }
    }, [houses, clusters, clusterColors]);

    if (isLoading) {
        return (
            <div className="space-y-4">
                <div className="w-full">
                    <Skeleton className="h-10 max-w-md rounded-md" />
                </div>
                <Skeleton className="w-full h-[700px] rounded-lg" />
            </div>
        );
    }

    return (
        <div className="space-y-4">
            <div className="w-full flex justify-between items-center">
                <HouseSelect onSelect={handleHouseSelect} />
                {selectedClusterId && (
                    <button 
                        onClick={resetMapView}
                        className="px-4 py-2 bg-primary text-primary-foreground rounded-md hover:bg-primary/90 transition-colors"
                    >
                        Reset View
                    </button>
                )}
            </div>
            <div className="w-full h-[700px] rounded-lg overflow-hidden border border-border" ref={mapRef} />
        </div>
    );
}