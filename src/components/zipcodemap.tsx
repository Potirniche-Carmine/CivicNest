"use client";
import React, { useEffect, useRef, useState } from "react";
import mapboxgl from 'mapbox-gl';
import { useTheme } from "next-themes";
import { House } from 'lucide-react';
import ReactDOM from 'react-dom/client';
import { Skeleton } from "./ui/skeleton";
import { houses, EmploymentPrediction } from "@/lib/types";

mapboxgl.accessToken = process.env.NEXT_PUBLIC_MAPBOX_ACCESS_TOKEN || "";

const DEFAULT_ZOOM = 11;
const DEFAULT_CENTER: [number, number] = [-119.8143, 39.5299];

const generateClusterColors = () => {
    return [
        '#3366CC',
        '#DC3912',
        '#FF9900',
        '#109618',
        '#990099',
        '#0099C6',
        '#DD4477',
        '#66AA00',
        '#B82E2E',
        '#316395',
        '#994499',
        '#22AA99'
    ];
};

const formatPrice = (price: number): string => {
    return new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD',
        minimumFractionDigits: 0,
        maximumFractionDigits: 0
    }).format(price);
};

interface MapProps {
    zipcode?: string;
}

export function ZipcodeMap({ zipcode }: MapProps = {}) {
    const mapRef = useRef<HTMLDivElement>(null);
    const mapInstanceRef = useRef<mapboxgl.Map | null>(null);
    const activePopupRef = useRef<mapboxgl.Popup | null>(null);
    const [houses, setHouses] = useState<houses[]>([]);
    const [clusters, setClusters] = useState<any[]>([]);
    const [clusterColors, setClusterColors] = useState<string[]>([]);
    const [employmentData, setEmploymentData] = useState<EmploymentPrediction[]>([]);
    const [isLoading, setIsLoading] = useState(true);
    const [displayMode, setDisplayMode] = useState<'all' | 'selectedHouse' | 'selectedClusters'>('all');
    const { theme, systemTheme } = useTheme();

    const isDarkMode = theme === "system"
        ? systemTheme === "dark"
        : theme === "dark";

    useEffect(() => {
        const fetchData = async () => {
          setIsLoading(true);
          try {
            const [locationResponse, clusterResponse, employmentResponse] = await Promise.all([
              fetch('/api/locations'),
              fetch('/api/clusters'),
              fetch('/api/employment')
            ]);
            const locationData = await locationResponse.json();
            const clusterData = await clusterResponse.json();
            const employmentData = await employmentResponse.json();
            
            const allHouses = locationData.houses || [];
            const filteredHouseData = zipcode 
              ? allHouses.filter((house: houses) => String(house.zipcode) === String(zipcode))
              : allHouses;
            
            setHouses(filteredHouseData);
            const clustersArray = clusterData.clusters || [];
            setClusters(clustersArray);
            setClusterColors(generateClusterColors());
            setEmploymentData(employmentData.employmentPredictions || []);
            
            if (zipcode && filteredHouseData.length > 0) {
              const avgLat = filteredHouseData.reduce((sum: number, h:houses) => sum + h.lat, 0) / filteredHouseData.length;
              const avgLong = filteredHouseData.reduce((sum: number, h:houses) => sum + h.long, 0) / filteredHouseData.length;
              
              if (mapInstanceRef.current) {
                mapInstanceRef.current.flyTo({
                  center: [avgLong, avgLat],
                  zoom: DEFAULT_ZOOM,
                  essential: true
                });
              }
            }
          } catch (error) {
            console.error('Error fetching data:', error);
            setHouses([]);
            setClusters([]);
            setClusterColors([]);
            setEmploymentData([]);
          } finally {
            setIsLoading(false);
          }
        };
        fetchData();
      }, [zipcode]);


    const getHousesToShow = () => {
        if (displayMode === 'selectedClusters' ) {
            return houses.map(house => {
                const houseCluster = clusters.find(cluster =>
                    cluster.houses.some((h: any) => h.zpid === house.zpid)
                );
                if (!houseCluster) return null;
                const houseInCluster = houseCluster.houses.find((h: any) => h.zpid === house.zpid);
                const clusterIndex = clusters.indexOf(houseCluster);
                const clusterColor = clusterIndex >= 0 ? clusterColors[clusterIndex % clusterColors.length] : isDarkMode ? "#f56565" : "#e53e3e";
                const employmentPrediction = employmentData.find(
                    emp => String(emp.zipcode) === String(house.zipcode)
                );
                return {
                    ...house,
                    bathrooms: houseInCluster?.bathrooms || house.bathrooms,
                    bedrooms: houseInCluster?.bedrooms || house.bedrooms,
                    cluster_id: houseCluster.cluster_id,
                    cluster_avg_price: houseCluster.avg_price,
                    color: clusterColor,
                    employment_prediction: employmentPrediction ? Number(employmentPrediction.percent_change) : null
                };
            }).filter(Boolean);
        }
        return houses.map(house => {
            const houseCluster = clusters.find(cluster =>
                cluster.houses.some((h: any) => h.zpid === house.zpid)
            );
            if (!houseCluster) return null;
            const houseInCluster = houseCluster.houses.find((h: any) => h.zpid === house.zpid);
            const clusterIndex = clusters.indexOf(houseCluster);
            const clusterColor = clusterIndex >= 0 ? clusterColors[clusterIndex % clusterColors.length] : isDarkMode ? "#f56565" : "#e53e3e";
            const employmentPrediction = employmentData.find(
                emp => String(emp.zipcode) === String(house.zipcode)
            );
            return {
                ...house,
                bathrooms: houseInCluster?.bathrooms || house.bathrooms,
                bedrooms: houseInCluster?.bedrooms || house.bedrooms,
                cluster_id: houseCluster.cluster_id,
                cluster_avg_price: houseCluster.avg_price,
                color: clusterColor,
                employment_prediction: employmentPrediction?.percent_change ?? null
            };
        }).filter(Boolean);
    };

    const updateHouseVisibility = () => {
        if (!mapInstanceRef.current || !mapInstanceRef.current.getSource('houses')) return;
        const updatedGeoJSON = {
            type: "FeatureCollection",
            features: getHousesToShow().map((house: any) => ({
                type: "Feature",
                properties: {
                    id: house.zpid,
                    address: house.address,
                    price: house.price,
                    cluster_id: house.cluster_id,
                    bathrooms: house.bathrooms,
                    bedrooms: house.bedrooms,
                    cluster_avg_price: house.cluster_avg_price,
                    color: house.color,
                },
                geometry: {
                    type: "Point",
                    coordinates: [house.long, house.lat]
                }
            }))
        } as GeoJSON.FeatureCollection<GeoJSON.Point>;
        (mapInstanceRef.current.getSource('houses') as mapboxgl.GeoJSONSource)
            .setData(updatedGeoJSON);
    };

    const createCustomPopup = (coordinates: [number, number], properties: any) => {
        if (!mapInstanceRef.current) return;
        if (activePopupRef.current) {
            activePopupRef.current.remove();
            activePopupRef.current = null;
        }

        const formattedPrice = formatPrice(properties.price);
        const formattedClusterAvgPrice = formatPrice(properties.cluster_avg_price);

        const popupContainer = document.createElement('div');
        popupContainer.className = `popup-container ${isDarkMode ? 'dark-popup' : 'light-popup'}`;
        popupContainer.setAttribute('role', 'dialog');
        popupContainer.setAttribute('aria-label', 'House Information');

        const popupContent = document.createElement('div');
        popupContent.className = 'popup-content';
        popupContent.style.position = 'relative';
        popupContent.style.padding = '16px';
        popupContent.style.borderRadius = '10px';
        popupContent.style.minWidth = '300px';
        popupContent.style.backgroundColor = isDarkMode ? '#1a2335' : '#f5f7fa';
        popupContent.style.color = isDarkMode ? '#f3f4f6' : '#1e293b';
        popupContent.style.boxShadow = isDarkMode
            ? '0 8px 16px rgba(0, 0, 0, 0.35)'
            : '0 8px 16px rgba(0, 0, 0, 0.15)';

        const addressElement = document.createElement('h3');
        addressElement.innerText = properties.address;
        addressElement.style.fontWeight = '600';
        addressElement.style.marginBottom = '12px';
        addressElement.style.paddingRight = '24px';
        addressElement.style.fontSize = '16px';

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
        detailsGrid.style.gap = '12px';
        detailsGrid.style.marginBottom = '16px';

        const createDetailItem = (label: string, value: string | number, valueStyle: React.CSSProperties = {}) => {
            const element = document.createElement('div');
            const labelDiv = document.createElement('div');
            labelDiv.innerText = label;
            labelDiv.style.fontWeight = '600';
            labelDiv.style.fontSize = '14px';
            labelDiv.style.opacity = '0.8';
            const valueDiv = document.createElement('div');
            valueDiv.innerText = String(value);
            valueDiv.style.fontSize = '15px';
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
                color: predictionValue > 0 ? '#10b981' : '#ef4444',
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

        const actionsContainer = document.createElement('div');
        actionsContainer.style.display = 'flex';
        actionsContainer.style.flexDirection = 'column';
        actionsContainer.style.gap = '10px';

               const zillowLinkContainer = document.createElement('div');

        const zillowLinkReactContainer = document.createElement('div');
        zillowLinkContainer.appendChild(zillowLinkReactContainer);

        actionsContainer.appendChild(zillowLinkContainer);
        popupContent.appendChild(actionsContainer);
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

    const handleHouseSelect = (house: houses) => {
        setDisplayMode('selectedHouse');
        updateHouseVisibility();
        const houseWithCluster = houses.map(h => {
            const houseCluster = clusters.find(cluster =>
                cluster.houses.some((ch: any) => ch.zpid === h.zpid)
            );
            if (!houseCluster) return null;
            const houseInCluster = houseCluster ?
                houseCluster.houses.find((ch: any) => ch.zpid === h.zpid) :
                null;
            const clusterIndex = houseCluster ? clusters.indexOf(houseCluster) : -1;
            const clusterColor = clusterIndex >= 0 ? clusterColors[clusterIndex % clusterColors.length] : isDarkMode ? "#f56565" : "#e53e3e";
            return {
                ...h,
                bathrooms: houseInCluster?.bathrooms || h.bathrooms,
                bedrooms: houseInCluster?.bedrooms || h.bedrooms,
                cluster_id: houseCluster?.cluster_id || null,
                cluster_avg_price: houseCluster?.avg_price || null,
                color: clusterColor
            };
        }).filter(Boolean).find(h => h?.zpid === house.zpid);
        if (mapInstanceRef.current && houseWithCluster) {
            mapInstanceRef.current.flyTo({
                center: [houseWithCluster.long, houseWithCluster.lat],
                zoom: 15,
                essential: true
            });
            setTimeout(() => {
                const employmentPrediction = employmentData.find(
                    emp => String(emp.zipcode) === String(houseWithCluster.zipcode)
                );
                const properties = {
                    address: houseWithCluster.address,
                    price: houseWithCluster.price,
                    bedrooms: houseWithCluster.bedrooms,
                    bathrooms: houseWithCluster.bathrooms,
                    cluster_id: houseWithCluster.cluster_id,
                    cluster_avg_price: houseWithCluster.cluster_avg_price,
                    zipcode: houseWithCluster.zipcode,
                    employment_prediction: employmentPrediction ? Number(employmentPrediction.percent_change) : null
                };
                createCustomPopup([houseWithCluster.long, houseWithCluster.lat], properties);
            }, 1000);
        }
    };

       const getHousesGeoJSON = () => {
        const housesToShow = getHousesToShow();
        return {
            type: "FeatureCollection",
            features: housesToShow.map((house: any) => ({
                type: "Feature",
                properties: {
                    id: house.zpid,
                    address: house.address,
                    price: house.price,
                    cluster_id: house.cluster_id,
                    bathrooms: house.bathrooms,
                    bedrooms: house.bedrooms,
                    cluster_avg_price: house.cluster_avg_price,
                    color: house.color,
                    employment_prediction: house.employment_prediction !== null ?
                        Number(house.employment_prediction) : null,
                    zipcode: house.zipcode ?? null
                },
                geometry: {
                    type: "Point",
                    coordinates: [house.long, house.lat]
                }
            }))
        } as GeoJSON.FeatureCollection<GeoJSON.Point>;
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
                mapInstanceRef.current.addControl(new mapboxgl.NavigationControl({
                    visualizePitch: true
                }), 'top-right');
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
                    canvas.setAttribute('aria-label', 'Interactive map of Reno housing clusters');
                    canvas.setAttribute('role', 'application');
                    canvas.setAttribute('tabindex', '0');
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
                            border-top-color: ${isDarkMode ? '#2b1f66' : '#d5ccff'};
                        }
                        .mapboxgl-ctrl button {
                            width: 36px !important;
                            height: 36px !important;
                        }
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
                        filter: ['!', ['has', 'point_count']],
                        paint: {
                            'circle-radius': [
                                'case',
                                ['==', ['get', 'isSelected'], true], 12,
                                6
                            ],
                            'circle-color': ['get', 'color'],
                            'circle-stroke-width': [
                                'case',
                                ['==', ['get', 'isSelected'], true], 2,
                                1.2
                            ],
                            'circle-stroke-color': isDarkMode ? '#ffffff' : '#000000',
                            'circle-opacity': 0.9,
                        },
                    });
                    mapInstanceRef.current.on('click', 'houses-layer', (e) => {
                        if (e.features && e.features[0] && e.features[0].properties) {
                            const coordinates = (e.features[0].geometry as GeoJSON.Point).coordinates.slice();
                            const props = e.features[0].properties;
                            createCustomPopup(
                                coordinates as [number, number],
                                props
                            );
                        }
                    });
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
                    mapInstanceRef.current.on('mouseenter', 'clusters', () => {
                        if (mapInstanceRef.current) {
                            mapInstanceRef.current.getCanvas().style.cursor = 'pointer';
                        }
                    });
                    mapInstanceRef.current.on('mouseleave', 'clusters', () => {
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
                    if (!mapInstanceRef.current.getSource('houses')) {
                        mapInstanceRef.current.addSource('houses', {
                            type: 'geojson',
                            data: getHousesGeoJSON(),
                        });
                        mapInstanceRef.current.addLayer({
                            id: 'houses-layer',
                            type: 'circle',
                            source: 'houses',
                            filter: ['!', ['has', 'point_count']],
                            paint: {
                                'circle-radius': [
                                    'case',
                                    ['==', ['get', 'isSelected'], true], 12,
                                    6
                                ],
                                'circle-color': ['get', 'color'],
                                'circle-stroke-width': [
                                    'case',
                                    ['==', ['get', 'isSelected'], true], 2,
                                    1.2
                                ],
                                'circle-stroke-color': isDarkMode ? '#ffffff' : '#000000',
                                'circle-opacity': 0.9,
                            },
                        });
                    } else {
                        (mapInstanceRef.current.getSource('houses') as mapboxgl.GeoJSONSource)
                            .setData(getHousesGeoJSON());
                    }
                });
            }
        };
        initializeMap();
        return () => {
            if (activePopupRef.current) {
                activePopupRef.current.remove();
                activePopupRef.current = null;
            }
            mapInstanceRef.current?.remove();
            mapInstanceRef.current = null;
        };
    }, [isDarkMode, houses, clusters, clusterColors]);

    useEffect(() => {
        if (mapInstanceRef.current) {
            if (mapInstanceRef.current.getSource('houses')) {
                (mapInstanceRef.current.getSource('houses') as mapboxgl.GeoJSONSource)
                    .setData(getHousesGeoJSON());
            }
        }
    }, [displayMode]);

    if (isLoading) {
        return (
            <div className="space-y-4">
                <Skeleton className="w-full h-[700px] rounded-lg" />
            </div>
        );
    }

    return (
        <div className="space-y-4">
            <div className="relative w-full h-[700px] rounded-lg overflow-hidden border border-border">
                <div className="w-full h-full" ref={mapRef} />
            </div>
        </div>
    );
}
