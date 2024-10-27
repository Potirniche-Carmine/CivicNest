"use client"

import React, { useEffect } from "react";
import { Loader } from '@googlemaps/js-api-loader';

export function Map() {

    const mapRef = React.useRef<HTMLDivElement>(null);

    useEffect(() => {

        const initMap = async () => {

            const loader = new Loader({
                apiKey: process.env.NEXT_PUBLIC_MAPS_API_KEY!,
                version: 'weekly'
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
                mapId: 'CIVICNEST_MAPID'
            };

            // Initialize the map
            const map = new google.maps.Map(mapRef.current as HTMLDivElement, mapOptions);
        }

        initMap();
    }, []);

    return (
        <div style={{ height: '725px' }} ref={mapRef} />
    );
}
