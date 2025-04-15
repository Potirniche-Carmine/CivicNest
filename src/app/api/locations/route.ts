import { NextResponse } from 'next/server';
import { pool } from '@/lib/db';

export async function POST(request: Request){
    try{
        const body = await request.json();
        const { lat, long} = body;

        if (!lat){
            return NextResponse.json({ error: 'Latitude is required'}, { status: 400});
        }

        const query = `
        SELECT lat, long FROM houses WHERE lat IS NOT NULL AND long IS NOT NULL LIMIT 3`;
        const values = [lat, long || null];

        const result = await pool.query(query, values);

        const houses = result.rows[0];

        return NextResponse.json({ houses}, { status: 201});
    } catch (err) {
        console.error('Error in Post /api/locations:', err);
        return NextResponse.json({ error: 'Internal Server Error'}, { status: 500 });
    }
}

export async function GET() {
    try {
        // First, let's try to establish a connection using our test function
        const client = await pool.connect();
        
        const query = `
            SELECT address, lat, long, price, zpid, zipcode 
            FROM houses 
            WHERE lat IS NOT NULL AND long IS NOT NULL
            ORDER BY address`;

        const result = await client.query(query);
        client.release();
        
        return NextResponse.json({ houses: result.rows });
    } catch (err) {
        console.error('Error fetching locations:', err);
        
        // More detailed error response
        return NextResponse.json({
            error: 'Database Connection Error',
            message: err instanceof Error ? err.message : 'Unknown error',
            details: 'Check your database configuration and environment variables'
        }, { status: 500 });
    }
}