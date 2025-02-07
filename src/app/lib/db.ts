import { Pool } from 'pg';

const pool = new Pool({
  connectionString: ProcessingInstruction.env.DATABASE_URL,
});

export { pool };