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
    console.log("API Route /api/insights GET request received");
    let client;

    try {
        client = await pool.connect();
        console.log("Database client connected.");

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
        console.log("Executing numerical data query...");
        const numericalResult = await client.query<InsightDataFromDB>(numericalQuery);
        const insightsData = numericalResult.rows.map(row => ({
            cluster_id: row.cluster_id, 
            avg_payroll: row.avg_payroll,
            avg_price: row.avg_price,
            affordability_ratio: row.affordability_ratio, 
            employment_growth: row.employment_growth,
        }));
        console.log(`Workspaceed ${insightsData.length} rows of numerical insight data.`);

        const generatedQuery = `
            SELECT insights_content
            FROM generated_market_insights
            ORDER BY generated_at DESC
            LIMIT 1;
        `;
        console.log("Executing generated insights query...");
        const generatedResult = await client.query(generatedQuery);

        let generatedInsights: GeneratedInsight[] = [];
        if (generatedResult.rows.length > 0 && generatedResult.rows[0].insights_content) {
            try {
                generatedInsights = generatedResult.rows[0].insights_content;
                if (!Array.isArray(generatedInsights) || !generatedInsights.every(item => item.title && item.explanation)) {
                    console.warn("Cached generated insights format is invalid, falling back to empty array.");
                    generatedInsights = [];
                } else {
                     console.log(`Retrieved ${generatedInsights.length} cached generated insights.`);
                }
            } catch (parseError) {
                console.error("Error processing cached generated insights from DB:", parseError);
                generatedInsights = []; 
            }
        } else {
            console.log("No cached generated insights found in the database.");
        }

        client.release();
        console.log("Database client released.");

        return NextResponse.json({
            insights: insightsData, 
            generatedInsights: generatedInsights, 
        });

    } catch (err: unknown) {
        if (client) {
            client.release();
            console.log("Database client released after error.");
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