"use client";
import React, { useEffect, useRef, useState } from "react";
import mapboxgl from 'mapbox-gl';
import { useTheme } from "next-themes";
import { Info, CheckSquare, Square } from 'lucide-react';
import ReactDOM from 'react-dom/client';
import HouseSelect from './house_select';
import { Skeleton } from "@/app/components/ui/skeleton";
import {
    Tooltip,
    TooltipContent,
    TooltipProvider,
    TooltipTrigger
} from "@/app/components/ui/tooltip";
import { houses, EmploymentPrediction } from "@/lib/types";
import { Badge } from "@/app/components/ui/badge";

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

export function Map() {
    const mapRef = useRef<HTMLDivElement>(null);
    const mapInstanceRef = useRef<mapboxgl.Map | null>(null);
    const activePopupRef = useRef<mapboxgl.Popup | null>(null);
    const [houses, setHouses] = useState<houses[]>([]);
    const [clusters, setClusters] = useState<any[]>([]);
    const [clusterColors, setClusterColors] = useState<string[]>([]);
    const [selectedHouse, setSelectedHouse] = useState<houses | null>(null);
    const [selectedClusterIds, setSelectedClusterIds] = useState<number[]>([]);
    const [employmentData, setEmploymentData] = useState<EmploymentPrediction[]>([]);
    const [showEmploymentOverlay, setShowEmploymentOverlay] = useState<boolean>(false);
    const [isLoading, setIsLoading] = useState(true);
    const [displayMode, setDisplayMode] = useState<'all' | 'selectedHouse' | 'selectedClusters'>('all');
    const [visibleHousesCount, setVisibleHousesCount] = useState<number>(0);
    const [totalHousesCount, setTotalHousesCount] = useState<number>(0);
    const [isLegendVisible, setIsLegendVisible] = useState<boolean>(false);
    const [legendTimeoutId, setLegendTimeoutId] = useState<NodeJS.Timeout | null>(null);
    const { theme, systemTheme } = useTheme();

    const isDarkMode = theme === "system"
        ? systemTheme === "dark"
        : theme === "dark";

    const resetMapView = () => {
        if (mapInstanceRef.current) {
            mapInstanceRef.current.flyTo({
                center: DEFAULT_CENTER,
                zoom: DEFAULT_ZOOM,
                essential: true
            });
            setSelectedClusterIds([]);
            setDisplayMode('all');
            setSelectedHouse(null);
            updateHouseVisibility();
            if (activePopupRef.current) {
                activePopupRef.current.remove();
            }
        }
    }

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
                setHouses(locationData.houses || []);
                const clustersArray = clusterData.clusters || [];
                setClusters(clustersArray);
                setClusterColors(generateClusterColors());
                setEmploymentData(employmentData.employmentPredictions || []);
                const total = clustersArray.reduce(
                    (count: number, cluster: { houses?: any[] }) => count + (cluster.houses?.length || 0),
                    0
                );
                setTotalHousesCount(total);
                setVisibleHousesCount(total);
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
    }, []);

    useEffect(() => {
        updateVisibleHousesCount();
    }, [displayMode, selectedClusterIds, clusters, totalHousesCount]);

    const updateVisibleHousesCount = () => {
        switch (displayMode) {
            case 'all':
                setVisibleHousesCount(totalHousesCount);
                break;
            case 'selectedHouse':
                setVisibleHousesCount(totalHousesCount);
                break;
            case 'selectedClusters':
                if (selectedClusterIds.length > 0) {
                    const selectedCount = clusters
                        .filter(cluster => selectedClusterIds.includes(cluster.cluster_id))
                        .reduce((count, cluster) => count + (cluster.houses?.length || 0), 0);
                    setVisibleHousesCount(selectedCount);
                }
                break;
            default:
                setVisibleHousesCount(totalHousesCount);
        }
    };

    const getHousesToShow = () => {
        if (displayMode === 'selectedClusters' && selectedClusterIds.length > 0) {
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
                if (!selectedClusterIds.includes(houseCluster.cluster_id)) {
                    return null;
                }
                return {
                    ...house,
                    bathrooms: houseInCluster?.bathrooms || house.bathrooms,
                    bedrooms: houseInCluster?.bedrooms || house.bedrooms,
                    cluster_id: houseCluster.cluster_id,
                    cluster_avg_price: houseCluster.avg_price,
                    color: clusterColor,
                    isSelected: selectedHouse?.zpid === house.zpid,
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
                isSelected: selectedHouse?.zpid === house.zpid,
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
                    isSelected: house.isSelected || selectedHouse?.zpid === house.zpid
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
        popupContent.style.borderRadius = '8px';
        popupContent.style.minWidth = '280px';
        popupContent.style.backgroundColor = isDarkMode ? '#2b1f66' : '#d5ccff';
        popupContent.style.color = isDarkMode ? '#f3f4f6' : '#111827';
        popupContent.style.boxShadow = '0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)';
        const addressElement = document.createElement('h3');
        addressElement.innerText = properties.address;
        addressElement.style.fontWeight = 'bold';
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
        const detailsGrid = document.createElement('div');
        detailsGrid.style.display = 'grid';
        detailsGrid.style.gridTemplateColumns = 'repeat(2, 1fr)';
        detailsGrid.style.gap = '8px';
        detailsGrid.style.marginBottom = '12px';
        const priceElement = document.createElement('div');
        const priceLabel = document.createElement('div');
        priceLabel.innerText = 'Price';
        priceLabel.style.fontWeight = 'bold';
        priceLabel.style.fontSize = '14px';
        const priceValue = document.createElement('div');
        priceValue.innerText = formattedPrice;
        priceValue.style.fontSize = '15px';
        priceElement.appendChild(priceLabel);
        priceElement.appendChild(priceValue);
        const clusterAvgElement = document.createElement('div');
        const clusterAvgLabel = document.createElement('div');
        clusterAvgLabel.innerText = 'Cluster Avg';
        clusterAvgLabel.style.fontWeight = 'bold';
        clusterAvgLabel.style.fontSize = '14px';
        const clusterAvgValue = document.createElement('div');
        clusterAvgValue.innerText = formattedClusterAvgPrice;
        clusterAvgValue.style.fontSize = '15px';
        clusterAvgElement.appendChild(clusterAvgLabel);
        clusterAvgElement.appendChild(clusterAvgValue);
        const zipcodeElement = document.createElement('div');
        const zipcodeLabel = document.createElement('div');
        zipcodeLabel.innerText = 'Zipcode';
        zipcodeLabel.style.fontWeight = 'bold';
        zipcodeLabel.style.fontSize = '14px';
        const zipcodeValue = document.createElement('div');
        zipcodeValue.innerText = properties.zipcode;
        zipcodeValue.style.fontSize = '15px';
        zipcodeElement.appendChild(zipcodeLabel);
        zipcodeElement.appendChild(zipcodeValue);
        const employmentElement = document.createElement('div');
        const employmentLabel = document.createElement('div');
        employmentLabel.innerText = 'Employment Trend';
        employmentLabel.style.fontWeight = 'bold';
        employmentLabel.style.fontSize = '14px';
        const employmentValue = document.createElement('div');
        if (properties.employment_prediction !== null &&
            properties.employment_prediction !== undefined &&
            !isNaN(properties.employment_prediction)) {
            const predictionValue = Number(properties.employment_prediction);
            const formattedPrediction = `${predictionValue > 0 ? '+' : ''}${predictionValue.toFixed(2)}%`;
            employmentValue.innerText = formattedPrediction;
            employmentValue.style.color = predictionValue > 0 ? '#10b981' : '#ef4444';
        } else {
            employmentValue.innerText = 'N/A';
        }
        employmentValue.style.fontSize = '15px';
        employmentElement.appendChild(employmentLabel);
        employmentElement.appendChild(employmentValue);
        popupContent.appendChild(addressElement);
        popupContent.appendChild(detailsGrid);
        const divider = document.createElement('div');
        divider.style.height = '1px';
        divider.style.backgroundColor = isDarkMode ? '#374151' : '#e5e7eb';
        divider.style.margin = '8px 0';
        popupContent.appendChild(divider);
        const buttonsContainer = document.createElement('div');
        buttonsContainer.style.display = 'flex';
        buttonsContainer.style.gap = '8px';
        buttonsContainer.style.marginTop = '8px';
        const toggleButtonContainer = document.createElement('div');
        toggleButtonContainer.style.flex = '1';
        detailsGrid.appendChild(priceElement);
        detailsGrid.appendChild(clusterAvgElement);
        if (Number(properties.bedrooms) === 0 && Number(properties.bathrooms) === 0) {
            const lotElement = document.createElement('div');
            lotElement.style.gridColumn = 'span 2';
            const lotLabel = document.createElement('div');
            lotLabel.innerText = 'Property Type';
            lotLabel.style.fontWeight = 'bold';
            lotLabel.style.fontSize = '14px';
            const lotValue = document.createElement('div');
            lotValue.innerText = 'LOT';
            lotValue.style.fontSize = '15px';
            lotElement.appendChild(lotLabel);
            lotElement.appendChild(lotValue);
            detailsGrid.appendChild(lotElement);
        } else {
            const bedroomElement = document.createElement('div');
            const bedroomLabel = document.createElement('div');
            bedroomLabel.innerText = 'Bedrooms';
            bedroomLabel.style.fontWeight = 'bold';
            bedroomLabel.style.fontSize = '14px';
            const bedroomValue = document.createElement('div');
            bedroomValue.innerText = properties.bedrooms;
            bedroomValue.style.fontSize = '15px';
            bedroomElement.appendChild(bedroomLabel);
            bedroomElement.appendChild(bedroomValue);
            const bathroomElement = document.createElement('div');
            const bathroomLabel = document.createElement('div');
            bathroomLabel.innerText = 'Bathrooms';
            bathroomLabel.style.fontWeight = 'bold';
            bathroomLabel.style.fontSize = '14px';
            const bathroomValue = document.createElement('div');
            bathroomValue.innerText = properties.bathrooms;
            bathroomValue.style.fontSize = '15px';
            bathroomElement.appendChild(bathroomLabel);
            bathroomElement.appendChild(bathroomValue);
            detailsGrid.appendChild(bedroomElement);
            detailsGrid.appendChild(bathroomElement);
        }
        detailsGrid.appendChild(zipcodeElement);
        detailsGrid.appendChild(employmentElement);
        popupContent.appendChild(buttonsContainer);
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
        const toggleRoot = ReactDOM.createRoot(toggleButtonContainer);
        toggleRoot.render(
            <button
                className="flex items-center justify-center gap-2 py-2 px-3 bg-primary/90 hover:bg-primary text-primary-foreground text-sm rounded-md w-full"
                onClick={() => {
                    const clusterId = properties.cluster_id;
                    setSelectedClusterIds([clusterId]);
                    setDisplayMode('selectedClusters');
                    updateHouseVisibility();
                }}
                aria-label="Show only this cluster"
            >
                <Info size={16} />
                Show Only This Cluster
            </button>
        );
        activePopupRef.current = popup;
        return popup;
    };

    const handleHouseSelect = (house: houses) => {
        setSelectedHouse(house);
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

    const handleClusterSelection = (clusterId: number) => {
        let newSelectedClusters = [...selectedClusterIds];
        if (newSelectedClusters.includes(clusterId)) {
            newSelectedClusters = newSelectedClusters.filter(id => id !== clusterId);
        } else {
            newSelectedClusters.push(clusterId);
        }
        setSelectedClusterIds(newSelectedClusters);
        if (newSelectedClusters.length > 0) {
            setDisplayMode('selectedClusters');
        } else {
            setDisplayMode('all');
        }
        updateHouseVisibility();
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
        }, 1000);
        setLegendTimeoutId(timeoutId);
    };

    const renderLegend = () => {
        const clusterGroups = clusters.map((cluster, index) => {
            return {
                id: cluster.cluster_id,
                avgPrice: cluster.avg_price,
                color: clusterColors[index % clusterColors.length],
                count: cluster.houses?.length || 0
            };
        }).sort((a, b) => a.id - b.id);
        const isCompact = !isLegendVisible;
        return (
            <div
                className={`bg-card rounded-md border border-border absolute bottom-6 right-6 z-10 shadow-md transition-all duration-300 ease-in-out ${isCompact ? 'w-12 h-12 p-2 hover:scale-105' : 'w-72 p-4'
                    }`}
                onMouseEnter={handleLegendHover}
                onMouseLeave={handleLegendLeave}
            >
                {isCompact ? (
                    <div className="w-full h-full flex items-center justify-center">
                        <div className="grid grid-cols-3 gap-1">
                            {clusterGroups.slice(0, 9).map(cluster => (
                                <div
                                    key={cluster.id}
                                    style={{ backgroundColor: cluster.color }}
                                    className="w-2 h-2 rounded-full"
                                    aria-hidden="true"
                                ></div>
                            ))}
                        </div>
                    </div>
                ) : (
                    <>
                        <h3 className="text-lg font-medium mb-3">Price Clusters</h3>
                        <div className="space-y-2 max-h-40 overflow-y-auto">
                            {clusterGroups.map(cluster => (
                                <div
                                    key={cluster.id}
                                    className="flex items-center justify-between gap-2 cursor-pointer hover:bg-accent/50 p-1 rounded"
                                    onClick={() => handleClusterSelection(cluster.id)}
                                >
                                    <div className="flex items-center gap-2">
                                        {selectedClusterIds.includes(cluster.id) ? (
                                            <CheckSquare size={16} className="text-primary" />
                                        ) : (
                                            <Square size={16} className="text-muted-foreground" />
                                        )}
                                        <div
                                            style={{ backgroundColor: cluster.color }}
                                            className="w-4 h-4 rounded-full border border-border"
                                            aria-label={`Cluster ${cluster.id} color indicator`}
                                        ></div>
                                        <span className="text-sm">Cluster {cluster.id}</span>
                                    </div>
                                    <div className="text-sm font-medium">{formatPrice(cluster.avgPrice)}</div>
                                </div>
                            ))}
                        </div>
                        <div className="mt-3 text-xs text-muted-foreground">
                            Click clusters to select/deselect
                        </div>
                    </>
                )}
            </div>
        );
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
                    isSelected: selectedHouse?.zpid === house.zpid,
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

    const getDisplayModeDescription = () => {
        switch (displayMode) {
            case 'all':
                return "Showing all houses";
            case 'selectedHouse':
                return "Showing all houses with selected property highlighted";
            case 'selectedClusters':
                return `Showing all houses from ${selectedClusterIds.length} selected clusters`;
            default:
                return "";
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
    }, [displayMode, selectedClusterIds, selectedHouse]);

    if (isLoading) {
        return (
            <div className="space-y-4">
                <div className="w-full">
                    <Skeleton className="h-10 rounded-md" />
                </div>
                <Skeleton className="w-full h-[700px] rounded-lg" />
            </div>
        );
    }

    return (
        <div className="space-y-4">
            <div className="w-full flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
                <div className="flex flex-col sm:flex-row sm:items-center gap-2 sm:flex-1">
                    <div className="w-full sm:flex-1 max-w-md sm:max-w-none">
                        <HouseSelect onSelect={handleHouseSelect} />
                    </div>
                    <div className="mt-1 sm:mt-0 sm:flex-shrink-0">
                        <TooltipProvider>
                            <Tooltip>
                                <TooltipTrigger asChild>
                                    <Badge variant="outline" className="px-3 py-1 text-xs bg-card whitespace-nowrap">
                                        Showing <span className="font-bold mx-1">{visibleHousesCount}</span> of <span className="font-bold mx-1">{totalHousesCount}</span> houses
                                    </Badge>
                                </TooltipTrigger>
                                <TooltipContent>
                                    <p>{getDisplayModeDescription()}</p>
                                </TooltipContent>
                            </Tooltip>
                        </TooltipProvider>
                    </div>
                </div>
                <div className="mt-2 sm:mt-0 flex justify-end">
                    <div className="h-10">
                        {(displayMode !== 'all' || selectedClusterIds.length > 0 || selectedHouse) ? (
                            <TooltipProvider>
                                <Tooltip>
                                    <TooltipTrigger asChild>
                                        <button
                                            onClick={resetMapView}
                                            className="px-4 py-2 bg-primary text-primary-foreground rounded-md hover:bg-primary/90 transition-colors"
                                            aria-label="Reset map view"
                                        >
                                            Reset Map View
                                        </button>
                                    </TooltipTrigger>
                                    <TooltipContent>
                                        <p>Return to default map view</p>
                                    </TooltipContent>
                                </Tooltip>
                            </TooltipProvider>
                        ) : (
                            <div className="opacity-0 invisible">
                                <button
                                    className="px-4 py-2 bg-primary text-primary-foreground rounded-md"
                                    aria-hidden="true"
                                >
                                    Reset Map View
                                </button>
                            </div>
                        )}
                    </div>
                </div>
            </div>
            <div className="relative w-full h-[700px] rounded-lg overflow-hidden border border-border">
                <div className="w-full h-full" ref={mapRef} />
                {renderLegend()}
            </div>
            <div className="text-sm text-muted-foreground">
                <p>Use the map to explore housing clusters in Reno. Each color represents a group of houses with similar prices.</p>
                <p>Click on a house to see details, hover over the legend to select clusters, or use the dropdown to search for a specific property.</p>
                <p>Zoom out to see clustered groups of houses with counts displayed.</p>
            </div>
        </div>
    );
}
