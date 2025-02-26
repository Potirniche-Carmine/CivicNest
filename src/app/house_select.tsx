import { useState, useEffect } from 'react';

export interface houses {
    address: string;
    lat: number;
    long: number;
    price: number; 
    spid: number;
}

interface HouseSelectProps {
    onSelect:(house: houses) => void;
}

export default function HouseSelect({ onSelect }: HouseSelectProps){
    const [Houses, setHouses] = useState<houses[]>([]);
    const [search, setSearch] = useState('');
    const [, setIsLoading] = useState(true);
    const [showDropdown, setShowDropdown] = useState(false);

    useEffect(() => {
        const fetchHouses = async () => {
            try{
                const response = await fetch('/api/locations');
                const data = await response.json();
                setHouses(data.Houses);
            } catch (error) {
                console.error('Error fetching customers:', error);
            } finally {
                setIsLoading(false);
            }
        };

        fetchHouses();
    }, []);

    const filteredHouses = Houses.filter(house => house.address.toLowerCase().includes(search.toLowerCase()));

    const handleSelect = (house : houses) => {
        onSelect(house);
        setSearch(house.address);
        setShowDropdown(false);
    };

    return (
        <div className="relative">
            <input 
            type="text"
            className="w-full p-2 border rounded"
            placeholder="Search houses..."
            value={search}
            onChange={(e) => {
                setSearch(e.target.value);
                setShowDropdown(true);
            }}
            onFocus={() => setShowDropdown(true)}
            />
            {showDropdown && search && (
                <div className="absolute z-10 w-full mt-1 bg-white border rounded shadow-lg max-h-60 overflow-auto">
                    {filteredHouses.map((house) => (
                        <div 
                        key={house.spid}
                        className="p-2 hover:bg-gray-100 cursor-pointer"
                        onClick={() => handleSelect(house)}
                        >
                            {house.address}
                        </div>
                    ))}
                    </div>
            )}
            </div>
    );

}
