'use client';
import { useState } from 'react';
import { useRouter } from 'next/navigation';
import { Button } from '@/app/components/ui/button';
import {UserRoundPlus } from "lucide-react";
import { NextPage } from 'next';
import { Map } from '@/app/components/map';

export default function AddLocationsPage(){
  const router = useRouter();
  const [lat, setLat] = useState('');
  const [long, setLong] = useState('');
  const [address, setAddress] = useState('');
  const [errorMsg, setErrorMsg] = useState('');

  async function handleSubmit(e: React.FormEvent<HTMLFormElement>){
    e.preventDefault();
    setErrorMsg('');

    try{
      const res = await fetch('/api/locations', {
        method: 'POST',
        headers:{
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({lat, long})
      });

      if(!res.ok){
        const errorData = await res.json();
        setErrorMsg(errorData.error || 'Something went wrong');
      } else {
        router.push('/admin/dashboard');
      }
    } catch (err){
      setErrorMsg('An unexpected error occured');
      console.error(err);
    } finally {

    }
  }

  return (
    <div className="p-8 max-w-md mx-auto">
      <h1 className="text-2xl font-bold mb-4">Search or update a house</h1>
      {errorMsg && (
        <p className="text-red-600 mb-4">
          {errorMsg}
        </p>
      )
      }
      <form onSubmit={handleSubmit} className="space-y-4">
        <div>
          <label className="block font-semibold mb-1" htmlFor="lat">
            House Address
          </label>
          <input
            id="houseLat"
            type="text"
            className="border rounded w-full p-2"
            value={lat}
            onChange={(e) =>setLat(e.target.value)}
            placeholder="e.g. 0.0"
            required
          />
        </div>
        <div>
        <label className="block font-semibold mb-1" htmlFor="long">
            House Longitude
          </label>
          <input
            id="long"
            type="text"
            className="border rounded w-full p-2"
            value={long}
            onChange={(e) => setLong(e.target.value)}
            placeholder="e.g. 2.5"
          />
        </div>
        <div>
          <label className="block font-semibold mb-1" htmlFor="houseAddress">
            House address
          </label>
          <input
            id="houseAddress"
            type="text"
            className="border rounded w-full p-2"
            value={address}
            onChange={(e) => setAddress(e.target.value)}
            placeholder = "e.g. 123 Main St."
            />
        </div>
        <Button
        className="w-full">
          <UserRoundPlus/> Add/Update House
        </Button>
      </form>
    </div>
  )
}

const Home: NextPage = () => {
  return (
    <div className="container mx-auto px-12 py-4">
        <Map />
    </div>
  );
};

