'use client'

import React from 'react';
import Link from 'next/link';
import { Button } from '@/app/components/ui/button';
import { TrendingUp, Home, BarChart2, Info } from 'lucide-react';

interface EmploymentGrowth {
  cluster: number;
  avgGrowth: string;
}

interface PayrollPriceRatio {
  cluster: number;
  avgPayroll: string;
  avgHousePrice: string;
  ratio: number;
}

const employmentGrowthData: EmploymentGrowth[] = [
  { cluster: 1, avgGrowth: "2.38%" },
  { cluster: 2, avgGrowth: "2.86%" },
  { cluster: 3, avgGrowth: "4.12%" },
  { cluster: 4, avgGrowth: "4.49%" },
];

const payrollPriceData: PayrollPriceRatio[] = [
  { cluster: 1, avgPayroll: "$46,307.99", avgHousePrice: "$429,209.34", ratio: 0.1079 },
  { cluster: 2, avgPayroll: "$47,160.59", avgHousePrice: "$596,008.82", ratio: 0.0791 },
  { cluster: 3, avgPayroll: "$45,685.44", avgHousePrice: "$238,207.24", ratio: 0.1918 },
  { cluster: 4, avgPayroll: "$45,556.42", avgHousePrice: "$824,959.37", ratio: 0.0552 },
];

const InsightsPage = () => {
  return (
    <main className="flex-1 bg-background min-h-screen">
      <div className="container mx-auto px-4 py-16">
        <h1 className="text-4xl font-bold mb-8 bg-gradient-to-r from-blue-600 to-sky-600 inline-block text-transparent bg-clip-text">
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
                  {payrollPriceData.map((item) => {
                    let ratioColorClass = "";
                    if (item.ratio >= 0.15) {
                      ratioColorClass = "text-emerald-600 dark:text-emerald-400 font-medium";
                    } else if (item.ratio >= 0.1) {
                      ratioColorClass = "text-blue-600 dark:text-blue-400 font-medium";
                    } else if (item.ratio >= 0.07) {
                      ratioColorClass = "text-amber-600 dark:text-amber-400 font-medium";
                    } else {
                      ratioColorClass = "text-rose-600 dark:text-rose-400 font-medium";
                    }
                    
                    return (
                      <tr key={`payroll-${item.cluster}`} className="border-b border-border hover:bg-muted/50">
                        <td className="p-3 font-medium">Cluster {item.cluster}</td>
                        <td className="p-3">{item.avgPayroll}</td>
                        <td className="p-3">{item.avgHousePrice}</td>
                        <td className={`p-3 ${ratioColorClass}`}>
                          {item.ratio.toFixed(4)}
                        </td>
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
              {employmentGrowthData.map((item) => {
                const growthValue = parseFloat(item.avgGrowth.replace("%", ""));
                let growthColorClass = "";
                let textColorClass = "";
                
                if (growthValue >= 4) {
                  growthColorClass = "bg-emerald-100/80 dark:bg-emerald-900/30 border-emerald-300 dark:border-emerald-700";
                  textColorClass = "text-emerald-700 dark:text-emerald-300";
                } else if (growthValue >= 3) {
                  growthColorClass = "bg-blue-100/80 dark:bg-blue-900/30 border-blue-300 dark:border-blue-700";
                  textColorClass = "text-blue-700 dark:text-blue-300";
                } else if (growthValue >= 2.5) {
                  growthColorClass = "bg-amber-100/80 dark:bg-amber-900/30 border-amber-300 dark:border-amber-700";
                  textColorClass = "text-amber-700 dark:text-amber-300";
                } else {
                  growthColorClass = "bg-muted border-border";
                  textColorClass = "text-foreground";
                }
                
                return (
                  <div 
                    key={`emp-${item.cluster}`} 
                    className={`p-4 rounded-lg border ${growthColorClass} flex flex-col items-center`}
                  >
                    <h3 className="text-lg font-medium">Cluster {item.cluster}</h3>
                    <p className={`text-2xl font-bold ${textColorClass}`}>{item.avgGrowth}</p>
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
            <h2 className="text-2xl font-semibold">Key Market Insights</h2>
          </div>
          
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div className="p-4 rounded-lg bg-blue-50/50 dark:bg-blue-900/20 border border-blue-200 dark:border-blue-800">
              <h3 className="font-semibold text-blue-700 dark:text-blue-300 mb-2">Investment Opportunity</h3>
              <p className="text-muted-foreground">Cluster 3 combines strong employment growth (4.12%) with the highest affordability ratio (0.1918), making it potentially attractive for investment.</p>
            </div>
            
            <div className="p-4 rounded-lg bg-emerald-50/50 dark:bg-emerald-900/20 border border-emerald-200 dark:border-emerald-800">
              <h3 className="font-semibold text-emerald-700 dark:text-emerald-300 mb-2">Growth Leaders</h3>
              <p className="text-muted-foreground">Clusters 3 and 4 show exceptional employment growth rates above 4%, suggesting strong economic development in these areas.</p>
            </div>
            
            <div className="p-4 rounded-lg bg-amber-50/50 dark:bg-amber-900/20 border border-amber-200 dark:border-amber-800">
              <h3 className="font-semibold text-amber-700 dark:text-amber-300 mb-2">Affordability Challenge</h3>
              <p className="text-muted-foreground">Despite having the highest employment growth, Cluster 4 shows the lowest affordability ratio (0.0552), indicating potential housing accessibility issues.</p>
            </div>
            
            <div className="p-4 rounded-lg bg-purple-50/50 dark:bg-purple-900/20 border border-purple-200 dark:border-purple-800">
              <h3 className="font-semibold text-purple-700 dark:text-purple-300 mb-2">Market Balance</h3>
              <p className="text-muted-foreground">Cluster 1 offers moderate affordability (0.1079) with stable but slower employment growth (2.38%), potentially representing a balanced market.</p>
            </div>
          </div>
        </section>
        
        <div className="mt-8 text-center">
          <h2 className="text-3xl font-bold mb-6">Ready to Explore Property Opportunities?</h2>
          <p className="text-xl text-muted-foreground mb-8 max-w-2xl mx-auto">
            Leverage these market insights to make informed investment decisions in areas with strong growth potential.
          </p>
          <div className="flex justify-center">
            <Link href="/home">
              <Button
                variant="outline"
                size="lg"
                className="text-lg px-8 py-6"
              >
                Explore Property Listings
              </Button>
            </Link>
          </div>
        </div>
      </div>
    </main>
  );
};

export default InsightsPage;