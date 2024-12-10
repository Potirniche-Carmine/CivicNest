import { Pool } from "pg"; 

const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
});

export default async function handler(req, res){
  try{
    const {rows} = await pool.query(
      "SELECT lat, long, price FROM houses"
    );
    res.status(200).json(rows);
  }
}
