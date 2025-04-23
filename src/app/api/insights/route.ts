import { NextResponse } from 'next/server';
import { pool } from "@/lib/db";
import { ZipInsightData, ClusterInsightData, GeneratedInsight } from "@/lib/types";

const parseSafeFloat = (value: any): number | null => {
    if (value === null || value === undefined) return null;
    const num = parseFloat(String(value));
    return isNaN(num) ? null : num;
}

export async function GET() {
    let client;

    try {
        client = await pool.connect();
        const zipQuery = `
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
        const zipResult = await client.query<ZipInsightData>(zipQuery);
        const zipInsights = zipResult.rows.map(row => ({
            zipcode: row.zipcode, 
            pct_cluster_1: parseSafeFloat(row.pct_cluster_1),
            pct_cluster_2: parseSafeFloat(row.pct_cluster_2),
            pct_cluster_3: parseSafeFloat(row.pct_cluster_3),
            pct_cluster_4: parseSafeFloat(row.pct_cluster_4),
            assigned_cluster: row.assigned_cluster,
            median_price: row.median_price,
            affordability_ratio: row.affordability_ratio, 
            employment_growth: row.employment_growth,
        }));
        const clusterQuery = `
            SELECT
                cluster_id,
                avg_payroll::text,
                median_price::text,
                affordability_ratio,
                employment_growth
            FROM cluster_insights
            WHERE cluster_id IS NOT NULL
            ORDER BY cluster_id;
        `;
        const clusterResult = await client.query<ClusterInsightData>(clusterQuery);
        const clusterInsights = clusterResult.rows.map(row => ({
            cluster_id: row.cluster_id,
            avg_payroll: parseSafeFloat(row.avg_payroll),
            median_price: parseSafeFloat(row.median_price),
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
            insights: zipInsights, 
            clusterInsights: clusterInsights,
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