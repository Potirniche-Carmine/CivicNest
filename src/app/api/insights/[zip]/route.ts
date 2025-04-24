import { NextResponse } from 'next/server';
import { pool } from "@/lib/db";
import type { NextRequest } from 'next/server';

const parseSafeFloat = (value: any): number | null => {
    if (value === null || value === undefined) return null;
    const num = parseFloat(String(value));
    return isNaN(num) ? null : num;
}

const parseSafeInt = (value: any): number | null => {
    if (value === null || value === undefined) return null;
    const num = parseInt(String(value), 10);
    return isNaN(num) ? null : num;
}

export async function GET(
    request: NextRequest,
    { params }: { params: Promise<{ zip: string }> }
) {
    const zip = (await params).zip;
    let client;

    if (!zip || typeof zip !== 'string' || !/^\d{5}$/.test(zip)) {
        return NextResponse.json({ error: 'Invalid or missing zip code format. Requires 5 digits.' }, { status: 400 });
    }

    try {
        client = await pool.connect();

        const nonCensusQuery = `
        SELECT
            col_index,        
            median_age,
            enrollment,
            num_of_schools,          
            schools_rated_1_or_2,  
            num_of_1_or_2_es,      
            num_of_1_or_2_ms,     
            num_of_1_or_2_hs      
        FROM non_census_data
        WHERE zipcode = $1;
    `;

        const generatedInsightsQuery = `
        SELECT
            insights_content 
        FROM generated_zipcode_insights
        WHERE zipcode = $1
        ORDER BY generated_at DESC -- Get the most recent entry
        LIMIT 1; 
    `;

        const [nonCensusResult, generatedInsightsResult] = await Promise.all([
            client.query(nonCensusQuery, [zip]),
            client.query(generatedInsightsQuery, [zip])
        ]);

        if (nonCensusResult.rows.length === 0) {
            client.release();
            return NextResponse.json({ error: `Core demographic/school data not found for zip code ${zip}.` }, { status: 404 });
        }
        const nonCensusData = nonCensusResult.rows[0];
        
        let generatedInsights = [];
        if (generatedInsightsResult.rows.length > 0 && generatedInsightsResult.rows[0].insights_content) {
            try {
                const content = typeof generatedInsightsResult.rows[0].insights_content === 'string' 
                    ? JSON.parse(generatedInsightsResult.rows[0].insights_content)
                    : generatedInsightsResult.rows[0].insights_content;
                
                if (Array.isArray(content)) {
                    generatedInsights = content;
                } else {
                    console.warn("Unexpected format for insights_content:", content);
                    generatedInsights = [];
                }
            } catch (parseError) {
                console.error("Error parsing insights_content:", parseError);
                generatedInsights = [];
            }
        }

        const responseData = {
            zipcodeDetails: {
                col_index: parseSafeFloat(nonCensusData.col_index),
                demographics: {
                    median_age: parseSafeFloat(nonCensusData.median_age),
                    school_enrollment_total: parseSafeInt(nonCensusData.enrollment),
                },
                schoolRatings: {
                    poorly_rated_elementary: parseSafeInt(nonCensusData.num_of_1_or_2_es),
                    poorly_rated_middle: parseSafeInt(nonCensusData.num_of_1_or_2_ms),
                    poorly_rated_high: parseSafeInt(nonCensusData.num_of_1_or_2_hs),
                },
            },
            generatedInsights: generatedInsights, 
        };

        client.release();
        return NextResponse.json(responseData, { status: 200 });

    } catch (err: unknown) {
        if (client) {
            client.release();
        }
        console.error(`Error in /api/insights/${zip} route:`, err);
        const errorDetails = (err instanceof Error) ? err.message : 'Unknown server error occurred.';
        return NextResponse.json({
            error: `Failed to fetch insights for zip code ${zip}`,
            message: 'An error occurred while processing your request.',
            details: errorDetails,
        }, { status: 500 });
    }
}