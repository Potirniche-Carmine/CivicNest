import { Pool } from 'pg';

// Create a connection pool using your Heroku or local database URL
const pool = new Pool({
  connectionString: process.env.DATABASE_URL, // Make sure to set DATABASE_URL in your .env
  ssl: {
    rejectUnauthorized: false,
  },
});

export default pool;