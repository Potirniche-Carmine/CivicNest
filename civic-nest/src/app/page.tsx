"use client";

import { NextPage } from 'next';
import Header from '@/app/components/header'
import Footer from '@/app/components/footer'

const Home: NextPage = () => {
  return (
    <div className="min-h-screen flex flex-col justify-between bg-backgroundLight dark:bg-backgroundDark text-foregroundLight dark:text-foregroundDark transition-colors">
      <Header />
      <main className="flex-grow container mx-auto p-6">
        <section className="bg-backgroundLight dark:bg-backgroundDark p-8 rounded-lg shadow-lg transition-colors">
          <h2 className="text-2xl font-semibold mb-4">Discover Your Ideal Neighborhood</h2>
          <p className="mb-6">
          </p>
          <button className="px-5 py-3 bg-blueLight dark:bg-blueDark text-foregroundLight dark:text-foregroundDark rounded-lg hover:bg-blueDark dark:hover:bg-blueLight transition-colors">
            Explore Now
          </button>
        </section>
      </main>

      <Footer />
    </div>
  );
};

export default Home;
