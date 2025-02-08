import { NextResponse } from 'next/server';
import { pool } from '@/app/lib/db';

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
  try{const query = `
    SELECT address, lat, long, price, zpid
    FROM houses
    ORDER BY address`;

    const result = await pool.query(query);
    return NextResponse.json({ houses: result.rows});
}   catch (err) {
    console.error('Error fetching locations:', err);
    return NextResponse.json({error: 'Internal Server Error' }, { status: 500 });
}
  
}