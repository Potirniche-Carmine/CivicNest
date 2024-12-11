import { Client } from 'pg';

const client = new Client({
  connectionString: process.env.DATABASE_URL,
  ssl: {
    rejectUnauthorized: false,
  },
});

export async function connectToDatabase(){
  try{
    await client.connect();
    console.log('Connected to the database');
  }catch(error){
    console.error('Database connection error:', error);
    process.exit(1);
  }
}

export async function queryDatabase(query: string, values =[]) {
  try {
    const result = await client.query(query, values);
    return result;
  } catch (error) {
    console.error('Query error:', error);
    throw error;
  }
}