import { NextResponse } from 'next/server';
import { queryDatabase } from '../../lib/db';
import NodeCache from 'node-cache';
const cache = new NodeCache();

export async function GET() {
  const cachedData = cache.get('locations');
  if(cachedData){
    return NextResponse.json(cachedData, { status: 200 });
  }
    try {
      // Query the database to get the house locations (latitude and longitude)
      const result = await queryDatabase('SELECT lat, lng FROM your_table WHERE lat IS NOT NULL AND lng IS NOT NULL LIMIT 3');
      cache.set('locations',result.rows,3600);
      // Return the rows from the query as a JSON response
      return NextResponse.json(result.rows, { status: 200 });
  }catch(error){
  return NextResponse.json({message: 'Method Not Allowed' })
  }
}