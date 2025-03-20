import { NextResponse } from 'next/server';
import { pool } from "@/lib/db";

interface Cluster {
    cluster_id: number;
    avg_price: number;
    houses: Array<{
        zpid: string;
        latitude: number;
        longitude: number;
    }>;
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
        
        const clustersMap: Record<string, Cluster> = {};
        result.rows.forEach(row => {
            if (!clustersMap[row.cluster_id]) {
                clustersMap[row.cluster_id] = {
                    cluster_id: row.cluster_id,
                    avg_price: row.cluster_avg_price,
                    houses: []
                };
            }
            
            clustersMap[row.cluster_id].houses.push({
                zpid: row.zpid,
                latitude: row.latitude,
                longitude: row.longitude
            });
        });

        const clusters = Object.values(clustersMap);

        return NextResponse.json({ clusters });
    } catch (err) {
        console.error('Error fetching clusters and houses:', err);

        return NextResponse.json({
            error: 'Database Query Error',
            message: err instanceof Error ? err.message : 'Unknown error',
            details: 'Error retrieving cluster and house data'
        }, { status: 500 });
    } 
}
