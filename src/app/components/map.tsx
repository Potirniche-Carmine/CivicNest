"use client"

import React, { useEffect, useRef } from "react";
import mapboxgl from 'mapbox-gl';
import { useTheme } from "next-themes";

mapboxgl.accessToken = 'pk.eyJ1IjoidG5vcnJpczU1IiwiYSI6ImNtNWxpdjVrOTB4b3gyam9xNGJpbml3YnQifQ.xAv-Vz7lcSjlya4TuFScYA';

export function Map() {
    const mapRef = useRef<HTMLDivElement>(null);
    const mapInstanceRef = useRef<mapboxgl.Map | null>(null);
    const { theme, systemTheme } = useTheme();

    const isDarkMode = theme === "system" 
        ? systemTheme === "dark"
        : theme === "dark";

    const polygons: GeoJSON.FeatureCollection<GeoJSON.Polygon> = {
        type: "FeatureCollection",
        features: [
            {
                type: "Feature",
                properties: { 
                    id: 1, 
                    color: isDarkMode ? "#4a9eff" : "#2b6cb0"
                },
                geometry: {
                    type: "Polygon",
                    coordinates: [
                        [
                            [-119.858883, 39.512475],  
                            [-119.856763, 39.512631],  
                            [-119.851716, 39.514111],  
                            [-119.850298, 39.515931],  
                            [-119.848867, 39.518351],  
                            [-119.846009, 39.519976],  
                            [-119.834961, 39.524137],  
                            [-119.830844, 39.525441],  
                            [-119.828201, 39.525975],  
                            [-119.826750, 39.526761],  
                            [-119.826447, 39.526426],  
                            [-119.825039, 39.522065],  
                            [-119.824540, 39.520377],  
                            [-119.824540, 39.520043],  
                            [-119.824952, 39.519207],  
                            [-119.825104, 39.518088],  
                            [-119.825702, 39.515917],  
                            [-119.830327, 39.513025],  
                            [-119.832080, 39.512687],  
                            [-119.835828, 39.509908],  
                            [-119.837760, 39.509670],  
                            [-119.840632, 39.508793],  
                            [-119.844673, 39.507191],  
                            [-119.846409, 39.506790],  
                            [-119.848032, 39.505923],  
                            [-119.851010, 39.505312],  
                            [-119.853218, 39.505617],  
                            [-119.858445, 39.507529],  
                            [-119.858487, 39.510695],  
                            [-119.858883, 39.512475],

                        ],
                    ],
                },
            },
            {
                type: "Feature",
                properties: { 
                    id: 2, 
                    color: isDarkMode ? "#48bb78" : "#2f855a"
                },
                geometry: {
                    type: "Polygon",
                    coordinates: [
                        [
                            [-119.862108, 39.523864],  
                            [-119.858053, 39.525579],  
                            [-119.853998, 39.526185],  
                            [-119.836142, 39.526941],  
                            [-119.830452, 39.528909],  
                            [-119.828490, 39.530170],  
                            [-119.823715, 39.531633],  
                            [-119.819006, 39.533600],  
                            [-119.815932, 39.534205],  
                            [-119.814385, 39.529985],  
                            [-119.825395, 39.527843],  
                            [-119.827937, 39.526275],  
                            [-119.835278, 39.524291],  
                            [-119.847818, 39.519552],  
                            [-119.849175, 39.518531],  
                            [-119.849804, 39.517871],  
                            [-119.851025, 39.515531],  
                            [-119.852699, 39.514344],  
                            [-119.857115, 39.513089],  
                            [-119.859123, 39.512795],  
                            [-119.862108, 39.523864],
                        ],
                    ],
                },
            },
        ],
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
                    center: [-119.816326, 39.543627],
                    zoom: 15,
                });

                mapInstanceRef.current.on('load', () => {
                    if (!mapInstanceRef.current) return;

                    mapInstanceRef.current.addSource('polygons', {
                        type: 'geojson',
                        data: polygons,
                    });

                    mapInstanceRef.current.addLayer({
                        id: 'polygons-layer',
                        type: 'fill',
                        source: 'polygons',
                        paint: {
                            'fill-color': ['get', 'color'],
                            'fill-opacity': isDarkMode ? 0.6 : 0.5, // Slightly higher opacity for dark mode
                        },
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

                    if (!mapInstanceRef.current.getSource('polygons')) {
                        mapInstanceRef.current.addSource('polygons', {
                            type: 'geojson',
                            data: polygons,
                        });

                        mapInstanceRef.current.addLayer({
                            id: 'polygons-layer',
                            type: 'fill',
                            source: 'polygons',
                            paint: {
                                'fill-color': ['get', 'color'],
                                'fill-opacity': isDarkMode ? 0.6 : 0.5,
                            },
                        });
                    } else {
                        (mapInstanceRef.current.getSource('polygons') as mapboxgl.GeoJSONSource)
                            .setData(polygons);
                    }
                });
            }
        };

        initializeMap();

        return () => {
            mapInstanceRef.current?.remove();
            mapInstanceRef.current = null;
        };
    }, [isDarkMode]);

    return (
        <div className="w-full h-[700px] rounded-lg overflow-hidden border border-border" ref={mapRef} />
    );
}
