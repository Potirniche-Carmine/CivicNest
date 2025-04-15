"use client";
import Link from 'next/link';
import { Button } from '@/components/ui/button';

import { Map } from '@/components/map';

export default function Home() {
  return (
    <div className="container mx-auto px-12 py-4">
        <Map />
        <div className="flex justify-center py-10">
            <Link href="/insights">
              <Button
                variant="outline"
                size="lg"
                className="text-lg px-8 py-6"
              >
                Explore Insights
              </Button>
            </Link>
          </div>
    </div>
    
  );
};
