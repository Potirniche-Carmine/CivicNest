"use client";

import React, { useEffect, useRef } from "react";
import mapboxgl from 'mapbox-gl';
import { useDarkMode } from "../DarkModeContext";
import * as turf from '@turf/turf'; // Import Turf for circle generation

mapboxgl.accessToken = 'pk.eyJ1IjoidG5vcnJpczU1IiwiYSI6ImNtNWxpdjVrOTB4b3gyam9xNGJpbml3YnQifQ.xAv-Vz7lcSjlya4TuFScYA';

export function Map() {
    const mapRef = useRef<HTMLDivElement>(null);
    const mapInstanceRef = useRef<mapboxgl.Map | null>(null);
    const { darkMode } = useDarkMode();

    const polygons: GeoJSON.FeatureCollection<GeoJSON.Polygon> = {
        type: "FeatureCollection",
        features: [
            {
                type: "Feature",
                properties: { id: 1, color: "Blue" }, // Initial color
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
                properties: { id: 2, color: "#00FF00" }, // Initial color
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

        if (!mapInstanceRef.current) {
            mapInstanceRef.current = new mapboxgl.Map({
                container: mapRef.current,
                style: darkMode
                    ? "mapbox://styles/mapbox/dark-v11"
                    : "mapbox://styles/mapbox/light-v11",
                center: [-119.816326, 39.543627], // Initial map center [lng, lat]
                zoom: 15, // Initial zoom level
            });

            // Wait for the map to load before adding sources and layers
            mapInstanceRef.current.on('load', () => {
                if (!mapInstanceRef.current) return;

                // Add polygons source
                mapInstanceRef.current?.addSource('polygons', {
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
                        'fill-opacity': 0.5,
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
            // Update the map style dynamically when darkMode changes
            mapInstanceRef.current.setStyle(
                darkMode
                    ? "mapbox://styles/mapbox/dark-v11"
                    : "mapbox://styles/mapbox/light-v11"
            );
        }

        // Cleanup on unmount
        return () => {
            mapInstanceRef.current?.remove();
            mapInstanceRef.current = null;
        };
    }, [darkMode]);

    return <div style={{ height: '700px' }} ref={mapRef} />;
}






