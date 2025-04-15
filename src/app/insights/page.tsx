'use client'

import React, { useState, useEffect } from 'react';
import Link from 'next/link';
import { Button } from '@/app/components/ui/button';
import { TrendingUp, Home, BarChart2, Info, Loader2, AlertTriangle } from 'lucide-react';

interface InsightData {
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

export default function Insights() {
  const [insightsData, setInsightsData] = useState<InsightData[]>([]);
  const [generatedInsights, setGeneratedInsights] = useState<GeneratedInsight[]>([]);
  const [isLoading, setIsLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchCombinedData = async () => {
      setIsLoading(true);
      setError(null);
      setInsightsData([]); 
      setGeneratedInsights([]);
      try {
        const response = await fetch('/api/insights');

        if (!response.ok) {
          let errorMsg = `API Error: ${response.status} ${response.statusText}`;
          try {
            const errorData = await response.json();
            errorMsg = errorData.error || errorData.message || errorMsg;
          } catch (parseError) {}
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

        setInsightsData(data.insights);
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

  const formatCurrency = (value: string): string => {
      try {
        const numericString = String(value).replace(/[^0-9.]/g, '');
        const number = parseFloat(numericString);
        if (isNaN(number)) return value;
        return `$${number.toLocaleString('en-US', { maximumFractionDigits: 0 })}`;
      } catch (error) {
        console.error("Error formatting currency:", error, "Value:", value);
        return value;
      }
  };

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
              <h2 className="text-2xl font-semibold">Housing Affordability</h2>
            </div>
            <div className="overflow-x-auto">
              <table className="w-full border-collapse">
                 <thead>
                   <tr className="border-b border-border">
                     <th className="p-3 text-left font-medium text-muted-foreground">Cluster</th>
                     <th className="p-3 text-left font-medium text-muted-foreground">Avg Payroll</th>
                     <th className="p-3 text-left font-medium text-muted-foreground">Avg House Price</th>
                     <th className="p-3 text-left font-medium text-muted-foreground">Affordability Ratio</th>
                   </tr>
                 </thead>
                 <tbody>
                  {insightsData.map((item) => {
                    let ratioColorClass = "";
                    if (item.affordability_ratio >= 0.15) ratioColorClass = "text-emerald-600 dark:text-emerald-400 font-medium";
                    else if (item.affordability_ratio >= 0.1) ratioColorClass = "text-blue-600 dark:text-blue-400 font-medium";
                    else if (item.affordability_ratio >= 0.07) ratioColorClass = "text-amber-600 dark:text-amber-400 font-medium";
                    else ratioColorClass = "text-rose-600 dark:text-rose-400 font-medium";

                    return (
                      <tr key={`payroll-${item.cluster_id}`} className="border-b border-border hover:bg-muted/50">
                        <td className="p-3 font-medium">Cluster {item.cluster_id}</td>
                        <td className="p-3">{formatCurrency(item.avg_payroll)}</td>
                        <td className="p-3">{formatCurrency(item.avg_price)}</td>
                        <td className={`p-3 ${ratioColorClass}`}>{item.affordability_ratio}</td>
                      </tr>
                    );
                  })}
                </tbody>
              </table>
            </div>
             <div className="mt-4 text-sm text-muted-foreground flex items-start">
               <Info className="mr-2 mt-0.5 flex-shrink-0" size={14} />
               <p>A higher Payroll-to-Price Ratio suggests greater housing affordability relative to local wages.</p>
             </div>
          </section>

          <section className="p-6 rounded-xl bg-card shadow-lg border border-border">
             <div className="flex items-center mb-4">
               <TrendingUp className="mr-3 text-sky-500 dark:text-sky-400" size={24} />
               <h2 className="text-2xl font-semibold">Employment Growth</h2>
             </div>
             <div className="grid grid-cols-2 gap-4">
              {insightsData.map((item) => {
                  const growthValue = parseFloat(String(item.employment_growth || '0').replace(/[^0-9.-]/g, ''));
                  let growthColorClass = "", textColorClass = "";

                  if (isNaN(growthValue)) {
                      growthColorClass = "bg-muted border-border";
                      textColorClass = "text-foreground";
                  } else if (growthValue >= 4) {
                      growthColorClass = "bg-emerald-100/80 dark:bg-emerald-900/30 border-emerald-300 dark:border-emerald-700"; textColorClass = "text-emerald-700 dark:text-emerald-300";
                  } else if (growthValue >= 3) {
                      growthColorClass = "bg-blue-100/80 dark:bg-blue-900/30 border-blue-300 dark:border-blue-700"; textColorClass = "text-blue-700 dark:text-blue-300";
                  } else if (growthValue >= 2.5) {
                      growthColorClass = "bg-muted border-border"; textColorClass = "text-foreground";
                  } else {
                      growthColorClass = "bg-amber-100/80 dark:bg-amber-900/30 border-amber-300 dark:border-amber-700"; textColorClass = "text-amber-700 dark:text-amber-300";
                  }

                  return (
                    <div key={`emp-${item.cluster_id}`} className={`p-4 rounded-lg border ${growthColorClass} flex flex-col items-center`}>
                      <h3 className="text-lg font-medium">Cluster {item.cluster_id}</h3>
                      <p className={`text-2xl font-bold ${textColorClass}`}>{item.employment_growth || 'N/A'}%</p>
                      <p className="text-sm text-muted-foreground mt-1">Annual Growth</p>
                    </div>
                  );
              })}
             </div>
             <div className="mt-4 text-sm text-muted-foreground flex items-start">
               <Info className="mr-2 mt-0.5 flex-shrink-0" size={14} />
               <p>Employment growth indicates economic health and future housing demand.</p>
             </div>
          </section>
        </div>

        <section className="p-6 rounded-xl bg-card shadow-lg border border-border mb-12">
          <div className="flex items-center mb-6">
            <BarChart2 className="mr-3 text-sky-500 dark:text-sky-400" size={24} />
            <h2 className="text-2xl font-semibold">Key Market Insights (Latest Update)</h2>
          </div>

          {generatedInsights.length > 0 ? (
            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              {generatedInsights.map((insight, index) => (
                 <div key={index} className={`p-4 rounded-lg border ${
                     index % 4 === 0 ? 'bg-blue-50/50 dark:bg-blue-900/20 border-blue-200 dark:border-blue-800' :
                     index % 4 === 1 ? 'bg-emerald-50/50 dark:bg-emerald-900/20 border-emerald-200 dark:border-emerald-800' :
                     index % 4 === 2 ? 'bg-amber-50/50 dark:bg-amber-900/20 border-amber-200 dark:border-amber-800' :
                     'bg-purple-50/50 dark:bg-purple-900/20 border-purple-200 dark:border-purple-800'
                 }`}>
                   <h3 className={`font-semibold mb-2 ${
                       index % 4 === 0 ? 'text-blue-700 dark:text-blue-300' :
                       index % 4 === 1 ? 'text-emerald-700 dark:text-emerald-300' :
                       index % 4 === 2 ? 'text-amber-700 dark:text-amber-300' :
                       'text-purple-700 dark:text-purple-300'
                   }`}>{insight.title || `Insight ${index + 1}`}</h3>
                   <p className="text-muted-foreground">{insight.explanation || "No explanation provided."}</p>
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
      </div>
    </main>
  );
};