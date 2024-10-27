"use client";

import { NextPage } from 'next';
import { Map } from '@/app/components/map';

const Home: NextPage = () => {
  return (
    <div className="container mx-auto p-6">
        <Map />
    </div>
  );
};
export default Home;
