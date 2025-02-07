'use client'

import { Button } from "@/app/components/ui/button";
import { useRouter } from "next/navigation";
import Image from "next/image";

export default function LandingPage() {
  const router = useRouter();

  return (
    <main className="flex-1 bg-background">
      <div className="container mx-auto px-4 py-16">
        <div className="flex flex-col lg:flex-row items-center justify-between gap-12">
          <div className="flex-1 text-center lg:text-left">
            <h1 className="text-4xl lg:text-6xl font-bold mb-6 bg-gradient-to-r from-blue-600 to-sky-600 inline-block text-transparent bg-clip-text">
              Welcome to CivicNest
            </h1>
            <p className="text-xl mb-8 text-muted-foreground">
              Discover your perfect neighborhood with comprehensive property insights.
              Make confident real estate decisions with detailed analytics beyond traditional listings.
            </p>
            <div className="flex flex-colsm:flex-row gap-4 justify-center lg:justify-start">
              <Button
                variant="outline"
                size="lg"
                className="text-lg px-8 py-6"
                onClick={() => router.push('/auth/sign-up')}
              >
                Create an Account
              </Button>
              <Button
                variant="outline"
                size="lg"
                className="text-lg px-8 py-6"
                onClick={() => router.push('/auth/sign-in')}
              >
                Sign In
              </Button>
            </div>
          </div>
          <div className="flex-1 relative w-full max-w-xl h-[400px]">
          <Image
              src="/hero-image-light.png"
              alt="CivicNest Platform Preview"
              fill
              className="object-contain dark:hidden"
              priority
            />
            <Image
              src="/hero-image-dark.png"
              alt="CivicNest Platform Preview"
              fill
              className="hidden dark:block object-contain"
              priority
            />
          </div>
        </div>

        <div className="mt-24 grid md:grid-cols-3 gap-8">
          <div className="p-6 rounded-xl bg-card shadow-lg">
            <h3 className="text-xl font-semibold mb-3">Interactive Mapping</h3>
            <p className="text-muted-foreground">
              Explore neighborhoods with our color-coded map interface showing walkability, food access, crime rates, and school ratings.
            </p>
          </div>
          <div className="p-6 rounded-xl bg-card shadow-lg">
            <h3 className="text-xl font-semibold mb-3">Comprehensive Analytics</h3>
            <p className="text-muted-foreground">
              Access detailed neighborhood insights and property value trends to make informed real estate decisions.
            </p>
          </div>
          <div className="p-6 rounded-xl bg-card shadow-lg">
            <h3 className="text-xl font-semibold mb-3">Smart Property Search</h3>
            <p className="text-muted-foreground">
              Find your ideal home with advanced filters and real-time market data beyond traditional listing platforms.
            </p>
          </div>
        </div>

        <div className="mt-24 text-center">
          <h2 className="text-3xl font-bold mb-6">Ready to Find Your Perfect Neighborhood?</h2>
          <p className="text-xl text-muted-foreground mb-8 max-w-2xl mx-auto">
            Join CivicNest today and gain access to comprehensive neighborhood analytics that help you make confident property decisions.
          </p>
          <Button
            variant="outline"
            size="lg"
            className="text-lg px-8 py-6"
            onClick={() => router.push('/auth/sign-up')}
          >
            Start Your Property Search
          </Button>
        </div>
      </div>
    </main>
  );
}