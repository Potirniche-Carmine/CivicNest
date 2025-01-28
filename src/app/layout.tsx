import type { Metadata } from "next";
import { Header } from "./components/header";
import { Footer } from './components/footer';

import { ClerkProvider, SignIn, SignedIn, SignedOut, UserButton } from '@clerk/nextjs'
import './globals.css'

export const metadata: Metadata = {
  title: "CivicNest",
  description: "A comprehensive platform providing real estate insights to help users make informed neighborhood decisions.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <ClerkProvider>
      <html lang="en">
        <body className="min-h-screen flex flex-col">
          <SignedOut>
            <div className="fixed inset-0 flex items-center justify-center p-4 bg-gray-50">
              <SignIn
                routing="hash"
                appearance={{
                  variables: {
                    colorPrimary: '#2563eb',
                    colorText: '#000000',
                    borderRadius: '8px'
                  },
                  elements: {
                    card: 'shadow-lg'
                  }
                }}/>
            </div>
          </SignedOut>
          <SignedIn>
            <Header />
            <div className="flex-grow">
              {children}
            </div>
            <Footer />
          </SignedIn>
        </body>
      </html>
    </ClerkProvider>
  );
}
