"use client";

import React, { useEffect, useRef, useState } from "react";
import mapboxgl from 'mapbox-gl';
import { useTheme } from "next-themes";
import { X } from 'lucide-react';
import ReactDOM from 'react-dom/client';
import HouseSelect, { houses } from './house_select';
import { Skeleton } from "@/app/components/ui/skeleton";
import { useNeighborhoodPolygons } from "./mapPolygons";

mapboxgl.accessToken = process.env.NEXT_PUBLIC_MAPBOX_ACCESS_TOKEN || "";

const DEFAULT_ZOOM = 11;
const DEFAULT_CENTER: [number, number] = [-119.8143, 39.5299];

export function Map() {
    const mapRef = useRef<HTMLDivElement>(null);
    const mapInstanceRef = useRef<mapboxgl.Map | null>(null);
    const activePopupRef = useRef<mapboxgl.Popup | null>(null);
    const [houses, setHouses] = useState<houses[]>([]);
    const [, setSelectedHouse] = useState<houses | null>(null);
    const [isLoading, setIsLoading] = useState(true);
    const [showClusters, setShowClusters] = useState(true);
    const { theme, systemTheme } = useTheme();

    const isDarkMode = theme === "system" 
        ? systemTheme === "dark"
        : theme === "dark";

    const neighborhoodPolygons = useNeighborhoodPolygons();

    const resetMapView = () => {
        if (mapInstanceRef.current) {
            mapInstanceRef.current.flyTo({
                center: DEFAULT_CENTER,
                zoom: DEFAULT_ZOOM,
                essential: true
            });
        }
    }

    // Fetch houses data
    useEffect(() => {
        const fetchHouses = async () => {
            setIsLoading(true);
            try {
                const response = await fetch('/api/locations');
                const data = await response.json();
                setHouses(data.houses);
            } catch (error) {
                console.error('Error fetching houses:', error);
            } finally {
                setIsLoading(false);
            }
        };

        fetchHouses();
    }, []);

    const housesGeoJSON = {
        type: "FeatureCollection",
        features: houses.map(house => ({
            type: "Feature",
            properties: { 
                id: house.zpid, 
                address: house.address,
                price: house.price,
                color: isDarkMode ? "#f56565" : "#e53e3e"
            },
            geometry: {
                type: "Point",
                coordinates: [house.long, house.lat]
            }
        }))
    } as GeoJSON.FeatureCollection<GeoJSON.Point>;

    // Function to create and display a custom popup for a house
    const createCustomPopup = (coordinates: [number, number], address: string, price: number) => {
        if (!mapInstanceRef.current) return;
        if (activePopupRef.current) {
            activePopupRef.current.remove();
        }
        
        const formattedPrice = new Intl.NumberFormat('en-US', {
            style: 'currency',
            currency: 'USD',
            minimumFractionDigits: 0
        }).format(price);
        
        // Create container for the popup
        const popupContainer = document.createElement('div');
        popupContainer.className = `popup-container ${isDarkMode ? 'dark-popup' : 'light-popup'}`;
        
        // Create the popup content
        const popupContent = document.createElement('div');
        popupContent.className = 'popup-content';
        popupContent.style.position = 'relative';
        popupContent.style.padding = '16px';
        popupContent.style.borderRadius = '8px';
        popupContent.style.minWidth = '100px';
        popupContent.style.backgroundColor = isDarkMode ? '#1f2937' : '#ffffff';
        popupContent.style.color = isDarkMode ? '#f3f4f6' : '#111827';
        popupContent.style.boxShadow = '0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)';
        
        const addressElement = document.createElement('h3');
        addressElement.innerText = address;
        addressElement.style.fontWeight = 'bold';
        addressElement.style.marginBottom = '8px';
        addressElement.style.paddingRight = '24px';
        
        const priceElement = document.createElement('p');
        priceElement.innerText = `Price: ${formattedPrice}`;
        
        const closeButtonContainer = document.createElement('div');
        closeButtonContainer.className = 'close-button-container';
        closeButtonContainer.style.position = 'absolute';
        closeButtonContainer.style.top = '16px';
        closeButtonContainer.style.right = '10px';
        closeButtonContainer.style.cursor = 'pointer';
        
        popupContent.appendChild(addressElement);
        popupContent.appendChild(priceElement);
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
                onClick={() =>{
                 popup.remove()
                 resetMapView()
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
        
        return popup;
    };

    // House selection to see all of the database houses
    const handleHouseSelect = (house: houses) => {
        setSelectedHouse(house);
        if (mapInstanceRef.current) {
            mapInstanceRef.current.flyTo({
                center: [house.long, house.lat],
                zoom: 15,
                essential: true
            });
            
            // Show popup after a short delay to let the animation complete
            setTimeout(() => {
                createCustomPopup([house.long, house.lat], house.address, house.price);
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

                    // Add CSS for custom popups
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
                            border-top-color: ${isDarkMode ? '#1f2937' : '#ffffff'};
                        }
                    `;
                    document.head.appendChild(style);

                    // Add neighborhood polygons source and layer
                    mapInstanceRef.current.addSource('neighborhoods', {
                        type: 'geojson',
                        data: neighborhoodPolygons
                    });

                    mapInstanceRef.current.addLayer({
                        id: 'neighborhoods-layer',
                        type: 'fill',
                        source: 'neighborhoods',
                        paint: {
                            'fill-color': ['get', 'color'],
                            'fill-opacity': isDarkMode ? 0.6 : 0.5,
                        }
                    });

                    mapInstanceRef.current.addSource('houses', {
                        type: 'geojson',
                        data: housesGeoJSON,
                    });

                    mapInstanceRef.current.addLayer({
                        id: 'houses-layer',
                        type: 'circle',
                        source: 'houses',
                        paint: {
                            'circle-radius': 8,
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
                                props.address, 
                                props.price
                            );
                        }
                    });

                    // Change cursor on house hover
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

                    // Re-add sources and layers after style change
                    if (!mapInstanceRef.current.getSource('neighborhoods')) {
                        mapInstanceRef.current.addSource('neighborhoods', {
                            type: 'geojson',
                            data: neighborhoodPolygons
                        });

                        mapInstanceRef.current.addLayer({
                            id: 'neighborhoods-layer',
                            type: 'fill',
                            source: 'neighborhoods',
                            paint: {
                                'fill-color': ['get', 'color'],
                                'fill-opacity': isDarkMode ? 0.6 : 0.5,
                            }
                        });
                    }
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
                                'circle-radius': 8,
                                'circle-color': ['get', 'color'],
                                'circle-stroke-width': 1,
                                'circle-stroke-color': isDarkMode ? '#ffffff' : '#000000',
                            },
                        });
                    } else {
                        (mapInstanceRef.current.getSource('houses') as mapboxgl.GeoJSONSource)
                            .setData(housesGeoJSON);
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
    }, [isDarkMode, houses, isLoading]);

    // Update house source data when houses change
    useEffect(() => {
        if (mapInstanceRef.current && mapInstanceRef.current.getSource('houses')) {
            (mapInstanceRef.current.getSource('houses') as mapboxgl.GeoJSONSource)
                .setData(housesGeoJSON);
        }
    }, [houses]);


    return (
        <div className="space-y-4">
            <div className="w-full flex justify-between items-center">
                <HouseSelect onSelect={handleHouseSelect} />
            </div>
            <div className="w-full h-[700px] rounded-lg overflow-hidden border border-border" ref={mapRef} />
        </div>
    );
}