"use client";
import React, { useEffect, useRef, useState } from "react";
import mapboxgl from 'mapbox-gl';
import { useTheme } from "next-themes";
import { House, Layers } from 'lucide-react';
import ReactDOM from 'react-dom/client';
import { Skeleton } from "./ui/skeleton";
import { houses as HouseType, EmploymentPrediction } from "@/lib/types";

mapboxgl.accessToken = process.env.NEXT_PUBLIC_MAPBOX_ACCESS_TOKEN || "";

const DEFAULT_ZOOM = 12;
const DEFAULT_RENO_CENTER: [number, number] = [-119.8143, 39.5299];

const generateClusterColors = () => {
    return [
        '#3366CC', '#DC3912', '#FF9900', '#109618', '#990099',
        '#0099C6', '#DD4477', '#66AA00', '#B82E2E', '#316395',
        '#994499', '#22AA99'
    ];
};

const formatPrice = (price: number): string => {
    return new Intl.NumberFormat('en-US', {
        style: 'currency', currency: 'USD',
        minimumFractionDigits: 0, maximumFractionDigits: 0
    }).format(price);
};

interface MapProps {
    zipcode: string;
}

export function Map({ zipcode }: MapProps) {
    const mapRef = useRef<HTMLDivElement>(null);
    const mapInstanceRef = useRef<mapboxgl.Map | null>(null);
    const activePopupRef = useRef<mapboxgl.Popup | null>(null);

    const [filteredHouses, setFilteredHouses] = useState<HouseType[]>([]);
    const [relevantClusters, setRelevantClusters] = useState<any[]>([]);
    const [clusterColors, setClusterColors] = useState<string[]>([]);
    const [employmentData, setEmploymentData] = useState<EmploymentPrediction[]>([]);
    const [isLoading, setIsLoading] = useState(true);
    const [mapCenter, setMapCenter] = useState<[number, number]>(DEFAULT_RENO_CENTER);
    const [isLegendVisible, setIsLegendVisible] = useState<boolean>(false);
    const [legendTimeoutId, setLegendTimeoutId] = useState<NodeJS.Timeout | null>(null);

    const { theme, systemTheme } = useTheme();
    const isDarkMode = theme === "system" ? systemTheme === "dark" : theme === "dark";

    useEffect(() => {
        const fetchData = async () => {
            if (!zipcode) {
                setIsLoading(false);
                console.warn("Zipcode prop is missing.");
                return;
            }
            setIsLoading(true);
            try {
                const [locationResponse, clusterResponse, employmentResponse] = await Promise.all([
                    fetch('/api/locations'),
                    fetch('/api/clusters'),
                    fetch('/api/employment')
                ]);

                if (!locationResponse.ok || !clusterResponse.ok || !employmentResponse.ok) {
                    throw new Error('Failed to fetch map data');
                }

                const locationData = await locationResponse.json();
                const clusterData = await clusterResponse.json();
                const employmentData = await employmentResponse.json();

                const allHouses: HouseType[] = locationData.houses || [];
                const allClusters: any[] = clusterData.clusters || [];
                const allEmployment: EmploymentPrediction[] = employmentData.employmentPredictions || [];

                const housesInZipcode = allHouses.filter(house => String(house.zipcode) === String(zipcode));
                setFilteredHouses(housesInZipcode);

                const houseZpidsInZipcode = new Set(housesInZipcode.map(h => h.zpid));
                const filteredClusters = allClusters
                    .map(cluster => ({
                        ...cluster,
                        houses: cluster.houses.filter((h: HouseType) => houseZpidsInZipcode.has(h.zpid))
                    }))
                    .filter(cluster => cluster.houses.length > 0);

                setRelevantClusters(filteredClusters);
                setClusterColors(generateClusterColors());
                setEmploymentData(allEmployment);

                if (housesInZipcode.length > 0) {
                    const avgLat = housesInZipcode.reduce((sum, h) => sum + h.lat, 0) / housesInZipcode.length;
                    const avgLong = housesInZipcode.reduce((sum, h) => sum + h.long, 0) / housesInZipcode.length;
                    setMapCenter([avgLong, avgLat]);
                } else {
                    setMapCenter(DEFAULT_RENO_CENTER);
                    console.warn(`No houses found for zipcode ${zipcode}`);
                }

            } catch (error) {
                console.error('Error fetching or processing map data:', error);
                setFilteredHouses([]);
                setRelevantClusters([]);
                setClusterColors([]);
                setEmploymentData([]);
            } finally {
                setIsLoading(false);
            }
        };
        fetchData();
    }, [zipcode]);

    const getHousesGeoJSON = () => {
        const features = filteredHouses.map((house) => {
            const houseCluster = relevantClusters.find(cluster =>
                cluster.houses.some((h: any) => h.zpid === house.zpid)
            );

            const clusterIndex = houseCluster ? relevantClusters.indexOf(houseCluster) : -1;

            const clusterColor = clusterIndex >= 0
                ? clusterColors[clusterIndex % clusterColors.length]
                : isDarkMode ? "#A0AEC0" : "#4A5568";

            const employmentPrediction = employmentData.find(
                emp => String(emp.zipcode) === String(house.zipcode)
            );

            const houseInCluster = houseCluster?.houses.find((h: any) => h.zpid === house.zpid);

            return {
                type: "Feature",
                properties: {
                    id: house.zpid,
                    address: house.address,
                    price: house.price,
                    cluster_id: houseCluster?.cluster_id ?? null,
                    bathrooms: houseInCluster?.bathrooms ?? house.bathrooms,
                    bedrooms: houseInCluster?.bedrooms ?? house.bedrooms,
                    cluster_avg_price: houseCluster?.avg_price ?? null,
                    color: clusterColor,
                    zipcode: house.zipcode ?? null,
                    employment_prediction: employmentPrediction?.percent_change ?? null
                },
                geometry: {
                    type: "Point",
                    coordinates: [house.long, house.lat]
                }
            };
        }).filter(Boolean);

        return {
            type: "FeatureCollection",
            features: features,
        } as GeoJSON.FeatureCollection<GeoJSON.Point>;
    };

    const createCustomPopup = (coordinates: [number, number], properties: any) => {
        if (!mapInstanceRef.current) return;
        if (activePopupRef.current) {
            activePopupRef.current.remove();
            activePopupRef.current = null;
        }

        const formattedPrice = formatPrice(properties.price);
        const formattedClusterAvgPrice = properties.cluster_avg_price ? formatPrice(properties.cluster_avg_price) : 'N/A';

        const popupContainer = document.createElement('div');
        popupContainer.className = `popup-container ${isDarkMode ? 'dark-popup' : 'light-popup'}`;
        popupContainer.setAttribute('role', 'dialog');
        popupContainer.setAttribute('aria-label', 'House Information');

        const popupContent = document.createElement('div');
        popupContent.className = 'popup-content';
        popupContent.style.position = 'relative';
        popupContent.style.padding = '16px';
        popupContent.style.borderRadius = '10px';
        popupContent.style.minWidth = '280px';
        popupContent.style.backgroundColor = isDarkMode ? '#1a2335' : '#f5f7fa';
        popupContent.style.color = isDarkMode ? '#f3f4f6' : '#1e293b';
        popupContent.style.boxShadow = isDarkMode ? '0 8px 16px rgba(0, 0, 0, 0.35)' : '0 8px 16px rgba(0, 0, 0, 0.15)';

        const addressElement = document.createElement('h3');
        addressElement.innerText = properties.address;
        addressElement.style.fontWeight = '600';
        addressElement.style.marginBottom = '12px';
        addressElement.style.paddingRight = '24px';
        addressElement.style.fontSize = '15px';

        const closeButton = document.createElement('button');
        closeButton.setAttribute('aria-label', 'Close popup');
        closeButton.style.position = 'absolute';
        closeButton.style.top = '12px';
        closeButton.style.right = '12px';
        closeButton.style.background = isDarkMode ? 'rgba(255,255,255,0.1)' : 'rgba(0,0,0,0.05)';
        closeButton.style.border = 'none';
        closeButton.style.borderRadius = '4px';
        closeButton.style.cursor = 'pointer';
        closeButton.style.display = 'flex';
        closeButton.style.alignItems = 'center';
        closeButton.style.justifyContent = 'center';
        closeButton.style.width = '24px';
        closeButton.style.height = '24px';
        closeButton.style.padding = '0';
        closeButton.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="${isDarkMode ? '#e5e7eb' : '#4b5563'}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>`;
        closeButton.onclick = () => {
            if (activePopupRef.current) {
                activePopupRef.current.remove();
                activePopupRef.current = null;
            }
        };
        popupContent.appendChild(closeButton);
        popupContent.appendChild(addressElement);

        const detailsGrid = document.createElement('div');
        detailsGrid.style.display = 'grid';
        detailsGrid.style.gridTemplateColumns = 'repeat(2, 1fr)';
        detailsGrid.style.gap = '10px';
        detailsGrid.style.marginBottom = '14px';

        const createDetailItem = (label: string, value: string | number, valueStyle: React.CSSProperties = {}) => {
            const element = document.createElement('div');
            const labelDiv = document.createElement('div');
            labelDiv.innerText = label;
            labelDiv.style.fontWeight = '600';
            labelDiv.style.fontSize = '13px';
            labelDiv.style.opacity = '0.8';
            const valueDiv = document.createElement('div');
            valueDiv.innerText = String(value);
            valueDiv.style.fontSize = '14px';
            valueDiv.style.marginTop = '2px';
            Object.assign(valueDiv.style, valueStyle);
            element.appendChild(labelDiv);
            element.appendChild(valueDiv);
            return element;
        };

        detailsGrid.appendChild(createDetailItem('Price', formattedPrice));
        detailsGrid.appendChild(createDetailItem('Cluster Avg', formattedClusterAvgPrice));

        const isBedMissingOrZero = properties.bedrooms == null || Number(properties.bedrooms) === 0;
        const isBathMissingOrZero = properties.bathrooms == null || Number(properties.bathrooms) === 0;

        if (isBedMissingOrZero && isBathMissingOrZero) {
            const lotElement = createDetailItem('Property Type', 'Lot');
            lotElement.style.gridColumn = 'span 2';
            detailsGrid.appendChild(lotElement);
        } else {
            if (properties.bedrooms != null && Number(properties.bedrooms) > 0) {
                detailsGrid.appendChild(createDetailItem('Bedrooms', properties.bedrooms));
            } else {
                detailsGrid.appendChild(document.createElement('div'));
            }

            if (properties.bathrooms != null && Number(properties.bathrooms) > 0) {
                detailsGrid.appendChild(createDetailItem('Bathrooms', properties.bathrooms));
            } else {
                detailsGrid.appendChild(document.createElement('div'));
            }
        }

        detailsGrid.appendChild(createDetailItem('Zipcode', properties.zipcode));

        let employmentValue = 'N/A';
        let employmentStyle = {};
        if (properties.employment_prediction !== null &&
            properties.employment_prediction !== undefined &&
            !isNaN(properties.employment_prediction)) {
            const predictionValue = Number(properties.employment_prediction);
            employmentValue = `${predictionValue > 0 ? '+' : ''}${predictionValue.toFixed(2)}%`;
            employmentStyle = {
                color: predictionValue > 0 ? (isDarkMode ? '#34d399' : '#10b981') : (isDarkMode ? '#f87171' : '#ef4444'),
                fontWeight: '500'
            };
        }
        detailsGrid.appendChild(createDetailItem('Employment Trend', employmentValue, employmentStyle));

        popupContent.appendChild(detailsGrid);

        const divider = document.createElement('div');
        divider.style.height = '1px';
        divider.style.backgroundColor = isDarkMode ? 'rgba(255,255,255,0.1)' : 'rgba(0,0,0,0.1)';
        divider.style.margin = '12px 0';
        popupContent.appendChild(divider);

        const zillowLinkContainer = document.createElement('div');
        const zillowLinkReactContainer = document.createElement('div');
        zillowLinkContainer.appendChild(zillowLinkReactContainer);

        popupContent.appendChild(zillowLinkContainer);
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

        const zillowLinkRoot = ReactDOM.createRoot(zillowLinkReactContainer);
        zillowLinkRoot.render(
            <a
                href={`https://www.zillow.com/homedetails/${properties.id}_zpid/`}
                target="_blank"
                rel="noopener noreferrer"
                aria-label={`View ${properties.address} on Zillow`}
                className={`flex items-center justify-center gap-2 py-2 px-4 text-sm font-medium rounded-md w-full ${isDarkMode ? 'bg-blue-900/20 hover:bg-blue-900/30' : 'bg-blue-100/50 hover:bg-blue-100/80'}`}
                style={{
                    color: '#006aff',
                    textDecoration: 'none',
                    boxSizing: 'border-box'
                }}
            >
                <House size={16} color="#006aff" />
                <span>View on Zillow</span>
            </a>
        );

        activePopupRef.current = popup;
        return popup;
    };

    const handleLegendHover = () => {
        if (legendTimeoutId) {
            clearTimeout(legendTimeoutId);
            setLegendTimeoutId(null);
        }
        setIsLegendVisible(true);
    };

    const handleLegendLeave = () => {
        const timeoutId = setTimeout(() => {
            setIsLegendVisible(false);
        }, 1000); // Keep delay
        setLegendTimeoutId(timeoutId);
    };

    const renderLegend = () => {
        const clusterGroups = relevantClusters.map((cluster, index) => ({
            id: cluster.cluster_id,
            name: cluster.display_name,
            color: clusterColors[index % clusterColors.length],
            count: cluster.houses?.length || 0
        })).sort((a, b) => a.id - b.id);

        const isCompact = !isLegendVisible;

        return (
            <div
                className={`bg-card rounded-md border border-border absolute bottom-6 right-6 z-10 shadow-md transition-all duration-300 ease-in-out ${isCompact ? 'w-12 h-12 p-2 hover:scale-105 cursor-pointer' : 'w-72 p-4'}`}
                onMouseEnter={handleLegendHover}
                onMouseLeave={handleLegendLeave}
                onClick={isCompact ? handleLegendHover : undefined}
            >
                {isCompact ? (
                    <div className="w-full h-full flex items-center justify-center">
                        <Layers size={20} className="text-muted-foreground" />
                    </div>
                ) : (
                    <>
                        <h3 className="text-base font-medium mb-2">Relevant Clusters</h3>
                        <div className="space-y-1.5 max-h-32 overflow-y-auto mb-3 pr-1">
                            {clusterGroups.map(cluster => (
                                <div
                                    key={cluster.id}
                                    className="flex items-center justify-between gap-2 p-1 rounded"
                                >
                                    <div className="flex items-center gap-2">
                                        <div style={{ backgroundColor: cluster.color }} className="w-4 h-4 rounded-full border border-border flex-shrink-0" aria-label={`Cluster ${cluster.id} color indicator`}></div>
                                        <span className="text-sm truncate">{cluster.name}</span>
                                    </div>
                                    <span className="text-xs text-muted-foreground">({cluster.count})</span>
                                </div>
                            ))}
                        </div>
                         <div className="text-xs text-muted-foreground">
                            Shows clusters with houses in zipcode {zipcode}.
                         </div>
                    </>
                )}
            </div>
        );
    };


    useEffect(() => {
        if (!mapRef.current || isLoading || !clusterColors.length) return;

        const initializeMap = () => {
            if (!mapInstanceRef.current) {
                mapInstanceRef.current = new mapboxgl.Map({
                    container: mapRef.current as HTMLElement,
                    style: isDarkMode ? "mapbox://styles/mapbox/dark-v11" : "mapbox://styles/mapbox/light-v11",
                    center: mapCenter,
                    zoom: DEFAULT_ZOOM,
                });

                mapInstanceRef.current.addControl(new mapboxgl.NavigationControl({ visualizePitch: true }), 'top-right');

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
                mapInstanceRef.current.getCanvas().addEventListener('focus', () => {
                    keyboardTips.style.opacity = '1';
                    setTimeout(() => {
                        keyboardTips.style.opacity = '0';
                    }, 5000);
                });

                mapInstanceRef.current.on('load', () => {
                    if (!mapInstanceRef.current) return;

                    const canvas = mapInstanceRef.current.getCanvas();
                    canvas.setAttribute('aria-label', `Interactive map of housing in zipcode ${zipcode}`);
                    canvas.setAttribute('role', 'application');
                    canvas.setAttribute('tabindex', '0');

                    const style = document.createElement('style');
                    style.textContent = `
                        .custom-mapbox-popup .mapboxgl-popup-content { padding: 0; overflow: visible; background: transparent; border-radius: 8px; box-shadow: none; }
                        .custom-mapbox-popup .mapboxgl-popup-tip { border-top-color: ${isDarkMode ? '#1a2335' : '#f5f7fa'}; }
                        .mapboxgl-ctrl button { width: 36px !important; height: 36px !important; }
                    `;
                    document.head.appendChild(style);

                    mapInstanceRef.current.addSource('houses', {
                        type: 'geojson',
                        data: getHousesGeoJSON(),
                    });

                    mapInstanceRef.current.addLayer({
                        id: 'houses-layer',
                        type: 'circle',
                        source: 'houses',
                        paint: {
                            'circle-radius': 6,
                            'circle-color': ['get', 'color'],
                            'circle-stroke-width': 1.2,
                            'circle-stroke-color': isDarkMode ? '#ffffff' : '#000000',
                            'circle-opacity': 0.9,
                        },
                    });

                    mapInstanceRef.current.on('click', 'houses-layer', (e) => {
                        if (e.features && e.features[0] && e.features[0].properties) {
                            const coordinates = (e.features[0].geometry as GeoJSON.Point).coordinates.slice();
                            const props = e.features[0].properties;
                            createCustomPopup(coordinates as [number, number], props);
                        }
                    });

                    mapInstanceRef.current.on('mouseenter', 'houses-layer', () => {
                        if (mapInstanceRef.current) mapInstanceRef.current.getCanvas().style.cursor = 'pointer';
                    });
                    mapInstanceRef.current.on('mouseleave', 'houses-layer', () => {
                        if (mapInstanceRef.current) mapInstanceRef.current.getCanvas().style.cursor = '';
                    });

                     mapInstanceRef.current.flyTo({ center: mapCenter, zoom: DEFAULT_ZOOM });

                });

            } else {
                mapInstanceRef.current.setStyle(
                    isDarkMode ? "mapbox://styles/mapbox/dark-v11" : "mapbox://styles/mapbox/light-v11"
                );
                mapInstanceRef.current.once('style.load', () => {
                    if (!mapInstanceRef.current) return;
                    const source = mapInstanceRef.current.getSource('houses');
                    if (source) {
                        (source as mapboxgl.GeoJSONSource).setData(getHousesGeoJSON());
                    } else {
                         mapInstanceRef.current.addSource('houses', {
                             type: 'geojson',
                             data: getHousesGeoJSON(),
                         });
                         mapInstanceRef.current.addLayer({
                             id: 'houses-layer',
                             type: 'circle',
                             source: 'houses',
                             paint: {
                                 'circle-radius': 6,
                                 'circle-color': ['get', 'color'],
                                 'circle-stroke-width': 1.2,
                                 'circle-stroke-color': isDarkMode ? '#ffffff' : '#000000',
                                 'circle-opacity': 0.9,
                             },
                         });
                    }
                    mapInstanceRef.current.flyTo({ center: mapCenter, zoom: DEFAULT_ZOOM });
                });
            }
        };

        initializeMap();

        return () => {
            if (activePopupRef.current) {
                activePopupRef.current.remove();
                activePopupRef.current = null;
            }
        };
    }, [isDarkMode, isLoading, filteredHouses, relevantClusters, clusterColors, mapCenter, zipcode]);

     useEffect(() => {
         if (mapInstanceRef.current && mapInstanceRef.current.getSource('houses') && !isLoading) {
              (mapInstanceRef.current.getSource('houses') as mapboxgl.GeoJSONSource).setData(getHousesGeoJSON());
         }
     }, [filteredHouses, relevantClusters, clusterColors, isLoading]);


    if (isLoading) {
        return (
            <div className="space-y-4">
                <Skeleton className="w-full h-[600px] rounded-lg" />
            </div>
        );
    }

    if (!isLoading && filteredHouses.length === 0 && zipcode) {
        return (
             <div className="flex items-center justify-center h-[600px] bg-card border border-border rounded-lg">
                 <p className="text-muted-foreground">No housing data found for zipcode {zipcode}.</p>
             </div>
        )
    }
    if (!zipcode) {
         return (
             <div className="flex items-center justify-center h-[600px] bg-card border border-border rounded-lg">
                 <p className="text-muted-foreground">Zipcode not provided.</p>
             </div>
         )
    }

    return (
        <div className="space-y-4">
            <div className="relative w-full h-[600px] rounded-lg overflow-hidden border border-border">
                <div className="w-full h-full" ref={mapRef} />
                {relevantClusters.length > 0 && renderLegend()}
            </div>
            <div className="text-sm text-muted-foreground space-y-1">
                <p>Showing houses found in zipcode {zipcode}.</p>
                <p>
                    House colors <span className="inline-block w-3 h-3 rounded-full bg-red-500" aria-hidden="true"></span><span className="inline-block w-3 h-3 rounded-full bg-green-500" aria-hidden="true"></span><span className="inline-block w-3 h-3 rounded-full bg-purple-500" aria-hidden="true"></span> indicate price clusters for the Reno area.
                </p>
                <p>Hover over the legend <Layers size={14} className="inline-block -mt-1" /> (bottom-right) to view relevant cluster details for this zipcode.</p>
                <p>Click on a house circle <span className="inline-block w-3 h-3 rounded-full bg-blue-500 border border-black dark:border-white" aria-hidden="true"></span> to see details and a link to Zillow.</p>
            </div>
        </div>
    );
}