import { NextResponse } from 'next/server';
import { pool } from "@/lib/db";

interface InsightDataFromDB {
    zipcode: number;
    pct_cluster_1: string;
    pct_cluster_2: string;
    pct_cluster_3: string;
    pct_cluster_4: string;
    assigned_cluster: number;
    median_price: string;
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
                zipcode,
                pct_cluster_1,
                pct_cluster_2,
                pct_cluster_3,
                pct_cluster_4,  
                assigned_cluster,   
                median_price,
                affordability_ratio,
                employment_growth
            FROM final_insights_table    
            WHERE zipcode IS NOT NULL
            ORDER BY zipcode;
        `;
        const numericalResult = await client.query<InsightDataFromDB>(numericalQuery);
        const insightsData = numericalResult.rows.map(row => ({
            zipcode: row.zipcode, 
            pct_cluster_1: parseFloat(row.pct_cluster_1),
            pct_cluster_2: parseFloat(row.pct_cluster_2),
            pct_cluster_3: parseFloat(row.pct_cluster_3),
            pct_cluster_4: parseFloat(row.pct_cluster_4),
            assigned_cluster: row.assigned_cluster,
            median_price: row.median_price,
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