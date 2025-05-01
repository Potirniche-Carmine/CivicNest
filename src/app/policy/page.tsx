'use client'

import Link from "next/link";
import { Shield, FileText, Key, Eye, Clock, Server, Users, AlertTriangle } from 'lucide-react';

export default function PolicyAndTermsPage() {
  return (
    <main className="flex-1 bg-background">
      <div className="container mx-auto px-8 py-16">

        <div className="text-center mb-16 pb-8 border-b">
          <h1 className="text-4xl lg:text-5xl font-bold mb-4 bg-gradient-to-r from-blue-600 to-sky-600 inline-block text-transparent bg-clip-text">
            Terms of Service & Privacy Policy
          </h1>
          <p className="text-xl max-w-3xl mx-auto text-muted-foreground">
            CivicNest is committed to transparency and protecting your privacy. This page outlines our terms of service and explains how we handle your information.
          </p>
          <p className="text-md mt-4 max-w-2xl mx-auto text-muted-foreground">
            Last Updated: April 30, 2025
          </p>
        </div>

        <div className="mb-16">
          <h2 className="text-3xl font-semibold mb-6 pb-2 border-b flex items-center">
            <FileText className="mr-3 h-7 w-7 text-blue-500 flex-shrink-0" />
            Terms of Service
          </h2>

          <section className="mb-10">
            <h3 className="text-2xl font-semibold mb-4 flex items-center">
              <Users className="mr-3 h-6 w-6 text-emerald-500 flex-shrink-0" />
              1. Account Terms
            </h3>
            <div className="pl-10">
              <p className="text-lg text-muted-foreground mb-4">
                CivicNest uses Clerk for user authentication. By creating an account, you agree to:
              </p>
              <ul className="list-disc list-inside text-lg text-muted-foreground space-y-2 mb-4">
                <li>Provide accurate and complete registration information.</li>
                <li>Maintain the security of your account credentials.</li>
                <li>Accept responsibility for all activities that occur under your account.</li>
                <li>Comply with all applicable laws and regulations.</li>
              </ul>
              <p className="text-lg text-muted-foreground">
                CivicNest reserves the right to suspend or terminate accounts that violate our terms.
              </p>
            </div>
          </section>

          <section className="mb-10">
            <h3 className="text-2xl font-semibold mb-4 flex items-center">
              <Server className="mr-3 h-6 w-6 text-amber-500 flex-shrink-0" />
              2. Service Usage
            </h3>
            <div className="pl-10">
              <p className="text-lg text-muted-foreground mb-4">
                CivicNest provides real estate market analysis and visualization tools. Users agree to:
              </p>
              <ul className="list-disc list-inside text-lg text-muted-foreground space-y-2 mb-4">
                <li>Use the service for personal or business research purposes only.</li>
                <li>Not attempt to reverse engineer, decompile, or hack the platform.</li>
                <li>Not disrupt or interfere with the security or availability of the service.</li>
                <li>Not use the service to collect or harvest personally identifiable information.</li>
              </ul>
              <p className="text-lg text-muted-foreground">
                CivicNest reserves the right to modify, suspend, or discontinue any part of the service at any time.
              </p>
            </div>
          </section>

          <section className="mb-10">
            <h3 className="text-2xl font-semibold mb-4 flex items-center">
              <AlertTriangle className="mr-3 h-6 w-6 text-rose-500 flex-shrink-0" />
              3. Disclaimers
            </h3>
            <div className="pl-10">
              <p className="text-lg text-muted-foreground mb-4">
                CivicNest provides information and analytics as tools to aid decision-making, but:
              </p>
              <ul className="list-disc list-inside text-lg text-muted-foreground space-y-2 mb-4">
                <li>All content is provided "as is" without warranty of any kind.</li>
                <li>We do not guarantee the accuracy, completeness, or reliability of any data.</li>
                <li>Our analytics and AI-generated insights are not substitutes for professional advice.</li>
                <li>Users should independently verify information before making real estate decisions.</li>
              </ul>
              <p className="text-lg text-muted-foreground">
                CivicNest is not responsible for any decisions made based on information obtained through our platform.
              </p>
            </div>
          </section>
        </div>

        {/* Privacy Policy Section */}
        <div className="mb-16">
          <h2 className="text-3xl font-semibold mb-6 pb-2 border-b flex items-center">
            <Shield className="mr-3 h-7 w-7 text-blue-500 flex-shrink-0" />
            Privacy Policy
          </h2>

          <section className="mb-10">
            <h3 className="text-2xl font-semibold mb-4 flex items-center">
              <Key className="mr-3 h-6 w-6 text-emerald-500 flex-shrink-0" />
              1. Authentication & Data Collection
            </h3>
            <div className="pl-10">
              <p className="text-lg text-muted-foreground mb-4">
                <span className="font-semibold text-foreground/90">Authentication:</span> CivicNest uses Clerk for user authentication. When you create an account:
              </p>
              <ul className="list-disc list-inside text-lg text-muted-foreground space-y-2 mb-4">
                <li>Authentication data is handled and stored by Clerk according to their privacy policy.</li>
                <li>CivicNest does not directly store your passwords or authentication credentials.</li>
                <li>For more information about how Clerk handles your data, please visit their <a href="https://clerk.com/privacy" target="_blank" rel="noopener noreferrer" className="text-blue-500 hover:underline">Privacy Policy</a>.</li>
              </ul>
              <p className="text-lg text-muted-foreground mb-4">
                <span className="font-semibold text-foreground/90">Data Collection:</span> Currently, CivicNest:
              </p>
              <ul className="list-disc list-inside text-lg text-muted-foreground space-y-2 mb-4">
                <li>Does not collect personal data beyond what is necessary for account management.</li>
                <li>Does not use cookies for advertising purposes.</li>
                <li>Does not sell or share your personal information with third parties.</li>
                <li>May collect anonymized usage data to improve our services.</li>
              </ul>
            </div>
          </section>

          <section className="mb-10">
            <h3 className="text-2xl font-semibold mb-4 flex items-center">
              <Eye className="mr-3 h-6 w-6 text-amber-500 flex-shrink-0" />
              2. Data Usage & Sharing
            </h3>
            <div className="pl-10">
              <p className="text-lg text-muted-foreground mb-4">
                CivicNest is committed to minimal data collection. The limited data we do collect:
              </p>
              <ul className="list-disc list-inside text-lg text-muted-foreground space-y-2 mb-4">
                <li>Is used solely to provide and improve our services.</li>
                <li>May be used to personalize your experience on the platform.</li>
                <li>Is not used for advertising or marketing purposes at this time.</li>
                <li>Is not shared with third parties except as required by law.</li>
              </ul>
              <p className="text-lg text-muted-foreground">
                We may share anonymized, aggregated data for research or analysis purposes, but this will never include personally identifiable information.
              </p>
            </div>
          </section>

          <section className="mb-10">
            <h3 className="text-2xl font-semibold mb-4 flex items-center">
              <Clock className="mr-3 h-6 w-6 text-purple-500 flex-shrink-0" />
              3. Future Changes
            </h3>
            <div className="pl-10">
              <p className="text-lg text-muted-foreground mb-4">
                As CivicNest evolves, our data practices may change. We commit to:
              </p>
              <ul className="list-disc list-inside text-lg text-muted-foreground space-y-2 mb-4">
                <li>Notifying users of significant changes to our privacy policy.</li>
                <li>Obtaining appropriate consent before collecting additional types of data.</li>
                <li>Maintaining transparency about how we use your information.</li>
                <li>Providing options to opt out of new data collection where possible.</li>
              </ul>
              <p className="text-lg text-muted-foreground">
                We will notify users of material changes to this policy via email or through notices on our website.
              </p>
            </div>
          </section>
        </div>

        <div className="mt-16 text-center border-t pt-16">
          <h2 className="text-3xl font-bold mb-6">Questions About Our Terms or Privacy Practices?</h2>
          <p className="text-xl text-muted-foreground mb-8 max-w-2xl mx-auto">
            If you have any questions or concerns about our Terms of Service or Privacy Policy, please don't hesitate to contact us.
          </p>
          <div className="flex justify-center items-center">
            <Link href="/contact" className="text-lg px-8 py-4 bg-blue-600 hover:bg-blue-700 text-white rounded-md transition-colors">
              Contact Us
            </Link>
          </div>
        </div>

      </div>
    </main>
  );
}