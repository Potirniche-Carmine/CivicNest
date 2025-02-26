"use client";

import React, { useEffect, useRef } from "react";
import mapboxgl from 'mapbox-gl';
import { useTheme } from "next-themes";
import * as turf from '@turf/turf'; // Import Turf for circle generation

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
                            [-119.82, 39.54],
                            [-119.81, 39.54],
                            [-119.81, 39.55],
                            [-119.82, 39.55],
                            [-119.82, 39.54],
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
                            [-119.83, 39.53],
                            [-119.82, 39.53],
                            [-119.82, 39.54],
                            [-119.83, 39.54],
                            [-119.83, 39.53],
                        ],
                    ],
                },
            },
        ],
    };

    // Circle data with center coordinates and radius in meters
    const circles: GeoJSON.FeatureCollection<GeoJSON.Polygon> = {
        type: "FeatureCollection",
        features: [
            {
                type: "Feature",
                properties: { id: 3, color: "Red" },
                geometry: turf.circle(
                    [-119.81, 39.52], // Circle center [lng, lat]
                    500, // Radius in meters
                    { steps: 64, units: 'meters' } // Number of points and unit of measurement
                ).geometry,
            },
            {
                type: "Feature",
                properties: { id: 4, color: "Purple" },
                geometry: turf.circle(
                    [-119.83, 39.56], // Circle center [lng, lat]
                    300, // Radius in meters
                    { steps: 64, units: 'meters' }
                ).geometry,
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

            // Add the polygon layer
            mapInstanceRef.current?.addLayer({
                id: 'polygons-layer',
                type: 'fill',
                source: 'polygons',
                paint: {
                    'fill-color': ['get', 'color'],
                    'fill-opacity': isDarkMode ? 0.6 : 0.5,
                },
            });

            // Add circles source
            mapInstanceRef.current?.addSource('circles', {
                type: 'geojson',
                data: circles,
            });

            // Add the circle layer
            mapInstanceRef.current?.addLayer({
                id: 'circles-layer',
                type: 'fill',
                source: 'circles',
                paint: {
                    'fill-color': ['get', 'color'],
                    'fill-opacity': 0.5,
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
    return <div style={{ height: '700px' }} ref={mapRef} />;
}