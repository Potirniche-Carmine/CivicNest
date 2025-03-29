export interface houses {
    zpid: number;
    address: string;
    lat: number;
    long: number;
    price: number;
    bedrooms: number;
    bathrooms: number;
    cluster_id?: number | null;
}