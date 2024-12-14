"use client"

import React, { useEffect, useRef, useState, useMemo} from "react";
import mapboxgl from "mapbox-gl";
import { useDarkMode} from "../DarkModeContext";

interface Location {
    lat: number;
    lng: number; 
}

mapboxgl.accessToken =  process.env.NEXT_PUBLIC_MAPBOX_ACCESS_TOKEN!;

export function Map(){
    const mapRef = useRef<HTMLDivElement>(null);
    const { darkMode } = useDarkMode();
    const [locations, setLocations] = useState<Location[]>([]);

    const darkModeStyles = useMemo(() => "mapbox://styles/mapbox/dark-v11", []);
    const lightModeStyles = useMemo(() => "mapbox://styles/mapbox/streets-v11", []);

    useEffect(() => {
        async function fetchLocations() {
            const res = await fetch('/api/locations');
            const data = await res.json();
            setLocations(data);
        }
        fetchLocations();
    }, []);

    useEffect(() => {
        if (!mapRef.current) return;

        const map = new mapboxgl.Map({
            container: mapRef.current,
            style: darkMode ? darkModeStyles : lightModeStyles,
            center: [-119.81691931136118, 39.543949300371295],
            zoom: 15,
        });

        locations.forEach((location) => {
            new mapboxgl.Marker()
                .setLngLat([location.lng, location.lat])
                .addTo(map);
        });

        return () => {
            map.remove(); // Cleanup map instance on component unmount
        };
    }, [darkMode, darkModeStyles, lightModeStyles, locations]);

    return (
        <div style={{ height: "700px", width: "100%" }} ref={mapRef} />
    );

}