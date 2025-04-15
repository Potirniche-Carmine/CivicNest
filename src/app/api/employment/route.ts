import { NextResponse } from 'next/server';
import { pool } from "@/lib/db";
import { EmploymentPrediction } from "@/lib/types";


export async function GET() {
    let client;
    try {
        client = await pool.connect();

        const query = `
            SELECT
                ep.zipcode,
                ep.percent_change,
                h.zpid
            FROM
                employment_prediction ep
            JOIN
                houses h ON ep.zipcode = h.zipcode
            WHERE
                ep.zipcode IS NOT NULL
                AND h.zpid IS NOT NULL
            ORDER BY
                ep.zipcode;
        `;

        const result = await client.query(query);

        const predictionsMap: Record<string, EmploymentPrediction> = {};

        result.rows.forEach(row => {
            const zipcodeStr = String(row.zipcode);

            if (!predictionsMap[zipcodeStr]) {
                predictionsMap[zipcodeStr] = {
                    zipcode: row.zipcode,
                    percent_change: row.percent_change,
                    houses: []
                };
            }


            predictionsMap[zipcodeStr].houses.push({
                zpid: row.zpid
            });
        });

        const employmentPredictions = Object.values(predictionsMap);

        return NextResponse.json({ employmentPredictions });

    } catch (err) {
        console.error('Error fetching employment predictions and houses:', err);

        return NextResponse.json({
            error: 'Database Query Error',
            message: err instanceof Error ? err.message : 'An unknown database error occurred',
            details: 'Failed to retrieve employment prediction data and associated houses.'
        }, { status: 500 });

    } finally {
        if (client) {
            client.release();
        }
    }
}