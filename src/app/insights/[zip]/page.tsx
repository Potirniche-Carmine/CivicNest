'use client';

import React, { useState, useEffect } from 'react';
import { useParams } from 'next/navigation';
import {
  Card,
  CardContent,
  CardHeader,
  CardTitle,
} from "@/components/ui/card";
import { Separator } from "@/components/ui/separator";
import { Loader2, AlertTriangle, Users, School, MapPin, BrainCircuit, DollarSign, TrendingUp, TrendingDown, Home, Info } from 'lucide-react';
import { ZipcodeSpecificData, GeneratedZipInsight } from "@/lib/types";
import { ZipcodeMap } from '@/components/zipcodemap';

const RENO_COL_MIN = 94.5;
const RENO_COL_MAX = 103.0;
const NATIONAL_COL_AVG = 100.0;

export default function ZipcodePage() {
  const params = useParams();
  const zip = params?.zip as string;

  const [zipcodeData, setZipcodeData] = useState<ZipcodeSpecificData | null>(null);
  const [generatedInsights, setGeneratedInsights] = useState<GeneratedZipInsight[]>([]);
  const [isLoading, setIsLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);
  const [, setMapKey] = useState<number>(0);

  useEffect(() => {
    if (!zip) return;

    const fetchZipcodeDetails = async () => {
      setIsLoading(true);
      setError(null);
      setZipcodeData(null);
      setGeneratedInsights([]);

      try {
        const response = await fetch(`/api/insights/${zip}`);

        if (!response.ok) {
          let errorMsg = `API Error: ${response.status} ${response.statusText}`;
          try {
            const errorData = await response.json();
            errorMsg = errorData.error || errorData.message || errorMsg;
          } catch (parseError) { }
          throw new Error(errorMsg);
        }

        const data = await response.json();

        if (!data.zipcodeDetails || typeof data.zipcodeDetails !== 'object') {
          throw new Error("Invalid zip code data format received (missing zipcodeDetails).");
        }
        if (!data.zipcodeDetails.demographics || !data.zipcodeDetails.schoolRatings) {
          throw new Error("Invalid zip code data format received (missing demographics or schoolRatings).");
        }

        setZipcodeData(data.zipcodeDetails as ZipcodeSpecificData);

        if (data.generatedInsights && Array.isArray(data.generatedInsights)) {
          setGeneratedInsights(data.generatedInsights);
        } else {
          console.warn("Generated zip code insights missing or not an array.");
          setGeneratedInsights([]);
        }

        setMapKey(prev => prev + 1);

      } catch (err: unknown) {
        console.error(`Failed to fetch data for zip code ${zip}:`, err);
        const errorMessage = (err instanceof Error) ? err.message : "An unknown error occurred.";
        setError(errorMessage);
      } finally {
        setIsLoading(false);
      }
    };

    fetchZipcodeDetails();
  }, [zip]);

  const formatNumber = (value: number | null | undefined): string => {
    if (value === null || value === undefined) return 'N/A';
    return value.toLocaleString('en-US');
  }

  const formatAge = (value: number | null | undefined): string => {
    if (value === null || value === undefined) return 'N/A';
    return `${value.toFixed(1)} years`;
  }

  const formatColIndex = (value: number | null | undefined): string => {
    if (value === null || value === undefined) return 'N/A';
    return value.toFixed(1);
  }

  const getColStyle = (colIndex: number | null | undefined): { className: string; Icon: React.ElementType } => {
    if (colIndex === null || colIndex === undefined) {
      return { className: 'text-muted-foreground font-medium', Icon: DollarSign };
    }
    const range = RENO_COL_MAX - RENO_COL_MIN;
    const normalized = range > 0 ? Math.max(0, Math.min(1, (colIndex - RENO_COL_MIN) / range)) : 0.5;

    let className = 'font-bold';
    let Icon = DollarSign;

    if (normalized <= 0.20) { className += ' text-emerald-600 dark:text-emerald-400'; Icon = TrendingDown; }
    else if (normalized <= 0.40) { className += ' text-green-600 dark:text-green-400'; Icon = TrendingDown; }
    else if (normalized <= 0.60) { className += ' text-yellow-600 dark:text-yellow-400'; Icon = DollarSign; }
    else if (normalized <= 0.80) { className += ' text-orange-600 dark:text-orange-400'; Icon = TrendingUp; }
    else { className += ' text-blue-700 dark:text-blue-500'; Icon = TrendingUp; }

    return { className, Icon };
  };

  if (isLoading) {
    return (
      <main className="flex-1 bg-background min-h-screen flex items-center justify-center">
        <div className="flex flex-col items-center text-muted-foreground">
          <Loader2 className="h-10 w-10 animate-spin mb-4" />
          <p className="text-lg">Loading Zip Code Details for {zip}...</p>
        </div>
      </main>
    );
  }

  if (error) {
    return (
      <main className="flex-1 bg-background min-h-screen flex items-center justify-center">
        <div className="bg-destructive/10 border border-destructive/30 text-destructive p-6 rounded-lg max-w-md text-center">
          <AlertTriangle className="h-8 w-8 mx-auto mb-4 text-destructive" />
          <h2 className="text-xl font-semibold mb-2">Failed to Load Data for Zip {zip}</h2>
          <p className="text-sm mb-4">{error}</p>
          <p className="text-xs text-muted-foreground">Please try refreshing the page or check if the zip code is valid.</p>
        </div>
      </main>
    );
  }

  if (!zipcodeData) {
    return (
      <main className="flex-1 bg-background min-h-screen flex items-center justify-center">
        <p className="text-muted-foreground">No data available for zip code {zip}.</p>
      </main>
    )
  }

  const colIndexValue = zipcodeData.col_index;
  const { className: colClassName, Icon: ColIcon } = getColStyle(colIndexValue);

  return (
    <main className="flex-1 bg-background min-h-screen">
      <div className="container mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <h1 className="text-3xl md:text-4xl font-bold mb-8 px-3 py-3 bg-gradient-to-r from-blue-600 to-sky-600 inline-block text-transparent bg-clip-text">
          Market Details: Zip Code {zip}
        </h1>

        <section className="mb-8">
          <div className="flex items-center mb-6">
            <Home className="mr-3 text-sky-500 dark:text-sky-400" size={24} />
            <h2 className="text-2xl font-semibold">Key Statistics</h2>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          <Card className="shadow-lg border-border overflow-hidden h-full dark:!bg-[#020817]">
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2 bg-background">
                <CardTitle className="text-lg font-semibold">Demographics</CardTitle>
                <Users className="h-5 w-5 text-sky-500 dark:text-sky-400" />
              </CardHeader>
              <CardContent className="space-y-3 pt-4 bg-background flex-1 pb-6">
                <div className="flex justify-between items-center">
                  <span className="text-muted-foreground text-sm">Median Age:</span>
                  <span className="font-medium">{formatAge(zipcodeData.demographics.median_age)}</span>
                </div>
                <Separator />
                <div className="flex justify-between items-center">
                  <span className="text-muted-foreground text-sm">Total School Enrollment:</span>
                  <span className="font-medium">{formatNumber(zipcodeData.demographics.school_enrollment_total)}</span>
                </div>
              </CardContent>
            </Card>

            <Card className="shadow-lg border-border overflow-hidden h-full dark:!bg-[#020817]">
            <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2 bg-background">
                <CardTitle className="text-lg font-semibold">Poorly Rated Schools</CardTitle>
                <School className="h-5 w-5 text-sky-500 dark:text-sky-400" />
              </CardHeader>
              <CardContent className="space-y-3 pt-4 bg-background">
                <div className="flex justify-between items-center">
                  <span className="text-muted-foreground text-sm">Elementary:</span>
                  <span className="font-medium">{formatNumber(zipcodeData.schoolRatings.poorly_rated_elementary)}</span>
                </div>
                <Separator />
                <div className="flex justify-between items-center">
                  <span className="text-muted-foreground text-sm">Middle:</span>
                  <span className="font-medium">{formatNumber(zipcodeData.schoolRatings.poorly_rated_middle)}</span>
                </div>
                <Separator />
                <div className="flex justify-between items-center">
                  <span className="text-muted-foreground text-sm">High:</span>
                  <span className="font-medium">{formatNumber(zipcodeData.schoolRatings.poorly_rated_high)}</span>
                </div>
                <div className="text-xs pt-2 text-muted-foreground flex items-start mt-2">
                  <Info className="mr-2 mt-0.5 flex-shrink-0" size={14} />
                  <span>Count of schools with low performance ratings (e.g., rated 1 or 2).</span>
                </div>
              </CardContent>
            </Card>

            <Card className="shadow-lg border-border overflow-hidden h-full dark:!bg-[#020817]">
            <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2 bg-background">
                <CardTitle className="text-lg font-semibold">Cost of Living</CardTitle>
                <ColIcon className={`h-5 w-5 ${colIndexValue === null || colIndexValue === undefined ? 'text-muted-foreground' : colClassName.split(' ').find(c => c.startsWith('text-'))}`} />
              </CardHeader>
              <CardContent className="space-y-3 pt-4 bg-background">
                <div className="flex justify-between items-center">
                  <span className="text-muted-foreground text-sm">COL Index:</span>
                  <span className={colClassName}>
                    {formatColIndex(colIndexValue)}
                  </span>
                </div>
                <Separator />
                <div className="flex justify-between items-center">
                  <span className="text-muted-foreground text-sm">Compared to National:</span>
                  <span className={colClassName}>
                    {colIndexValue !== null && colIndexValue !== undefined
                      ? `${(colIndexValue - NATIONAL_COL_AVG).toFixed(1)} pts`
                      : 'N/A'}
                  </span>
                </div>
                <div className="text-xs pt-2 text-muted-foreground flex items-start mt-2">
                  <Info className="mr-2 mt-0.5 flex-shrink-0" size={14} />
                  <span>Relative to US average ({NATIONAL_COL_AVG.toFixed(1)}). Lower is cheaper. Reno area range: {RENO_COL_MIN}-{RENO_COL_MAX}.</span>
                </div>
              </CardContent>
            </Card>
          </div>
        </section>

        <section className="mb-8">
          <div className="flex items-center mb-6">
            <MapPin className="mr-3 text-sky-500 dark:text-sky-400" size={24} />
            <h2 className="text-2xl font-semibold">Location Map {zip}</h2>
          </div>
          <div className="w-full h-96 md:h-[500px] bg-muted rounded-lg shadow-lg border border-border overflow-hidden">
            <ZipcodeMap zipcode={zip} />
          </div>
        </section>

        <section className="mb-12">
          <div className="flex items-center mb-6">
            <BrainCircuit className="mr-3 text-sky-500 dark:text-sky-400" size={24} />
            <h2 className="text-2xl font-semibold">AI-Generated Market Analysis</h2>
          </div>
          <Card className="border border-border overflow-hidden shadow-sm dark:shadow-none bg-background">
            <CardContent className="p-6 bg-background">

              {generatedInsights.length > 0 ? (
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                  {generatedInsights.map((insight, index) => (
                    <div
                      key={index}
                      className={`p-4 rounded-lg border ${index % 4 === 0 ? 'bg-blue-50/50 dark:bg-blue-900/20 border-blue-200 dark:border-blue-800' :
                        index % 4 === 1 ? 'bg-emerald-50/50 dark:bg-emerald-900/20 border-emerald-200 dark:border-emerald-800' :
                          index % 4 === 2 ? 'bg-amber-50/50 dark:bg-amber-900/20 border-amber-200 dark:border-amber-800' :
                            'bg-purple-50/50 dark:bg-purple-900/20 border-purple-200 dark:border-purple-800'
                        }`}
                    >
                      <h3
                        className={`font-semibold mb-2 ${index % 4 === 0 ? 'text-blue-700 dark:text-blue-300' :
                          index % 4 === 1 ? 'text-emerald-700 dark:text-emerald-300' :
                            index % 4 === 2 ? 'text-amber-700 dark:text-amber-300' :
                              'text-purple-700 dark:text-purple-300'
                          }`}
                        dangerouslySetInnerHTML={{ __html: insight.title || `Market Insight ${index + 1}` }}
                      />
                      {insight.explanation ? (
                        <div
                          className="text-foreground/90 text-sm space-y-2"
                          dangerouslySetInnerHTML={{ __html: insight.explanation }}
                        />
                      ) : (
                        <p className="text-muted-foreground italic text-sm">No detailed explanation available.</p>
                      )}
                    </div>
                  ))}
                </div>
              ) : (
                <div className="text-center py-8">
                  <p className="text-muted-foreground mb-3">No AI-generated insights are currently available for zip code {zip}.</p>
                  <p className="text-sm text-muted-foreground">Check back later as our AI continues to analyze this market area.</p>
                </div>
              )}
            </CardContent>
          </Card>
        </section>
      </div>
    </main>
  );
}