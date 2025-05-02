import type { Metadata } from "next";
import { Header } from "../components/header";
import { Footer } from '../components/footer';
import { ThemeProvider } from "../components/theme-provider";
import { ClerkProvider } from '@clerk/nextjs'
import './globals.css'

export const metadata: Metadata = {
  title: "CivicNest",
  description: "Make informed neighborhood decisions with real estate insights",
  metadataBase: new URL('https://civicnest.carmine.live'),
  
  openGraph: {
    type: 'website',
    url: 'https://civicnest.carmine.live',
    title: "CivicNest",
    description: "Make informed neighborhood decisions with real estate insights",
    siteName: 'CivicNest',
    images: [
      {
        url: '/icons/icon-192x192.png', 
        width: 192,
        height: 192,
        alt: 'CivicNest'
      }
    ]
  },
  
  icons: {
    icon: [
      { url: '/icons/favicon-16x16.png', sizes: '16x16', type: 'image/png' },
      { url: '/icons/favicon-32x32.png', sizes: '32x32', type: 'image/png' },
      { url: '/icons/icon-192x192.png', sizes: '192x192', type: 'image/png' },
      { url: '/icons/icon-512x512.png', sizes: '512x512', type: 'image/png' },
    ],
    shortcut: '/icons/favicon-16x16.png',
    apple: '/icons/icon-192x192.png'
  }
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body className="min-h-screen flex flex-col">
        <ThemeProvider
          attribute="class"
          defaultTheme="system"
          enableSystem
          disableTransitionOnChange
        >
          <ClerkProvider afterSignOutUrl={'/'}>
            <Header />
            <div className="flex-grow">
              {children}
            </div>
            <Footer />
          </ClerkProvider>
        </ThemeProvider>
      </body>
    </html>
  );
}