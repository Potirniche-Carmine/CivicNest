'use client'

import { Button } from "@/components/ui/button"; 
import Link from "next/link";
import { MapPin, Users, Filter, Cpu, Search, TrendingUp } from 'lucide-react';

export default function FeaturesPage() {

  return (
    <main className="flex-1 bg-background">
      <div className="container mx-auto px-4 py-16">

        <div className="text-center mb-16 pb-8 border-b">
          <h1 className="text-4xl lg:text-5xl font-bold mb-4 bg-gradient-to-r from-blue-600 to-sky-600 inline-block text-transparent bg-clip-text">
            CivicNest Features
          </h1>
          <p className="text-xl max-w-3xl mx-auto text-muted-foreground">
            Go beyond standard listings. Leverage powerful analytics, interactive visualizations, and AI-driven insights to make smarter real estate decisions in the Reno area.
          </p>
        </div>

        <section className="mb-12">
          <h2 className="text-3xl font-semibold mb-4 flex items-center">
            <MapPin className="mr-3 h-7 w-7 text-blue-500 flex-shrink-0" />
            Interactive Map Exploration
          </h2>
          <div className="pl-10">
            <p className="text-lg text-muted-foreground mb-4">
              Visualize the market instantly with our interactive map. Properties are grouped into color-coded <span className="font-semibold text-foreground/90">Price Clusters</span>, helping you understand market segmentation at a glance.
            </p>
            <p className="text-lg text-muted-foreground mb-4">
              Click on any property marker to reveal key details:
            </p>
            <ul className="list-disc list-inside text-lg text-muted-foreground space-y-2 mb-4">
              <li>Current Price, Address, Bed/Bath count.</li>
              <li>Average price for its cluster.</li>
              <li>Predicted <span className="font-semibold text-foreground/90">Employment Trend (%)</span> for the zip code.</li>
              <li>A direct link to view the full listing on Zillow.</li>
            </ul>
             <Button variant="outline" size="sm" asChild>
                <Link href="/home">
                   <span>
                     Explore the Map <Search className="ml-2 h-4 w-4 inline-block" /> {/* Added inline-block for better alignment */}
                   </span>
                </Link>
             </Button>
           </div>
        </section>

        <section className="mb-12">
           <h2 className="text-3xl font-semibold mb-4 flex items-center">
              <Users className="mr-3 h-7 w-7 text-emerald-500 flex-shrink-0" />
              In-Depth Zip Code Analysis
            </h2>
           <div className="pl-10">
            <p className="text-lg text-muted-foreground mb-4">
              Understand the underlying factors driving a neighborhood's potential. For specific zip codes (requires account), access detailed data including:
            </p>
            <ul className="list-disc list-inside text-lg text-muted-foreground space-y-2 mb-4">
              <li><span className="font-semibold text-foreground/90">Demographics:</span> Median Age, Total School Enrollment.</li>
              <li><span className="font-semibold text-foreground/90">School Quality:</span> Count of poorly rated Elementary, Middle, and High schools.</li>
              <li><span className="font-semibold text-foreground/90">Cost of Living:</span> Index score compared to national and Reno averages.</li>
              <li><span className="font-semibold text-foreground/90">Local Map View:</span> Focused map of the selected zip code area.</li>
               <li><span className="font-semibold text-foreground/90">AI Analysis:</span> Key takeaways specific to that zip code's market conditions.</li>
            </ul>
             <Button variant="outline" size="sm" asChild>
                <Link href="/insights">
                   <span>
                     View Market Insights <TrendingUp className="ml-2 h-4 w-4 inline-block" />
                   </span>
                </Link>
             </Button>
            </div>
        </section>

        <section className="mb-12">
           <h2 className="text-3xl font-semibold mb-4 flex items-center">
               <Filter className="mr-3 h-7 w-7 text-amber-500 flex-shrink-0" />
               Targeted Filtering & Economic Trends
             </h2>
            <div className="pl-10">
             <p className="text-lg text-muted-foreground mb-4">
               Focus your search effectively. Select specific <span className="font-semibold text-foreground/90">Price Clusters</span> on the map to isolate properties within desired market segments, making comparisons easier.
             </p>
             <p className="text-lg text-muted-foreground mb-4">
               Gauge the economic health and potential future demand with <span className="font-semibold text-foreground/90">Projected Employment Trend</span> data displayed for each property's zip code. Higher growth can indicate a stronger future housing market.
             </p>
              <Button variant="outline" size="sm" asChild>
                <Link href="/home">
                   <span>
                      Try Filtering Now <Filter className="ml-2 h-4 w-4 inline-block" />
                   </span>
                </Link>
             </Button>
             </div>
        </section>

        <section className="mb-16">
           <h2 className="text-3xl font-semibold mb-4 flex items-center">
              <Cpu className="mr-3 h-7 w-7 text-purple-500 flex-shrink-0" />
              AI-Powered Market Summaries
            </h2>
           <div className="pl-10">
            <p className="text-lg text-muted-foreground mb-4">
              Cut through the noise with AI-generated insights (requires account). Our system analyzes the complex interplay of property data, cluster behavior, economic trends, and zip code statistics.
            </p>
            <p className="text-lg text-muted-foreground mb-4">
              Receive concise, actionable summaries highlighting key market characteristics, potential opportunities, and risk factors, both for the overall market and specific zip codes.
            </p>
             <Button variant="outline" size="sm" asChild>
                <Link href="/insights">
                   <span>
                      See AI Summaries <Cpu className="ml-2 h-4 w-4 inline-block" />
                   </span>
                </Link>
             </Button>
             </div>
        </section>

        <div className="mt-16 text-center border-t pt-16">
          <h2 className="text-3xl font-bold mb-6">Ready to Explore with Enhanced Insights?</h2>
          <p className="text-xl text-muted-foreground mb-8 max-w-2xl mx-auto">
            Start using CivicNest's powerful features today. Explore the interactive map freely or sign up to access the full suite of analytical tools and AI-generated insights.
          </p>
          <div className="flex flex-col sm:flex-row gap-4 justify-center items-center">
             <Link href="/home">
               <Button
                 variant="default"
                 size="lg"
                 className="text-lg px-8 py-6 bg-blue-600 hover:bg-blue-700 text-white w-full sm:w-auto"
               >
                 Explore The Map
               </Button>
             </Link>
             <Link href="/auth/sign-up">
               <Button
                 variant="outline"
                 size="lg"
                 className="text-lg px-8 py-6 w-full sm:w-auto"
               >
                 Sign Up for Full Access
               </Button>
            </Link>
          </div>
        </div>

      </div>
    </main>
  );
}