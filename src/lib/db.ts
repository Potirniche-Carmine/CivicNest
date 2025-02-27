import { Pool } from 'pg';

export const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
  ssl: {
    rejectUnauthorized: false 
  }
});

// Test function to verify connection
export async function testConnection() {
  try {
    const client = await pool.connect();
    console.log('Database connection successful');
    client.release();
    return { success: true };
  } catch (error) {
    console.error('Database connection error:', error);
    return { success: false, error };
  }
}