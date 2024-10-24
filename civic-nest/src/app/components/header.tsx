"use client";
import Image from 'next/image'

const Header = () => {

  return (
    <header className="bg-blueLight dark:bg-blueDark p-6 flex justify-between items-center">
      <div className="container mx-auto flex items-center">
        <Image
        src = "/logo.png"
        alt="CivicNest Logo"
        width = {50}
        height = {50}
        className='mr-2'
        />
        <h1 className="text-3xl font-bold">CivicNest</h1>
      </div>

    </header>
  );
};

export default Header;
