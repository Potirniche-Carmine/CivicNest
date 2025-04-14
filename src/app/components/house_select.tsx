import { useState, useEffect, useRef, KeyboardEvent } from 'react';
import { useTheme } from "next-themes";
import { houses } from '@/lib/types';

const MAX_DISPLAY_THRESHOLD = 30;
const MIN_SEARCH_LENGTH = 2;

interface HouseSelectProps {
    onSelect: (house: houses) => void;
}

export default function HouseSelect({ onSelect }: HouseSelectProps) {
    const [Houses, setHouses] = useState<houses[]>([]);
    const [search, setSearch] = useState('');
    const [isLoading, setIsLoading] = useState(true);
    const [showDropdown, setShowDropdown] = useState(false);
    const [activeIndex, setActiveIndex] = useState(-1);
    const { theme, systemTheme } = useTheme();
    const dropdownRef = useRef<HTMLDivElement>(null);
    const inputRef = useRef<HTMLInputElement>(null);

    const isDarkMode = theme === "system"
        ? systemTheme === "dark"
        : theme === "dark";

    useEffect(() => {
        const fetchHouses = async () => {
            try {
                const response = await fetch('/api/locations');
                if (!response.ok) {
                    throw new Error(`API returned ${response.status}`);
                }
                const data = await response.json();
                setHouses(Array.isArray(data.houses) ? data.houses : []);
            } catch (error) {
                console.error('Error fetching houses:', error);
                setHouses([]);
            } finally {
                setIsLoading(false);
            }
        };

        fetchHouses();
    }, []);

    useEffect(() => {
        setActiveIndex(-1);
    }, [search]);

    useEffect(() => {
        const handleClickOutside = (event: MouseEvent) => {
            if (dropdownRef.current && !dropdownRef.current.contains(event.target as Node) &&
                inputRef.current && !inputRef.current.contains(event.target as Node)) {
                setShowDropdown(false);
            }
        };

        document.addEventListener('mousedown', handleClickOutside);
        return () => {
            document.removeEventListener('mousedown', handleClickOutside);
        };
    }, []);

    const filteredHouses = (Houses && Array.isArray(Houses) && search.length >= MIN_SEARCH_LENGTH)
        ? Houses.filter(house =>
            house.address && house.address.toLowerCase().includes(search.toLowerCase())
        )
        : [];

    const handleSelect = (house: houses) => {
        onSelect(house);
        setSearch('');
        setShowDropdown(false);
    };

    const handleKeyDown = (e: KeyboardEvent<HTMLInputElement>) => {
        if (!showDropdown || filteredHouses.length === 0) return;

        if (e.key === 'ArrowDown') {
            e.preventDefault();
            setActiveIndex(prevIndex =>
                prevIndex < filteredHouses.length - 1 ? prevIndex + 1 : 0
            );
            if (dropdownRef.current && activeIndex >= 0) {
                const activeElement = dropdownRef.current.children[activeIndex + 1];
                if (activeElement) {
                    activeElement.scrollIntoView({ block: 'nearest' });
                }
            }
        }
        else if (e.key === 'ArrowUp') {
            e.preventDefault();
            setActiveIndex(prevIndex =>
                prevIndex > 0 ? prevIndex - 1 : filteredHouses.length - 1
            );
            if (dropdownRef.current && activeIndex >= 0) {
                const activeElement = dropdownRef.current.children[activeIndex - 1];
                if (activeElement) {
                    activeElement.scrollIntoView({ block: 'nearest' });
                }
            }
        }
        else if (e.key === 'Enter' && activeIndex >= 0) {
            e.preventDefault();
            handleSelect(filteredHouses[activeIndex]);
        }
        else if (e.key === 'Escape') {
            setShowDropdown(false);
        }
    };

    const shouldShowDropdown = showDropdown &&
        search.length >= MIN_SEARCH_LENGTH &&
        (filteredHouses.length <= MAX_DISPLAY_THRESHOLD) &&
        !isLoading;

    return (
        <div className="relative w-full" role="combobox" aria-expanded={showDropdown} aria-haspopup="listbox" aria-controls="house-dropdown">
            <input
                ref={inputRef}
                type="text"
                className="w-full p-2 border rounded bg-background text-foreground"
                placeholder={isLoading ? "Loading houses..." : "Search houses..."}
                value={search}
                onChange={(e) => {
                    setSearch(e.target.value);
                    setShowDropdown(true);
                }}
                onFocus={() => setShowDropdown(true)}
                onKeyDown={handleKeyDown}
                disabled={isLoading}
                aria-controls="house-dropdown"
                aria-autocomplete="list"
            />
            {shouldShowDropdown && (
                <div
                    id="house-dropdown"
                    ref={dropdownRef}
                    className={`absolute z-10 w-full mt-1 border rounded shadow-lg max-h-60 overflow-auto ${isDarkMode ? 'bg-card text-card-foreground' : 'bg-white text-gray-900'}`}
                    role="listbox"
                >
                    {filteredHouses.length > 0 ? (
                        filteredHouses.map((house, index) => (
                            <div
                                key={house.zpid}
                                className={`p-2 cursor-pointer ${index === activeIndex
                                    ? isDarkMode ? 'bg-primary text-primary-foreground' : 'bg-blue-100'
                                    : isDarkMode ? 'hover:bg-muted' : 'hover:bg-gray-100'
                                    }`}
                                onClick={() => handleSelect(house)}
                                role="option"
                                aria-selected={index === activeIndex}
                                tabIndex={-1}
                            >
                                {house.address}
                            </div>
                        ))
                    ) : (
                        <div className={`p-2 ${isDarkMode ? 'text-muted-foreground' : 'text-gray-500'}`}>
                            No houses found
                        </div>
                    )}
                </div>
            )}

            {showDropdown && search.length >= MIN_SEARCH_LENGTH && filteredHouses.length > MAX_DISPLAY_THRESHOLD && (
                <div className="absolute z-10 w-full mt-1 border rounded p-2 text-center shadow-lg bg-background">
                    {filteredHouses.length} matches found. Please type more to narrow results.
                </div>
            )}
        </div>
    );
}