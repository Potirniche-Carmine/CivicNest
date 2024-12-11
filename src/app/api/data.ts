import { NextApiRequest, NextApiResponse } from 'next';
import pool from '@/app/api/db'; // Assuming db.ts is in 'app/api'

export default async function handler(req: NextApiRequest, res: NextApiResponse) {
  console.log("Received request at /api/data");

  try {
    const client = await pool.connect();
    console.log("Connected to database");

    const result = await client.query('SELECT lat, long, price FROM houses');
    console.log("Query result:", result.rows);

    client.release();
    res.status(200).json(result.rows);
  } catch (error) {
    console.error("Error in /api/data:", error);
    res.status(500).json({ error: 'Internal Server Error' });
  }
}
