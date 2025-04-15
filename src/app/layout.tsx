import type { Metadata } from "next";
import { Header } from "./components/header";
import { Footer } from './components/footer';
import { ThemeProvider } from "./components/theme-provider";

import { ClerkProvider } from '@clerk/nextjs'
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
    <html lang="en" suppressHydrationWarning>
      <body className="min-h-screen flex flex-col">
        <ThemeProvider
          attribute="class"
          defaultTheme="system"
          enableSystem
          disableTransitionOnChange
        >
          <ClerkProvider
          afterSignOutUrl={'/'}>
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
