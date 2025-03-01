import { NextResponse } from 'next/server';
import { pool } from "@/lib/db";

export async function POST(request: Request){
    try{
        const body = await request.json();
        const { latitude, longitude} = body;

        if(!latitude){
            return NextResponse.json({ error: 'Latitude is Required'}, { status: 400});
        }

        const query = `
        SELECT latitude, longitude FROM cluster_table WHERE latitude IS NOT NULL AND longitude IS NOT NULL LIMIT 3`;
        const values = [latitude, longitude || null];

        const result = await pool.query(query, values);

        const cluster_table = result.rows[0];

        return NextResponse.json({ cluster_table}, { status: 201});
    } catch (err){
        console.error('Error in Post /api/clusters:', err);
        return NextResponse.json({ error: 'Internal Server Error'}, { status: 500});
    }
}

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