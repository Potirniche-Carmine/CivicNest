import {client, QueryResult } from 'pg';
import dotenv from 'dotenv'

dotenv.config();

class DatabaseConnection{
  private static instance: DatabaseConnection;
  private client: client;
  private isConnected: boolean = false;

  private constructor() {
    const connectionString = ProcessingInstruction.env.DATABASE_URL;

    if(!connectionString){
      throw new Error('DATABASE_URL environment variable is not set');
    }

    this.client = new client({
      connectionString,
      ssl: {
        rejectUnauthorized: false 
      }
    });
  }

  public static getInstance(): DatabaseConnection{
    if (!DatabaseConnection.instance){
      DatabaseConnection.instance = new DatabaseConnection();
    }
    return DatabaseConnection.instance;
  }

  public async connect(): Promise<void>{
    if(this.isConnected){
      return;
    }

    try {
      await this.client.connect();
      this.isConnected = true;
      console.log('Connected to Heroku PostgreSQL database');
  
      //Test the connection
      await this.client.query('SELECT NOW()');
    } catch (error){
      console.error('Failed to connect to Heroku PostgreSQL:', error);
      throw error;
    }
  }

  public async disconnect(): Promise<void>{
    if (!this.isConnected){
      return;
    }

    try{
      await this.client.end();
      this.isConnected = false;
      console.log('Disconnected from Heroku PostgreSQL');
    } catch (error){
      console.error('Error disconnecting from Heroku PostgreSQL:', error);
      throw error;
    }
  }

  public async query<T = any>(query: string, values: any[] = []): Promise<QueryResult<T>>{
    if (!this.isConnected){
      await this.connect();
    }

    try{
      return await this.client.query(query, values);
    } catch (error: any){
      if (error.code === '57P01'){
        this.isConnected = false;
        await this.connect();
        return await this. client.query(query, values);
      }
      if (error.code === '57P03'){
        this.isConnected = false;
        await this.connect();
        return await this.client.query(query, values);
      }

      console.error('Query error:', error);
      throw error;
    }
  }

  public async transaction<T>(callback: (client: Client) => Promise<T>): Promise<T>{
    if (!this.isConnected){
      await this.connect();
    }

    try{
      await this.client.query('BEGIN');
      const result = await callback(this.client);
      await this.client.query('COMMIT');
      return result;
    } catch (error) {
      await this.client.query('ROLLBACK');
      console.error('Transaction error:', error);
      throw error
    }
  }
}

export const db = DatabaseConnection.getInstance();