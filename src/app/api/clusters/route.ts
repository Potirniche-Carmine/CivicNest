import { NextResponse } from 'next/server';
import { pool } from "@/lib/db";

interface House {
    zpid: string;
    lat: number;
    long: number;
    bathrooms: string;
    bedrooms: string;
}
interface Cluster {
    cluster_id: number;
    display_name: string;
    avg_price: number;
    houses: House[];
}

function formatCurrency(price: number | null | undefined): string {
    if (price == null) {
        return 'N/A'; 
    }
    const numericPrice = Number(price);
     if (isNaN(numericPrice)) {
        return 'Invalid Price'; 
    }
    return numericPrice.toLocaleString('en-US', {
        style: 'currency',
        currency: 'USD',
        maximumFractionDigits: 0,
        minimumFractionDigits: 0,
    });

}

export async function GET() {
    try {
        const client = await pool.connect();

        const query = `
        SELECT 
            h.zpid, 
            h.lat, 
            h.long,
            h.bedrooms,
            h.bathrooms,
            ct.cluster_id,
            cc.price as cluster_avg_price
        FROM 
            houses h
        JOIN 
            cluster_table ct ON h.zpid = ct.zpid
        JOIN 
            cluster_centroids cc ON ct.cluster_id = cc.cluster_id
        WHERE 
            h.lat IS NOT NULL AND h.long IS NOT NULL
        ORDER BY 
            ct.cluster_id
        `;

        const result = await client.query(query);
        client.release();
        
        const clustersMap: Record<number, Cluster> = {};

        result.rows.forEach(row => {
            const clusterId: number = row.cluster_id;

            if (!clustersMap[clusterId]) {
                clustersMap[clusterId] = {
                    cluster_id: clusterId, 
                    display_name: `Cluster ${formatCurrency(row.cluster_avg_price)}`,
                    avg_price: row.cluster_avg_price, 
                    houses: [] 
                };
            }

            clustersMap[clusterId].houses.push({
                zpid: row.zpid,
                lat: row.lat,
                long: row.long,
                bathrooms: row.bathrooms,
                bedrooms: row.bedrooms
            });
        });

        const clusters: Cluster[] = Object.values(clustersMap);

        return NextResponse.json({ clusters });

    } catch (err) {
        console.error('Error fetching clusters and houses:', err);

        const message = err instanceof Error ? err.message : 'An unknown error occurred';

        return NextResponse.json({
            error: 'Database Query Error',
            message: message, 
            details: 'Error retrieving cluster and house data',
        }, { status: 500 });
    }
}