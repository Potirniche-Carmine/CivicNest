import pool from '../../api/db';

export default async function handler(req, res){
  try{
    const client = await pool.connect();
    const result = await client.query('SELECT latitude, longitude FROM houses');
    client.release();
    res.status(200).json(result.rows);
  }
}
