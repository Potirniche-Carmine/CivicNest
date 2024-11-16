"use client"

import React, { useEffect } from "react";
import { Loader } from '@googlemaps/js-api-loader';
import { useDarkMode } from "../DarkModeContext";

export function Map() {

    const mapRef = React.useRef<HTMLDivElement>(null);
    const { darkMode } = useDarkMode();

    useEffect(() => {
        const initMap = async () => {
            const loader = new Loader({
                apiKey: process.env.NEXT_PUBLIC_MAPS_API_KEY!,
                version: 'weekly',
            });

            await loader.load();

            const position = {
                //UNR position
                lat: 39.543949300371295,
                lng:  -119.81691931136118 
            };

            const mapOptions = {
                center: position,
                zoom: 15,
                styles: darkMode ? darkModeStyles : lightModeStyles
            };

            // Initialize the map
            const map = new google.maps.Map(mapRef.current as HTMLDivElement, mapOptions);
        }

        initMap();
    }, [darkMode]);

    const darkModeStyles : google.maps.MapTypeStyle[] = [
        {
          "elementType": "geometry",
          "stylers": [{ "color": "#242f3e" }]
        },
        {
          "elementType": "labels.text.fill",
          "stylers": [{ "color": "#746855" }]
        },
        {
          "elementType": "labels.text.stroke",
          "stylers": [{ "color": "#242f3e" }]
        },
        {
          "featureType": "poi",
          "elementType": "labels.text.fill",
          "stylers": [{ "color": "#d59563" }]
        },
        {
          "featureType": "poi.park",
          "elementType": "geometry",
          "stylers": [{ "color": "#263c3f" }]
        },
        {
          "featureType": "road",
          "elementType": "geometry",
          "stylers": [{ "color": "#38414e" }]
        },
        {
          "featureType": "road.highway",
          "elementType": "geometry",
          "stylers": [{ "color": "#746855" }]
        },
        {
          "featureType": "water",
          "elementType": "geometry",
          "stylers": [{ "color": "#17263c" }]
        }
      ];

    const lightModeStyles: google.maps.MapTypeStyle[] = [];

    return (
        <div style={{ height: '700px'}} ref={mapRef} />
    );
}
