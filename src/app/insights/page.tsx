'use client'

import React, { useState, useEffect, useMemo } from 'react';
import Link from 'next/link';
import { Button } from '@/components/ui/button';
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table";
import { TrendingUp, Home, BarChart2, Info, Loader2, AlertTriangle } from 'lucide-react';
import { ZipInsightData, ClusterInsightData, GeneratedInsight } from '@/lib/types';

export default function Insights() {
  const [zipInsightsData, setzipInsightsData] = useState<ZipInsightData[]>([]);
  const [clusterInsightsData, setClusterInsightsData] = useState<ClusterInsightData[]>([]);
  const [generatedInsights, setGeneratedInsights] = useState<GeneratedInsight[]>([]);
  const [isLoading, setIsLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchCombinedData = async () => {
      setIsLoading(true);
      setError(null);
      setzipInsightsData([]);
      setClusterInsightsData([]);
      setGeneratedInsights([]);
      try {
        const response = await fetch('/api/insights');

        if (!response.ok) {
          let errorMsg = `API Error: ${response.status} ${response.statusText}`;
          try {
            const errorData = await response.json();
            errorMsg = errorData.error || errorData.message || errorMsg;
          } catch (parseError) { }
          throw new Error(errorMsg);
        }

        const data = await response.json();

        if (!data.insights || !Array.isArray(data.insights)) {
          throw new Error("Invalid numerical insight data format received.");
        }
        if (!data.generatedInsights || !Array.isArray(data.generatedInsights)) {
          console.warn("Generated insights missing or not an array in response, displaying empty.");
          data.generatedInsights = [];
        }

        setzipInsightsData(data.insights);
        setClusterInsightsData(data.clusterInsights);
        setGeneratedInsights(data.generatedInsights);

      } catch (err: unknown) {
        console.error("Failed to fetch market data:", err);
        const errorMessage = (err instanceof Error) ? err.message : "An unknown error occurred while fetching data.";
        setError(errorMessage);
      } finally {
        setIsLoading(false);
      }
    };

    fetchCombinedData();
  }, []);

  const clusterPriceMap = useMemo(() => {
    const map = new Map<number, string>();
    clusterInsightsData.forEach(cluster => {
      map.set(cluster.cluster_id, cluster.median_price);
    });
    return map;
  }, [clusterInsightsData]);

  if (isLoading) {
    return (
      <main className="flex-1 bg-background min-h-screen flex items-center justify-center">
        <div className="flex flex-col items-center text-muted-foreground">
          <Loader2 className="h-10 w-10 animate-spin mb-4" />
          <p className="text-lg">Loading Market Insights...</p>
        </div>
      </main>
    );
  }

  if (error) {
    return (
      <main className="flex-1 bg-background min-h-screen flex items-center justify-center">
        <div className="bg-destructive/10 border border-destructive/30 text-destructive p-6 rounded-lg max-w-md text-center">
          <AlertTriangle className="h-8 w-8 mx-auto mb-4 text-destructive" />
          <h2 className="text-xl font-semibold mb-2">Failed to Load Data</h2>
          <p className="text-sm mb-4">{error}</p>
          <p className="text-xs text-muted-foreground">Please try refreshing the page or contact support.</p>
        </div>
      </main>
    );
  }

  const formatCurrency = (value: string | number | null | undefined): string => {
    if (value === null || value === undefined) return 'N/A';
    try {
      const numericString = String(value).replace(/[^0-9.-]+/g, '');
      const number = parseFloat(numericString);
      if (isNaN(number)) return String(value);
      return `$${number.toLocaleString('en-US', { maximumFractionDigits: 0 })}`;
    } catch (error) {
      console.error("Error formatting currency:", error, "Value:", value);
      return String(value);
    }
  };

  const approxRowHeight = 50;
  const maxVisibleRows = 7;
  const tableMaxHeight = approxRowHeight * maxVisibleRows;


  return (
    <main className="flex-1 bg-background min-h-screen">
      <div className="container mx-auto px-4 py-4">
        <h1 className="text-4xl font-bold mb-8 px-3 py-3 bg-gradient-to-r from-blue-600 to-sky-600 inline-block text-transparent bg-clip-text">
          Market Insights
        </h1>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-8 mb-12">
          <section className="p-6 rounded-xl bg-card shadow-lg border border-border">
            <div className="flex items-center mb-4">
              <Home className="mr-3 text-sky-500 dark:text-sky-400" size={24} />
              <h2 className="text-2xl font-semibold">Zip Code Cluster Insights</h2>
            </div>
            <div className="flex-grow overflow-hidden">
              <div className="overflow-y-auto" style={{ maxHeight: `${tableMaxHeight}px` }}>
                <Table className="w-full border-collapse">
                  <TableHeader className="sticky top-0 bg-card z-10 shadow-sm">
                    <TableRow className="border-b border-border">
                      <TableHead className="py-3 px-4 text-left font-semibold text-primary">Zip Code</TableHead>
                      <TableHead className="py-3 px-4 text-left font-semibold text-primary">Average House Price</TableHead>
                      <TableHead className="py-3 px-4 text-left font-semibold text-primary">Dominant Cluster</TableHead>
                      <TableHead className="py-3 px-4 text-left font-semibold text-primary">Affordability Ratio</TableHead>
                    </TableRow>
                  </TableHeader>
                  <TableBody>
                    {zipInsightsData.length > 0 ? zipInsightsData.map((item) => {
                      let ratioColorClass = "";
                      const ratio = item.affordability_ratio;
                      if (ratio === null) ratioColorClass = "text-muted-foreground";
                      else if (ratio >= 0.12) ratioColorClass = "text-emerald-600 dark:text-emerald-400 font-medium";
                      else if (ratio >= 0.08) ratioColorClass = "text-amber-600 dark:text-amber-400 font-medium";
                      else ratioColorClass = "text-rose-600 dark:text-rose-400 font-medium";

                      const clusterPrice = clusterPriceMap.get(item.assigned_cluster);
                      const dominantClusterDisplay = clusterPrice !== undefined
                        ? `Cluster ${formatCurrency(clusterPrice)}`
                        : `ID: ${item.assigned_cluster}`;

                      return (
                        <TableRow
                          key={`zip-${item.zipcode}`}
                          className="border-b border-border transition-colors hover:bg-primary/5 dark:hover:bg-primary/10 cursor-pointer group relative"
                          onClick={() => window.location.href = `/insights/${item.zipcode}`}
                        >
                          <TableCell className="py-3 px-4 font-medium">
                            <div className="flex items-center">
                              <span className="text-primary group-hover:text-primary/80 group-hover:underline">
                                {item.zipcode}
                              </span>
                              <span className="ml-2 opacity-0 group-hover:opacity-100 transition-opacity text-primary">
                                →
                              </span>
                            </div>
                          </TableCell>
                          <TableCell className="py-3 px-4">{formatCurrency(item.median_price)}</TableCell>
                          <TableCell className="py-3 px-4">{dominantClusterDisplay}</TableCell>
                          <TableCell className={`py-3 px-4 ${ratioColorClass}`}>
                            {ratio !== null && ratio !== undefined ? Number(ratio).toFixed(3) : 'N/A'}
                          </TableCell>
                        </TableRow>
                      );
                    }) : (
                      <TableRow>
                        <TableCell colSpan={4} className="py-8 text-center text-muted-foreground">
                          <div className="flex flex-col items-center justify-center space-y-2">
                            <span className="text-lg">No zip code data available</span>
                            <span className="text-sm text-muted-foreground">Try adjusting your filters or importing data</span>
                          </div>
                        </TableCell>
                      </TableRow>
                    )}
                  </TableBody>
                </Table>
              </div>
            </div>

            <div className="mt-4 text-sm text-muted-foreground flex items-start">
              <Info className="mr-2 mt-0.5 flex-shrink-0" size={14} />
              <p>Affordability: Green (Better), Yellow (Average), Red (Worse).</p>
            </div>
          </section>

          <section className="p-6 rounded-xl bg-card shadow-lg border border-border">
            <div className="flex items-center mb-4">
              <TrendingUp className="mr-3 text-sky-500 dark:text-sky-400" size={24} />
              <h2 className="text-2xl font-semibold">Employment Growth by Cluster</h2>
            </div>
            {clusterInsightsData.length > 0 ? (
              <div className="grid grid-cols-2 gap-4">
                {[...clusterInsightsData]
                  .sort((a, b) => {
                    const growthA = parseFloat(String(a.employment_growth || '0').replace(/[^0-9.-]/g, ''));
                    const growthB = parseFloat(String(b.employment_growth || '0').replace(/[^0-9.-]/g, ''));

                    if (isNaN(growthA) && isNaN(growthB)) return 0;
                    if (isNaN(growthA)) return 1;
                    if (isNaN(growthB)) return -1;

                    return growthB - growthA;
                  })
                  .map((item) => {
                    const growthStr = String(item.employment_growth || '0').replace(/[^0-9.-]/g, '');
                    const growthValue = parseFloat(growthStr);
                    let growthColorClass = "", textColorClass = "";

                    if (isNaN(growthValue)) {
                      growthColorClass = "bg-muted border-border";
                      textColorClass = "text-foreground";
                    } else if (growthValue >= 4) {
                      growthColorClass = "bg-emerald-100/80 dark:bg-emerald-900/30 border-emerald-300 dark:border-emerald-700";
                      textColorClass = "text-emerald-700 dark:text-emerald-300";
                    } else if (growthValue >= 3) {
                      growthColorClass = "bg-blue-100/80 dark:bg-blue-900/30 border-blue-300 dark:border-blue-700";
                      textColorClass = "text-blue-700 dark:text-blue-300";
                    } else if (growthValue >= 2.5) {
                      growthColorClass = "bg-muted border-border";
                      textColorClass = "text-foreground";
                    } else {
                      growthColorClass = "bg-amber-100/80 dark:bg-amber-900/30 border-amber-300 dark:border-amber-700";
                      textColorClass = "text-amber-700 dark:text-amber-300";
                    }

                    return (
                      <div key={`emp-cluster-${item.cluster_id}`} className={`p-4 rounded-lg border ${growthColorClass} flex flex-col items-center`}>
                        <h3 className="text-lg font-medium text-center">
                          Cluster <br /> ({formatCurrency(item.median_price)})
                        </h3>
                        <p className={`text-2xl font-bold mt-2 ${textColorClass}`}>
                          {!isNaN(growthValue) ? `${growthValue.toFixed(1)}%` : 'N/A'}
                        </p>
                        <p className="text-sm text-muted-foreground mt-1">Annual Growth</p>
                      </div>
                    );
                  })}
              </div>
            ) : (
              <p className="text-muted-foreground text-center p-4">No cluster employment growth data available.</p>
            )}
            <div className="mt-4 text-sm text-muted-foreground flex items-start">
              <Info className="mr-2 mt-0.5 flex-shrink-0" size={14} />
              <p>Employment growth indicates economic health and potential future housing demand within each market cluster (identified by median price).</p>
            </div>
          </section>
        </div>
        <section className="p-6 rounded-xl bg-card shadow-lg border border-border mb-12">
          <div className="flex items-center mb-6">
            <BarChart2 className="mr-3 text-sky-500 dark:text-sky-400" size={24} />
            <h2 className="text-2xl font-semibold">AI-Generated Key Market Summaries (Latest Update)</h2>
          </div>

          {generatedInsights.length > 0 ? (
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              {generatedInsights.map((insight, index) => (
                <div key={index} className={`p-4 rounded-lg border ${index % 4 === 0 ? 'bg-blue-50/50 dark:bg-blue-900/20 border-blue-200 dark:border-blue-800' :
                  index % 4 === 1 ? 'bg-emerald-50/50 dark:bg-emerald-900/20 border-emerald-200 dark:border-emerald-800' :
                    index % 4 === 2 ? 'bg-amber-50/50 dark:bg-amber-900/20 border-amber-200 dark:border-amber-800' :
                      'bg-purple-50/50 dark:bg-purple-900/20 border-purple-200 dark:border-purple-800'
                  }`}>
                  <h3 className={`font-semibold mb-2 ${index % 4 === 0 ? 'text-blue-700 dark:text-blue-300' :
                    index % 4 === 1 ? 'text-emerald-700 dark:text-emerald-300' :
                      index % 4 === 2 ? 'text-amber-700 dark:text-amber-300' :
                        'text-purple-700 dark:text-purple-300'
                    }`}>{insight.title || `Insight ${index + 1}`}</h3>
                  {insight.explanation ? (
                    <p
                      className="text-muted-foreground"
                      dangerouslySetInnerHTML={{ __html: insight.explanation }}
                    />
                  ) : (
                    <p className="text-muted-foreground">No explanation provided.</p>
                  )}
                </div>
              ))}
            </div>
          ) : (
            <p className="text-muted-foreground text-center p-4">
              Market insights are currently being generated or are unavailable for the latest data update.
            </p>
          )}
        </section>

        <div className="mt-8 text-center">
          <h2 className="text-3xl font-bold mb-6">Ready to Explore Property Opportunities?</h2>
          <p className="text-xl text-muted-foreground mb-8 max-w-2xl mx-auto">
            Leverage these market insights to make informed investment decisions in areas with strong growth potential.
          </p>
          <div className="flex justify-center">
            <Link href="/home">
              <Button variant="outline" size="lg" className="text-lg px-8 py-6">
                Explore Property Listings
              </Button>
            </Link>
          </div>
        </div>
      </div >
    </main >
  );
};