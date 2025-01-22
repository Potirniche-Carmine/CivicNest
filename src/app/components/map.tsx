"use client"

import React, { useEffect,useMemo } from "react";
import mapboxgl from 'mapbox-gl';
import { useDarkMode } from "../DarkModeContext";

mapboxgl.accessToken = 'pk.eyJ1IjoidG5vcnJpczU1IiwiYSI6ImNtNWxpdjVrOTB4b3gyam9xNGJpbml3YnQifQ.xAv-Vz7lcSjlya4TuFScYA'

export function Map() {
    const mapRef = React.useRef<HTMLDivElement>(null);
    const mapInstanceRef = React.useRef<mapboxgl.Map | null>(null);
    const { darkMode } = useDarkMode();

    useEffect(() => {
      if(!mapRef.current) return;
    
      if (!mapInstanceRef.current) {
        mapInstanceRef.current = new mapboxgl.Map({
          container: mapRef.current,
          style: darkMode
            ? "mapbox://styles/mapbox/dark-v11"
            : "mapbox://styles/mapbox/light-v11",
          center: [-119.816326, 39.543627], // Initial map center [lng, lat]
          zoom: 15, // Initial zoom level
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
    },[darkMode]);

    return (
        <div style={{ height: '700px' }} ref={mapRef} />
    );
}