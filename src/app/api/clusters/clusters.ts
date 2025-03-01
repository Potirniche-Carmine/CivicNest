import { NextResponse } from 'next/server';
import { pool } from "@/lib/db";

export async function GET() {
    try{
        const client = await pool.connect();

        const query = `
        SELECT cluster_id, id, latitude, longitude
        FROM cluster_table
        WHERE latitude IS NOT NULL AND longitude IS NOT NULL
        ORDER BY cluster_id`;

        const result = await client.query(query);
        client.release();

        return NextResponse.json({ cluster_table: result.rows });
    } catch (err){
        console.error('Error fetching clusters:', err);

        //More detailed error response
        return NextResponse.json({
            error: 'Database Connection Error',
            message: err instanceof Error ? err.message : 'Unknown error',
            details: 'Check your database configuration and environment variables'
        }, { status: 500});
    } 
}