import { NextResponse } from 'next/server';
import { pool } from '@/lib/db';

export async function GET() {
  let client; 

  try {
    client = await pool.connect();

    const query = `
      SELECT
        zip_code,
        ST_AsGeoJSON(boundary) as geometry_geojson
      FROM zip_code_boundaries;
    `;
    const result = await client.query(query);

    const features = result.rows.map(row => {
      let geometry = null;
      try {
        if (row.geometry_geojson) {
          geometry = JSON.parse(row.geometry_geojson);
        } else {
           console.warn(`Warning: Null or empty geometry found for ZIP code ${row.zip_code}`);
        }
      } catch (parseError) {
        console.error(`Error parsing GeoJSON geometry for ZIP code ${row.zip_code}:`, parseError);
        return null; 
      }

      return {
        type: 'Feature',
        geometry: geometry, 
        properties: {
          zip_code: row.zip_code,
        },
      };
    }).filter(feature => feature !== null && feature.geometry !== null); 

    const featureCollection = {
      type: 'FeatureCollection',
      features: features,
    };

    return NextResponse.json(featureCollection);

  } catch (err) {
    console.error('Error fetching ZIP code boundaries:', err);

    return NextResponse.json({
      error: 'Failed to fetch ZIP code boundaries',
      message: err instanceof Error ? err.message : 'An unknown error occurred',
    }, { status: 500 });

  } finally {
    if (client) {
      client.release();
    }
  }
}