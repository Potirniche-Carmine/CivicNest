'use client'

import { Button } from "@/components/ui/button";
import Link from "next/link";
import { Database, School, BarChart2, Home, ExternalLink, LineChart, Shield } from 'lucide-react';

export default function OurDataPage() {
  return (
    <main className="flex-1 bg-background">
      <div className="container mx-auto px-8 py-16">

        <div className="text-center mb-16 pb-8 border-b">
          <h1 className="text-4xl lg:text-5xl font-bold mb-4 bg-gradient-to-r from-blue-600 to-sky-600 inline-block text-transparent bg-clip-text">
            Our Data Sources
          </h1>
          <p className="text-xl max-w-3xl mx-auto text-muted-foreground">
            CivicNest leverages reliable, high-quality data from trusted sources. Our analytics and insights are built on comprehensive datasets that provide accurate and timely information about the Reno real estate market.
          </p>
        </div>

        <section className="mb-12">
          <h2 className="text-3xl font-semibold mb-4 flex items-center">
            <Home className="mr-3 h-7 w-7 text-blue-500 flex-shrink-0" />
            Property Listings & Market Data
          </h2>
          <div className="pl-10">
            <p className="text-lg text-muted-foreground mb-4">
              Our comprehensive property listings and market data are powered by the Zillow API, providing up-to-date information on home values, property details, and market trends.
            </p>
            <p className="text-lg text-muted-foreground mb-4">
              Through this integration, we offer:
            </p>
            <ul className="list-disc list-inside text-lg text-muted-foreground space-y-2 mb-4">
              <li>Current property listings with accurate pricing.</li>
              <li>Detailed property specifications (beds, baths, square footage).</li>
              <li>Property location data for our interactive map.</li>
              <li>Direct links to original listings on Zillow.</li>
            </ul>
            <div className="mt-6 flex items-center space-x-2">
              <ExternalLink className="h-5 w-5 text-blue-500" />
              <a href="https://rapidapi.com/oneapiproject/api/zillow-working-api/playground/apiendpoint_528a92b5-42a4-4c7f-a429-4d8b43066c56" target="_blank" rel="noopener noreferrer" className="text-sm text-blue-500 hover:underline">
                Data provided by: Zillow API via RapidAPI
              </a>
            </div>
          </div>
        </section>

        <section className="mb-12">
          <h2 className="text-3xl font-semibold mb-4 flex items-center">
            <School className="mr-3 h-7 w-7 text-emerald-500 flex-shrink-0" />
            Education & School Quality Data
          </h2>
          <div className="pl-10">
            <p className="text-lg text-muted-foreground mb-4">
              Understanding school quality is essential for many homebuyers. Our education data comes directly from the Nevada Report Card, the official accountability portal for Nevada's public education system.
            </p>
            <p className="text-lg text-muted-foreground mb-4">
              This source provides:
            </p>
            <ul className="list-disc list-inside text-lg text-muted-foreground space-y-2 mb-4">
              <li>School performance ratings for elementary, middle, and high schools.</li>
              <li>Count of poorly rated schools per zip code.</li>
              <li>Total school enrollment figures.</li>
              <li>School district boundaries and information.</li>
            </ul>
            <div className="mt-6 flex items-center space-x-2">
              <ExternalLink className="h-5 w-5 text-emerald-500" />
              <a href="https://nevadareportcard.nv.gov/di/" target="_blank" rel="noopener noreferrer" className="text-sm text-emerald-500 hover:underline">
                Data provided by: Nevada Report Card
              </a>
            </div>
          </div>
        </section>

        <section className="mb-12">
          <h2 className="text-3xl font-semibold mb-4 flex items-center">
            <BarChart2 className="mr-3 h-7 w-7 text-amber-500 flex-shrink-0" />
            Census & Employment Data
          </h2>
          <div className="pl-10">
            <p className="text-lg text-muted-foreground mb-4">
              Our employment trends and projections are sourced from the U.S. Census Bureau, providing authoritative demographic and economic data at the zip code level.
            </p>
            <p className="text-lg text-muted-foreground mb-4">
              This data includes:
            </p>
            <ul className="list-disc list-inside text-lg text-muted-foreground space-y-2 mb-4">
              <li><span className="font-semibold text-foreground/90">Employment Trends:</span> Historical and projected employment growth by zip code.</li>
              <li><span className="font-semibold text-foreground/90">Population Statistics:</span> Current and projected population figures.</li>
              <li><span className="font-semibold text-foreground/90">Income Data:</span> Median household income and economic indicators.</li>
              <li><span className="font-semibold text-foreground/90">Housing Statistics:</span> Homeownership rates and housing characteristics.</li>
            </ul>
            <div className="mt-6 flex items-center space-x-2">
              <ExternalLink className="h-5 w-5 text-amber-500" />
              <a href="https://data.census.gov/" target="_blank" rel="noopener noreferrer" className="text-sm text-amber-500 hover:underline">
                Data provided by: U.S. Census Bureau
              </a>
            </div>
          </div>
        </section>

        <section className="mb-16">
          <h2 className="text-3xl font-semibold mb-4 flex items-center">
            <Database className="mr-3 h-7 w-7 text-purple-500 flex-shrink-0" />
            Demographic & Cost of Living Data
          </h2>
          <div className="pl-10">
            <p className="text-lg text-muted-foreground mb-4">
              For comprehensive demographic insights and cost of living indicators, we rely on City-Data.com, a trusted resource for detailed community information.
            </p>
            <p className="text-lg text-muted-foreground mb-4">
              This source provides:
            </p>
            <ul className="list-disc list-inside text-lg text-muted-foreground space-y-2 mb-4">
              <li><span className="font-semibold text-foreground/90">Median Age:</span> Age demographics by zip code.</li>
              <li><span className="font-semibold text-foreground/90">Cost of Living Index:</span> Comparative cost measurements against national and Reno averages.</li>
              <li><span className="font-semibold text-foreground/90">Crime Statistics:</span> Safety indicators for different areas.</li>
              <li><span className="font-semibold text-foreground/90">Neighborhood Characteristics:</span> Additional community features and amenities.</li>
            </ul>
            <div className="mt-6 flex items-center space-x-2">
              <ExternalLink className="h-5 w-5 text-purple-500" />
              <a href="https://www.city-data.com/zips/zipdir/dir108.html" target="_blank" rel="noopener noreferrer" className="text-sm text-purple-500 hover:underline">
                Data provided by: City-Data.com
              </a>
            </div>
          </div>
        </section>

        <section className="mb-16">
          <h2 className="text-3xl font-semibold mb-4 flex items-center">
            <Shield className="mr-3 h-7 w-7 text-rose-500 flex-shrink-0" />
            Our Data Commitment
          </h2>
          <div className="pl-10">
            <p className="text-lg text-muted-foreground mb-4">
              At CivicNest, we are committed to providing only the most reliable and up-to-date information. Our data processing includes:
            </p>
            <ul className="list-disc list-inside text-lg text-muted-foreground space-y-2 mb-4">
              <li>Regular updates to maintain currency of all information.</li>
              <li>Rigorous cleaning and validation procedures.</li>
              <li>Transparent sourcing with links to original data providers.</li>
              <li>Privacy-focused handling of all information.</li>
            </ul>
            <p className="text-lg text-muted-foreground mt-4">
              We transform raw data into actionable insights through our proprietary algorithms and AI analysis, helping you make informed real estate decisions with confidence.
            </p>
          </div>
        </section>

        <div className="mt-16 text-center border-t pt-16">
          <h2 className="text-3xl font-bold mb-6">Ready to Make Data-Driven Decisions?</h2>
          <p className="text-xl text-muted-foreground mb-8 max-w-2xl mx-auto">
            Start exploring CivicNest's powerful analytics and insights, backed by reliable data from trusted sources. Better information leads to better real estate decisions.
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
            <Link href="/insights">
              <Button
                variant="outline"
                size="lg"
                className="text-lg px-8 py-6 w-full sm:w-auto"
              >
                View Market Insights
              </Button>
            </Link>
          </div>
        </div>

      </div>
    </main>
  );
}