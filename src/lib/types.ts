export interface houses {
    zpid: number;
    address: string;
    lat: number;
    long: number;
    price: number;
    bedrooms: number;
    bathrooms: number;
    zipcode: string;
    cluster_id?: number | null;
}

export interface EmploymentPrediction {
    zipcode: string;
    percent_change: string;
    houses: Array<{
        zpid: string;
    }>;
}