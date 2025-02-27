"use client";

import React, { useEffect, useRef, useState } from "react";
import mapboxgl from 'mapbox-gl';
import { useTheme } from "next-themes";
import * as turf from '@turf/turf';
import { X } from 'lucide-react';
import ReactDOM from 'react-dom/client';
import HouseSelect, { houses } from './house_select';
import { Skeleton } from "@/app/components/ui/skeleton";
import { useNeighborhoodPolygons } from "./mapPolygons";

mapboxgl.accessToken = process.env.NEXT_PUBLIC_MAPBOX_ACCESS_TOKEN || "";

export function Map() {
    const mapRef = useRef<HTMLDivElement>(null);
    const mapInstanceRef = useRef<mapboxgl.Map | null>(null);
    const activePopupRef = useRef<mapboxgl.Popup | null>(null);
    const [houses, setHouses] = useState<houses[]>([]);
    const [, setSelectedHouse] = useState<houses | null>(null);
    const [isLoading, setIsLoading] = useState(true);
    const { theme, systemTheme } = useTheme();

    const isDarkMode = theme === "system" 
        ? systemTheme === "dark"
        : theme === "dark";

    const neighborhoodPolygons = useNeighborhoodPolygons();

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



// This is polygons to test out for future functionality
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
            {
                type: "Feature",
                properties: { 
                    id: 3, 
                    color: isDarkMode ? "#48bb78" : "#2f855a"
                },
                geometry: {
                    type: "Polygon",
                    coordinates: [
                        [
                            [-119.821856, 39.550756],  
                            [-119.817108, 39.534907],  
                            [-119.788122, 39.537364],  
                            [-119.788684, 39.556199],  
                            [-119.800179, 39.556150],  
                            [-119.803115, 39.555091],  
                            [-119.806176, 39.552394],  
                            [-119.821856, 39.550756],
                        ],
                    ],
                },
            },
            {
                type: "Feature",
                properties: { 
                    id: 4, 
                    color: isDarkMode ? "#BB86FC" : "#6200EE"
                },
                geometry: {
                    type: "Polygon",
                    coordinates: [
                        [
                            [-119.822957, 39.550746],
                            [-119.822917, 39.550746],
                            [-119.822883, 39.550741],
                            [-119.822852, 39.550733],
                            [-119.822827, 39.550720],
                            [-119.822813, 39.550710],
                            [-119.822657, 39.550492],
                            [-119.822652, 39.550486],
                            [-119.822247, 39.549974],
                            [-119.822230, 39.549938],
                            [-119.822221, 39.549896],
                            [-119.822215, 39.549846],
                            [-119.822208, 39.549768],
                            [-119.822184, 39.549618],
                            [-119.822180, 39.549178],
                            [-119.822175, 39.549152],
                            [-119.822160, 39.549111],
                            [-119.822120, 39.549028],
                            [-119.822107, 39.548992],
                            [-119.822102, 39.548962],
                            [-119.822032, 39.547270],
                            [-119.822022, 39.547170],
                            [-119.821999, 39.546988],
                            [-119.821983, 39.546872],
                            [-119.817297, 39.534809],
                            [-119.817429, 39.534785],
                            [-119.822763, 39.532528],
                            [-119.823481, 39.532249],
                            [-119.823839, 39.532133],
                            [-119.824565, 39.531930],
                            [-119.827308, 39.531135],
                            [-119.827723, 39.531011],
                            [-119.828244, 39.530811],
                            [-119.828631, 39.530636],
                            [-119.829100, 39.530391],
                            [-119.829172, 39.530343],
                            [-119.831335, 39.528982],
                            [-119.831686, 39.528784],
                            [-119.832170, 39.528525],
                            [-119.832639, 39.528315],
                            [-119.833501, 39.527993],
                            [-119.834023, 39.527834],
                            [-119.834891, 39.527630],
                            [-119.836282, 39.527452],
                            [-119.851567, 39.526867],
                            [-119.851911, 39.526865],
                            [-119.852278, 39.526870],
                            [-119.852803, 39.526878],
                            [-119.853908, 39.526861],
                            [-119.854535, 39.526830],
                            [-119.855350, 39.526759],
                            [-119.855858, 39.526696],
                            [-119.856382, 39.526619],
                            [-119.857565, 39.526351],
                            [-119.857924, 39.526262],
                            [-119.858656, 39.526059],
                            [-119.859302, 39.525853],
                            [-119.860086, 39.525561],
                            [-119.860646, 39.525327],
                            [-119.861450, 39.524944],
                            [-119.862339, 39.524475],
                            [-119.862509, 39.525736],
                            [-119.862545, 39.525966],
                            [-119.862697, 39.526608],
                            [-119.862776, 39.526877],
                            [-119.863074, 39.527715],
                            [-119.863336, 39.528387],
                            [-119.863567, 39.528957],
                            [-119.864119, 39.530372],
                            [-119.864221, 39.530726],
                            [-119.864298, 39.531014],
                            [-119.864382, 39.531585],
                            [-119.864405, 39.532631],
                            [-119.864461, 39.535950],
                            [-119.864422, 39.536280],
                            [-119.864348, 39.536584],
                            [-119.864259, 39.536932],
                            [-119.864149, 39.537237],
                            [-119.863916, 39.537738],
                            [-119.863565, 39.538269],
                            [-119.862873, 39.539078],
                            [-119.862230, 39.539601],
                            [-119.861682, 39.539961],
                            [-119.861243, 39.540195],
                            [-119.860735, 39.540423],
                            [-119.855295, 39.542651],
                            [-119.854709, 39.542921],
                            [-119.854163, 39.543201],
                            [-119.853818, 39.543396],
                            [-119.852346, 39.544352],
                            [-119.851975, 39.544634],
                            [-119.851547, 39.544998],
                            [-119.848000, 39.548375],
                            [-119.847586, 39.548691],
                            [-119.847115, 39.548977],
                            [-119.846588, 39.549224],
                            [-119.846024, 39.549417],
                            [-119.845434, 39.549555],
                            [-119.844952, 39.549615],
                            [-119.831337, 39.550749],
                            [-119.830946, 39.550761],
                            [-119.830253, 39.550739],
                            [-119.825694, 39.550538],
                            [-119.825250, 39.550528],
                            [-119.824741, 39.550548],
                            [-119.824176, 39.550595],
                            [-119.822982, 39.550743],
                            [-119.822957, 39.550746],
                        ],
                    ],
                },
            },
            {
                type: "Feature",
                properties: { 
                    id: 5, 
                    color: isDarkMode ? "#48bb78" : "#2f855a"
                },
                geometry: {
                    type: "Polygon",
                    coordinates: [
                        [
                            [-119.825528, 39.516378],  
                            [-119.825405, 39.516557],  
                            [-119.825108, 39.517311],  
                            [-119.824946, 39.517577],  
                            [-119.824851, 39.517889],  
                            [-119.824824, 39.518388],  
                            [-119.824811, 39.518940],  
                            [-119.824760, 39.519120],  
                            [-119.824561, 39.519549],  
                            [-119.824426, 39.519843],  
                            [-119.824359, 39.520113],  
                            [-119.824342, 39.520381],  
                            [-119.824356, 39.520616],  
                            [-119.824372, 39.520675],  
                            [-119.824463, 39.520990],  
                            [-119.824588, 39.521375],  
                            [-119.824800, 39.521969],  
                            [-119.826328, 39.526509],  
                            [-119.826338, 39.526676],  
                            [-119.826560, 39.526928],  
                            [-119.825575, 39.527617],  
                            [-119.825424, 39.527690],  
                            [-119.825332, 39.527727],  
                            [-119.814318, 39.529821],  
                            [-119.812772, 39.525224],  
                            [-119.812521, 39.524781],  
                            [-119.811568, 39.522240],  
                            [-119.811325, 39.521923],  
                            [-119.811118, 39.521743],  
                            [-119.810494, 39.520419],  
                            [-119.811361, 39.520168],  
                            [-119.821529, 39.520057],  
                            [-119.821713, 39.520041],  
                            [-119.821885, 39.520001],  
                            [-119.822117, 39.519905],  
                            [-119.823229, 39.519153],  
                            [-119.823366, 39.519034],  
                            [-119.824659, 39.517325],  
                            [-119.824869, 39.517186],  
                            [-119.825406, 39.516404],  
                            [-119.825528, 39.516378]  
                        ],
                    ],
                },
            },
            {
                type: "Feature",
                properties: { 
                    id: 6, 
                    color: isDarkMode ? "#BB86FC" : "#6200EE"
                },
                geometry: {
                    type: "Polygon",
                    coordinates: [
                        [
                            [-119.858525, 39.507446],  
                            [-119.858121, 39.507330],  
                            [-119.854425, 39.505990],  
                            [-119.853019, 39.505472],  
                            [-119.852748, 39.505392],  
                            [-119.852451, 39.505319],  
                            [-119.852168, 39.505276],  
                            [-119.851915, 39.505237],  
                            [-119.851360, 39.505203],  
                            [-119.850869, 39.505220],  
                            [-119.850333, 39.505291],  
                            [-119.848798, 39.505548],  
                            [-119.848395, 39.505650],  
                            [-119.847852, 39.505846],  
                            [-119.847437, 39.506058],  
                            [-119.846710, 39.506505],  
                            [-119.846148, 39.506766],  
                            [-119.845877, 39.506845],  
                            [-119.844867, 39.507052],  
                            [-119.844464, 39.507168],  
                            [-119.840509, 39.508731],  
                            [-119.840259, 39.508804],  
                            [-119.837919, 39.509522],  
                            [-119.837326, 39.509642],  
                            [-119.835869, 39.509835],  
                            [-119.835693, 39.509873],  
                            [-119.835042, 39.510405],  
                            [-119.834897, 39.510525],  
                            [-119.832805, 39.511941],  
                            [-119.832285, 39.512394],  
                            [-119.831977, 39.512599],  
                            [-119.830623, 39.512844],  
                            [-119.830369, 39.512904],  
                            [-119.827962, 39.514030],  
                            [-119.827746, 39.514158],  
                            [-119.826118, 39.515369],  
                            [-119.825450, 39.516056],  
                            [-119.824638, 39.517180],  
                            [-119.823965, 39.518133],  
                            [-119.823208, 39.519021],  
                            [-119.822046, 39.519840],  
                            [-119.821807, 39.519926],  
                            [-119.821540, 39.519969],  
                            [-119.811376, 39.520071],  
                            [-119.810455, 39.520321],  
                            [-119.803397, 39.505875],  
                            [-119.826479, 39.505451],  
                            [-119.832718, 39.505051],  
                            [-119.841608, 39.505029],  
                            [-119.842127, 39.505087],  
                            [-119.845251, 39.505014],  
                            [-119.845619, 39.504956],  
                            [-119.851565, 39.502866],  
                            [-119.852301, 39.502458],  
                            [-119.852622, 39.502422],  
                            [-119.853767, 39.502431],  
                            [-119.854044, 39.502338],  
                            [-119.855227, 39.501760],  
                            [-119.855901, 39.501305],  
                            [-119.856968, 39.500777],  
                            [-119.857245, 39.500723],  
                            [-119.858065, 39.500777],  
                            [-119.858010, 39.501150],  
                            [-119.857985, 39.501527],  
                            [-119.858005, 39.501888],  
                            [-119.858075, 39.502260],  
                            [-119.858176, 39.502548],  
                            [-119.858398, 39.503169],  
                            [-119.858488, 39.503682],  
                            [-119.858525, 39.507446]
                        ],
                    ],
                },
            },
            {
                type: "Feature",
                properties: { 
                    id: 6, 
                    color: isDarkMode ? "#4a9eff" : "#2b6cb0"
                },
                geometry: {
                    type: "Polygon",
                    coordinates: [
                        [
                            [-119.815553, 39.534471],  
                            [-119.813268, 39.534997],  
                            [-119.810082, 39.535996],  
                            [-119.809180, 39.536233],  
                            [-119.808365, 39.536382],  
                            [-119.807590, 39.536475],  
                            [-119.806588, 39.536568],  
                            [-119.788459, 39.536803],  
                            [-119.788102, 39.534096],  
                            [-119.787932, 39.533536],  
                            [-119.787624, 39.532833],  
                            [-119.786759, 39.531630],  
                            [-119.785245, 39.530105],  
                            [-119.784565, 39.529128],  
                            [-119.784365, 39.528628],  
                            [-119.784226, 39.528104],  
                            [-119.783851, 39.520096],  
                            [-119.783679, 39.519354],  
                            [-119.780828, 39.510600],  
                            [-119.780574, 39.509359],  
                            [-119.780433, 39.507791],  
                            [-119.780630, 39.506506],  
                            [-119.780743, 39.506005],  
                            [-119.803222, 39.505831],  
                            [-119.806604, 39.512832],  
                            [-119.806622, 39.513058],  
                            [-119.811007, 39.521933],  
                            [-119.811325, 39.522033],  
                            [-119.811811, 39.523296],  
                            [-119.812418, 39.524879],  
                            [-119.812865, 39.525645],  
                            [-119.815553, 39.534471]  
                        ],
                    ],
                },
            },
        ],
    };


    // This is circles to test out different regions
    const circles: GeoJSON.FeatureCollection<GeoJSON.Polygon> = {
        type: "FeatureCollection",
        features: [
            {
                type: "Feature",
                properties: { id: 3, color: "Red" },
                geometry: turf.circle(
                    [-119.81, 39.52], 
                    500, 
                    { steps: 64, units: 'meters' } 
                ).geometry,
            },
            {
                type: "Feature",
                properties: { id: 4, color: "Purple" },
                geometry: turf.circle(
                    [-119.83, 39.56], 
                    300, 
                    { steps: 64, units: 'meters' }
                ).geometry,
            },
        ],
    };

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
                onClick={() => popup.remove()} 
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
                    center: [-119.8143, 39.5299],
                    zoom: 11,
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

                    mapInstanceRef.current.addSource('circles', {
                        type: 'geojson',
                        data: circles,
                    });

                    mapInstanceRef.current.addLayer({
                        id: 'circles-layer',
                        type: 'fill',
                        source: 'circles',
                        paint: {
                            'fill-color': ['get', 'color'],
                            'fill-opacity': 0.5,
                        },
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

                    // Re-add polygon source if needed
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
                    // Re-adding everything in case we need to do it
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

                    if (!mapInstanceRef.current.getSource('circles')) {
                        mapInstanceRef.current.addSource('circles', {
                            type: 'geojson',
                            data: circles,
                        });

                        mapInstanceRef.current.addLayer({
                            id: 'circles-layer',
                            type: 'fill',
                            source: 'circles',
                            paint: {
                                'fill-color': ['get', 'color'],
                                'fill-opacity': 0.5,
                            },
                        });
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

    useEffect(() => {
        if (mapInstanceRef.current && mapInstanceRef.current.getSource('houses')) {
            (mapInstanceRef.current.getSource('houses') as mapboxgl.GeoJSONSource)
                .setData(housesGeoJSON);
        }
    }, [houses]);

    if (isLoading) {
        return (
            <div className="space-y-4">
                <div className="w-full">
                    <Skeleton className="h-10 w-full rounded-md" />
                </div>
                <Skeleton className="w-full h-[700px] rounded-lg" />
            </div>
        );
    }

    return (
        <div className="space-y-4">
            <div className="w-full">
                <HouseSelect onSelect={handleHouseSelect} />
            </div>
            <div className="w-full h-[700px] rounded-lg overflow-hidden border border-border" ref={mapRef} />
        </div>
    );
}
