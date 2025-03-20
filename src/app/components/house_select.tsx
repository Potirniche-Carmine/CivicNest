import { useState, useEffect } from 'react';
import { useTheme } from "next-themes";

export interface houses {
    address: string;
    lat: number;
    long: number;
    price: number; 
    zpid: number; 
    bedrooms: string;
    bathrooms: string;
}

interface HouseSelectProps {
    onSelect: (house: houses) => void;
}

export default function HouseSelect({ onSelect }: HouseSelectProps) {
    const [Houses, setHouses] = useState<houses[]>([]);
    const [search, setSearch] = useState('');
    const [isLoading, setIsLoading] = useState(true);
    const [showDropdown, setShowDropdown] = useState(false);
    const { theme, systemTheme } = useTheme();

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

    const filteredHouses = Houses && Array.isArray(Houses)
        ? Houses.filter(house => 
            house.address && house.address.toLowerCase().includes(search.toLowerCase())
          )
        : [];

    const handleSelect = (house: houses) => {
        onSelect(house);
        setSearch(house.address);
        setShowDropdown(false);
    };

    return (
        <div className="relative w-screen max-w-md">
            <input 
                type="text"
                className="w-full p-2 border rounded bg-background text-foreground"
                placeholder={isLoading ? "Loading houses..." : "Search houses..."}
                value={search}
                onChange={(e) => {
                    setSearch(e.target.value);
                    setShowDropdown(true);
                }}
                onFocus={() => setShowDropdown(true)}
                disabled={isLoading}
            />
            {showDropdown && search && !isLoading && (
                <div className={`absolute z-10 w-full mt-1 border rounded shadow-lg max-h-60 overflow-auto ${isDarkMode ? 'bg-card text-card-foreground' : 'bg-white text-gray-900'}`}>
                    {filteredHouses.length > 0 ? (
                        filteredHouses.map((house) => (
                            <div 
                                key={house.zpid}
                                className={`p-2 cursor-pointer ${isDarkMode ? 'hover:bg-muted' : 'hover:bg-gray-100'}`}
                                onClick={() => handleSelect(house)}
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
        </div>
    );
}