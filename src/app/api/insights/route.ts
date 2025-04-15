import { NextResponse } from 'next/server';
import { pool } from "@/lib/db";

interface InsightDataFromDB {
    cluster_id: number;
    avg_payroll: string;
    avg_price: string;
    affordability_ratio: number;
    employment_growth: string; 
}

interface GeneratedInsight {
    title: string;
    explanation: string;
}

export async function GET() {
    let client;

    try {
        client = await pool.connect();
        const numericalQuery = `
            SELECT
                cluster_id,
                avg_payroll::text,  
                avg_price::text,   
                affordability_ratio,
                employment_growth   
            FROM insights_table    
            WHERE cluster_id IS NOT NULL
            ORDER BY cluster_id;
        `;
        const numericalResult = await client.query<InsightDataFromDB>(numericalQuery);
        const insightsData = numericalResult.rows.map(row => ({
            cluster_id: row.cluster_id, 
            avg_payroll: row.avg_payroll,
            avg_price: row.avg_price,
            affordability_ratio: row.affordability_ratio, 
            employment_growth: row.employment_growth,
        }));
        const generatedQuery = `
            SELECT insights_content
            FROM generated_market_insights
            ORDER BY generated_at DESC
            LIMIT 1;
        `;
        const generatedResult = await client.query(generatedQuery);

        let generatedInsights: GeneratedInsight[] = [];
        if (generatedResult.rows.length > 0 && generatedResult.rows[0].insights_content) {
            try {
                generatedInsights = generatedResult.rows[0].insights_content;
                if (!Array.isArray(generatedInsights) || !generatedInsights.every(item => item.title && item.explanation)) {
                    console.warn("Cached generated insights format is invalid, falling back to empty array.");
                    generatedInsights = [];
                } else {
                }
            } catch (parseError) {
                console.error("Error processing cached generated insights from DB:", parseError);
                generatedInsights = []; 
            }
        } else {
        }

        client.release();
        return NextResponse.json({
            insights: insightsData, 
            generatedInsights: generatedInsights, 
        });

    } catch (err: unknown) {
        if (client) {
            client.release();
        }
        console.error('Error in /api/insights route:', err);

        const errorDetails = (err instanceof Error) ? err.message : 'Unknown server error';

        return NextResponse.json({
            error: 'Failed to fetch market insights',
            message: 'An error occurred while processing your request.',
            details: errorDetails, 
        }, { status: 500 });
    }
}