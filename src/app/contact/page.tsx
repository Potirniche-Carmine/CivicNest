'use client'

import Link from "next/link";
import { Mail, Github, ArrowRight, Users, Home, Code } from 'lucide-react';

export default function ContactPage() {
  return (
    <main className="flex-1 bg-background">
      <div className="container mx-auto px-8 py-16">

        <div className="text-center mb-16 pb-8 border-b">
          <h1 className="text-4xl lg:text-5xl font-bold mb-4 bg-gradient-to-r from-blue-600 to-sky-600 inline-block text-transparent bg-clip-text">
            Contact Us
          </h1>
          <p className="text-xl max-w-3xl mx-auto text-muted-foreground">
            CivicNest was developed as a senior project by a team of developers focused on bringing data-driven insights to the Reno real estate market.
          </p>
        </div>

        <div className="max-w-3xl mx-auto">
          <section className="mb-16">
            <h2 className="text-3xl font-semibold mb-6 flex items-center">
              <Users className="mr-3 h-7 w-7 text-blue-500 flex-shrink-0" />
              About The Project
            </h2>
            <div className="pl-10 text-lg text-muted-foreground space-y-4">
              <p>
                CivicNest was created as a senior project to provide better insights into the Reno real estate market through data visualization and advanced analytics.
              </p>
              <p>
                Our team combined multiple data sources to offer a comprehensive view of the local housing market, helping users make more informed decisions about real estate in the Reno area.
              </p>
              <p>
                The platform integrates property data with demographic information, school quality metrics, and employment trends to create a holistic picture of neighborhood potential.
              </p>
            </div>
          </section>

          <section className="mb-16">
            <h2 className="text-3xl font-semibold mb-6 flex items-center">
              <Code className="mr-3 h-7 w-7 text-emerald-500 flex-shrink-0" />
              Project Resources
            </h2>
            <div className="space-y-6 pl-10">              
              {/* GitHub Project Repository */}
              <a 
                href="https://github.com/Potirniche-Carmine/CivicNest" 
                target="_blank" 
                rel="noopener noreferrer" 
                className="flex items-center p-4 border rounded-lg hover:bg-gray-50 dark:hover:bg-gray-900 transition-colors"
              >
                <Github className="h-7 w-7 text-gray-900 dark:text-white mr-4 flex-shrink-0" />
                <div>
                  <h3 className="text-lg font-medium">Project Repository</h3>
                  <p className="text-muted-foreground">github.com/Potirniche-Carmine/CivicNest</p>
                </div>
                <ArrowRight className="h-5 w-5 text-muted-foreground ml-auto" />
              </a>
            </div>
          </section>

          <section className="mb-16">
            <h2 className="text-3xl font-semibold mb-6 flex items-center">
              <Mail className="mr-3 h-7 w-7 text-amber-500 flex-shrink-0" />
              Contact Information
            </h2>
            <div className="pl-10 text-lg text-muted-foreground mb-6">
              <p>
                For questions about this project or to provide feedback, please contact the project lead:
              </p>
            </div>
            
            <div className="space-y-6 pl-10">
              {/* Email */}
              <a 
                href="mailto:potirnichecarmine@gmail.com" 
                className="flex items-center p-4 border rounded-lg hover:bg-gray-50 dark:hover:bg-gray-900 transition-colors"
              >
                <Mail className="h-7 w-7 text-blue-500 mr-4 flex-shrink-0" />
                <div>
                  <h3 className="text-lg font-medium">Carmine Potirniche</h3>
                  <p className="text-muted-foreground">potirnichecarmine@gmail.com</p>
                </div>
                <ArrowRight className="h-5 w-5 text-muted-foreground ml-auto" />
              </a>
            </div>
          </section>

          <div className="mt-16 text-center border-t pt-16">
            <h2 className="text-3xl font-bold mb-6">Explore CivicNest</h2>
            <p className="text-xl text-muted-foreground mb-8 max-w-2xl mx-auto">
              Check out our interactive map and data visualizations to better understand the Reno real estate market.
            </p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center items-center">
              <Link href="/home" className="text-lg px-8 py-4 bg-blue-600 hover:bg-blue-700 text-white rounded-md transition-colors">
                Explore The Map
              </Link>
            </div>
          </div>
        </div>
      </div>
    </main>
  );
}