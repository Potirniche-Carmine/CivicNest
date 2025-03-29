"use client";

import React, { useEffect, useRef, useState } from "react";
import mapboxgl from 'mapbox-gl';
import { useTheme } from "next-themes";
import { X, Info, ArrowLeft } from 'lucide-react';
import ReactDOM from 'react-dom/client';
import HouseSelect from './house_select';
import { Skeleton } from "@/app/components/ui/skeleton";
import { 
  Tooltip, 
  TooltipContent, 
  TooltipProvider, 
  TooltipTrigger 
} from "@/app/components/ui/tooltip";
import { houses } from "@/lib/types";

mapboxgl.accessToken = process.env.NEXT_PUBLIC_MAPBOX_ACCESS_TOKEN || "";

const DEFAULT_ZOOM = 11;
const DEFAULT_CENTER: [number, number] = [-119.8143, 39.5299];

const generateClusterColors = () => {
    return [
        '#3366CC', // Blue
        '#DC3912', // Red
        '#FF9900', // Orange
        '#109618', // Green
        '#990099', // Purple
        '#0099C6', // Teal
        '#DD4477', // Pink
        '#66AA00', // Lime
        '#B82E2E', // Dark Red
        '#316395', // Dark Blue
        '#994499', // Dark Purple
        '#22AA99'  // Dark Teal
    ];
};

// Function to format price for display
const formatPrice = (price: number): string => {
    return new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD',
        minimumFractionDigits: 0,
        maximumFractionDigits: 0
    }).format(price);
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
    const [showAllClusters, setShowAllClusters] = useState(false);
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
            setShowAllClusters(false);
            updateHouseOpacity(null, false);
            if (activePopupRef.current) {
                activePopupRef.current.remove();
            }
        }
    }

    const toggleClusterVisibility = () => {
        setShowAllClusters(!showAllClusters);
        updateHouseOpacity(selectedClusterId, !showAllClusters);
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
                
                setClusterColors(generateClusterColors());
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
        const clusterColor = clusterIndex >= 0 ? clusterColors[clusterIndex % clusterColors.length] : isDarkMode ? "#f56565" : "#e53e3e";
        
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

    const updateHouseOpacity = (clusterId: number | null, showAll: boolean = false) => {
        if (!mapInstanceRef.current) return;

        if (mapInstanceRef.current.getLayer('houses-layer')) {
            if (clusterId === null || showAll) {
                const opacity = showAll ? 0.9 : 0.4;
                mapInstanceRef.current.setPaintProperty('houses-layer', 'circle-opacity', opacity);
                mapInstanceRef.current.setPaintProperty('houses-layer', 'circle-radius', 5); 
                mapInstanceRef.current.setPaintProperty('houses-layer', 'circle-stroke-width', 1.2);
            } else {
                mapInstanceRef.current.setPaintProperty(
                    'houses-layer',
                    'circle-opacity',
                    ['case', ['==', ['get', 'cluster_id'], clusterId], 0.9, 0.2]
                );
                
                mapInstanceRef.current.setPaintProperty(
                    'houses-layer',
                    'circle-radius',
                    ['case', ['==', ['get', 'cluster_id'], clusterId], 8, 5] // Bigger for better clickability
                );
                
                mapInstanceRef.current.setPaintProperty(
                    'houses-layer',
                    'circle-stroke-width',
                    ['case', ['==', ['get', 'cluster_id'], clusterId], 2, 0.8]
                );
            }
        }
    };

    const createCustomPopup = (coordinates: [number, number], properties: any) => {
        if (!mapInstanceRef.current) return;
        if (activePopupRef.current) {
            activePopupRef.current.remove();
        }
        
        const formattedPrice = formatPrice(properties.price);
        const formattedClusterAvgPrice = formatPrice(properties.cluster_avg_price);
        
        const popupContainer = document.createElement('div');
        popupContainer.className = `popup-container ${isDarkMode ? 'dark-popup' : 'light-popup'}`;
        popupContainer.setAttribute('role', 'dialog');
        popupContainer.setAttribute('aria-label', 'House Information');
        
        const popupContent = document.createElement('div');
        popupContent.className = 'popup-content';
        popupContent.style.position = 'relative';
        popupContent.style.padding = '16px';
        popupContent.style.borderRadius = '8px';
        popupContent.style.minWidth = '280px';
        popupContent.style.backgroundColor = isDarkMode ? '#2b1f66' : '#d5ccff';
        popupContent.style.color = isDarkMode ? '#f3f4f6' : '#111827';
        popupContent.style.boxShadow = '0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)';
        
        const addressElement = document.createElement('h3');
        addressElement.innerText = properties.address;
        addressElement.style.fontWeight = 'bold';
        addressElement.style.marginBottom = '12px';
        addressElement.style.paddingRight = '24px';
        addressElement.style.fontSize = '16px';
        
        const detailsGrid = document.createElement('div');
        detailsGrid.style.display = 'grid';
        detailsGrid.style.gridTemplateColumns = 'repeat(2, 1fr)';
        detailsGrid.style.gap = '8px';
        detailsGrid.style.marginBottom = '12px';
        
        const priceElement = document.createElement('div');
        const priceLabel = document.createElement('div');
        priceLabel.innerText = 'Price';
        priceLabel.style.fontWeight = 'bold';
        priceLabel.style.fontSize = '14px';
        const priceValue = document.createElement('div');
        priceValue.innerText = formattedPrice;
        priceValue.style.fontSize = '15px';
        priceElement.appendChild(priceLabel);
        priceElement.appendChild(priceValue);
        
        const bedroomElement = document.createElement('div');
        const bedroomLabel = document.createElement('div');
        bedroomLabel.innerText = 'Bedrooms';
        bedroomLabel.style.fontWeight = 'bold';
        bedroomLabel.style.fontSize = '14px';
        const bedroomValue = document.createElement('div');
        bedroomValue.innerText = properties.bedrooms;
        bedroomValue.style.fontSize = '15px';
        bedroomElement.appendChild(bedroomLabel);
        bedroomElement.appendChild(bedroomValue);
        
        const bathroomElement = document.createElement('div');
        const bathroomLabel = document.createElement('div');
        bathroomLabel.innerText = 'Bathrooms';
        bathroomLabel.style.fontWeight = 'bold';
        bathroomLabel.style.fontSize = '14px';
        const bathroomValue = document.createElement('div');
        bathroomValue.innerText = properties.bathrooms;
        bathroomValue.style.fontSize = '15px';
        bathroomElement.appendChild(bathroomLabel);
        bathroomElement.appendChild(bathroomValue);
        
        const clusterAvgElement = document.createElement('div');
        const clusterAvgLabel = document.createElement('div');
        clusterAvgLabel.innerText = 'Cluster Avg';
        clusterAvgLabel.style.fontWeight = 'bold';
        clusterAvgLabel.style.fontSize = '14px';
        const clusterAvgValue = document.createElement('div');
        clusterAvgValue.innerText = formattedClusterAvgPrice;
        clusterAvgValue.style.fontSize = '15px';
        clusterAvgElement.appendChild(clusterAvgLabel);
        clusterAvgElement.appendChild(clusterAvgValue);
        
        detailsGrid.appendChild(priceElement);
        detailsGrid.appendChild(bedroomElement);
        detailsGrid.appendChild(bathroomElement);
        detailsGrid.appendChild(clusterAvgElement);
        
        const buttonsContainer = document.createElement('div');
        buttonsContainer.style.display = 'flex';
        buttonsContainer.style.gap = '8px';
        buttonsContainer.style.marginTop = '8px';
        
        const toggleButtonContainer = document.createElement('div');
        toggleButtonContainer.style.flex = '1';
        
        const closeButtonContainer = document.createElement('div');
        closeButtonContainer.style.cursor = 'pointer';
        
        popupContent.appendChild(addressElement);
        popupContent.appendChild(detailsGrid);
        
        const divider = document.createElement('div');
        divider.style.height = '1px';
        divider.style.backgroundColor = isDarkMode ? '#374151' : '#e5e7eb';
        divider.style.margin = '8px 0';
        popupContent.appendChild(divider);
        
        buttonsContainer.appendChild(toggleButtonContainer);
        buttonsContainer.appendChild(closeButtonContainer);
        popupContent.appendChild(buttonsContainer);
        
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
        
        const toggleRoot = ReactDOM.createRoot(toggleButtonContainer);
        toggleRoot.render(
            <button
                className="flex items-center justify-center gap-2 py-2 px-3 bg-primary/90 hover:bg-primary text-primary-foreground text-sm rounded-md w-full"
                onClick={() => {
                    setShowAllClusters(!showAllClusters);
                    updateHouseOpacity(properties.cluster_id, !showAllClusters);
                }}
                aria-label={showAllClusters ? "Hide other clusters" : "Show all clusters"}
            >
                {showAllClusters ? <ArrowLeft size={16} /> : <Info size={16} />}
                {showAllClusters ? "Hide Others" : "Show All Clusters"}
            </button>
        );
        
        const closeRoot = ReactDOM.createRoot(closeButtonContainer);
        closeRoot.render(
            <X 
                size={20} 
                onClick={() => {
                    popup.remove();
                }} 
                color={isDarkMode ? '#e5e7eb' : '#4b5563'} 
                style={{
                    cursor: 'pointer',
                    padding: '8px',
                    borderRadius: '4px',
                    backgroundColor: isDarkMode ? 'rgba(255,255,255,0.1)' : 'rgba(0,0,0,0.05)'
                }}
                aria-label="Close popup"
            />
        );
        
        activePopupRef.current = popup;
        
        setSelectedClusterId(properties.cluster_id);
        updateHouseOpacity(properties.cluster_id, showAllClusters);
        
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

    const renderLegend = () => {
        const clusterGroups = clusters.map((cluster, index) => {
            return {
                id: cluster.cluster_id,
                avgPrice: cluster.avg_price,
                color: clusterColors[index % clusterColors.length],
                count: cluster.houses?.length || 0
            };
        }).sort((a, b) => a.id - b.id);
        
        return (
            <div className="bg-card rounded-md p-4 border border-border w-64 absolute bottom-6 right-6 z-10 shadow-md">
                <h3 className="text-lg font-medium mb-3">Price Clusters</h3>
                <div className="space-y-2 max-h-40 overflow-y-auto">
                    {clusterGroups.map(cluster => (
                        <div 
                            key={cluster.id} 
                            className="flex items-center justify-between gap-2 cursor-pointer hover:bg-accent/50 p-1 rounded"
                            onClick={() => {
                                setSelectedClusterId(cluster.id);
                                updateHouseOpacity(cluster.id, showAllClusters);
                                
                                const houseInCluster = housesWithClusterInfo.find(h => h.cluster_id === cluster.id);
                                if (houseInCluster && mapInstanceRef.current) {
                                    mapInstanceRef.current.flyTo({
                                        center: [houseInCluster.long, houseInCluster.lat],
                                        zoom: 13,
                                        essential: true
                                    });
                                }
                            }}
                        >
                            <div className="flex items-center gap-2">
                                <div 
                                    style={{ backgroundColor: cluster.color }} 
                                    className="w-4 h-4 rounded-full border border-border"
                                    aria-label={`Cluster ${cluster.id} color indicator`}
                                ></div>
                                <span className="text-sm">Cluster {cluster.id}</span>
                            </div>
                            <div className="text-sm font-medium">{formatPrice(cluster.avgPrice)}</div>
                        </div>
                    ))}
                </div>
                <div className="mt-3 text-xs text-muted-foreground">
                    Click a cluster to highlight
                </div>
            </div>
        );
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

                // Add accessibility controls
                mapInstanceRef.current.addControl(new mapboxgl.NavigationControl({
                    visualizePitch: true
                }), 'top-right');
                
                // Add keyboard shortcuts help
                const keyboardTips = document.createElement('div');
                keyboardTips.className = 'keyboard-tips';
                keyboardTips.style.position = 'absolute';
                keyboardTips.style.top = '10px';
                keyboardTips.style.left = '10px';
                keyboardTips.style.zIndex = '1';
                keyboardTips.style.backgroundColor = isDarkMode ? 'rgba(0,0,0,0.7)' : 'rgba(255,255,255,0.7)';
                keyboardTips.style.padding = '5px 10px';
                keyboardTips.style.borderRadius = '4px';
                keyboardTips.style.fontSize = '12px';
                keyboardTips.style.pointerEvents = 'none';
                keyboardTips.style.transition = 'opacity 0.3s';
                keyboardTips.style.opacity = '0';
                keyboardTips.innerText = 'Use ← → ↑ ↓ to navigate, +/- to zoom';
                if (mapRef.current) {
                    mapRef.current.appendChild(keyboardTips);
                }

                // Show keyboard tips when map receives focus
                mapInstanceRef.current.getCanvas().addEventListener('focus', () => {
                    keyboardTips.style.opacity = '1';
                    setTimeout(() => {
                        keyboardTips.style.opacity = '0';
                    }, 5000);
                });

                mapInstanceRef.current.on('load', () => {
                    if (!mapInstanceRef.current) return;

                    // Set ARIA labels for map elements
                    const canvas = mapInstanceRef.current.getCanvas();
                    canvas.setAttribute('aria-label', 'Interactive map of Reno housing clusters');
                    canvas.setAttribute('role', 'application');
                    canvas.setAttribute('tabindex', '0');

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
                            border-top-color: ${isDarkMode ? '#2b1f66' : '#d5ccff'};
                        }
                        .mapboxgl-ctrl button {
                            width: 36px !important;
                            height: 36px !important;
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
                            'circle-radius': 5, // Slightly larger for better clickability
                            'circle-color': ['get', 'color'],
                            'circle-stroke-width': 1.2,
                            'circle-stroke-color': isDarkMode ? '#ffffff' : '#000000',
                            'circle-opacity': 0.4, // Start with lower opacity to reduce visual clutter
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
                                'circle-radius': 5,
                                'circle-color': ['get', 'color'],
                                'circle-stroke-width': 1.2,
                                'circle-stroke-color': isDarkMode ? '#ffffff' : '#000000',
                                'circle-opacity': 0.4,
                            },
                        });
                    } else {
                        (mapInstanceRef.current.getSource('houses') as mapboxgl.GeoJSONSource)
                            .setData(housesGeoJSON);
                    }
                    if (selectedClusterId !== null) {
                        updateHouseOpacity(selectedClusterId, showAllClusters);
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
                updateHouseOpacity(selectedClusterId, showAllClusters);
            }
        }
    }, [houses, clusters, clusterColors, showAllClusters]);

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
            <div className="w-full flex items-center justify-between flex-wrap gap-4">
                <div className="flex-1 min-w-64">
                    <HouseSelect onSelect={handleHouseSelect} />
                </div>
                
                <div className="flex gap-2">
                    <TooltipProvider>
                        <Tooltip>
                            <TooltipTrigger asChild>
                                <button 
                                    onClick={toggleClusterVisibility}
                                    className="px-4 py-2 bg-accent text-accent-foreground rounded-md hover:bg-accent/90 transition-colors"
                                    aria-label={showAllClusters ? "Hide all clusters" : "Show all clusters"}
                                >
                                    {showAllClusters ? "Hide Clusters" : "Show All Clusters"}
                                </button>
                            </TooltipTrigger>
                            <TooltipContent>
                                <p>{showAllClusters ? "Reduce visibility of all clusters" : "Make all clusters fully visible"}</p>
                            </TooltipContent>
                        </Tooltip>
                    </TooltipProvider>
                    
                    {(selectedClusterId || showAllClusters) && (
                        <TooltipProvider>
                            <Tooltip>
                                <TooltipTrigger asChild>
                                    <button 
                                        onClick={resetMapView}
                                        className="px-4 py-2 bg-primary text-primary-foreground rounded-md hover:bg-primary/90 transition-colors"
                                        aria-label="Reset map view"
                                    >
                                        Reset View
                                    </button>
                                </TooltipTrigger>
                                <TooltipContent>
                                    <p>Return to default map view</p>
                                </TooltipContent>
                            </Tooltip>
                        </TooltipProvider>
                    )}
                </div>
            </div>
            
            <div className="relative w-full h-[700px] rounded-lg overflow-hidden border border-border">
                <div className="w-full h-full" ref={mapRef} />
                {renderLegend()}
            </div>
            
            <div className="text-sm text-muted-foreground">
                <p>Use the map to explore housing clusters in Reno. Each color represents a group of houses with similar characteristics.</p>
                <p>Click on a house to see details or use the dropdown to search for a specific property.</p>
            </div>
        </div>
    );
}
