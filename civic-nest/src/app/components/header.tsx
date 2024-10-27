"use client";
import Image from 'next/image'
import Link from 'next/link'

const Header = () => {

  return (
    <header className="bg-blueLight dark:bg-blueDark p-6 flex justify-between items-center">
      <div className="container mx-auto flex items-center">
        <Link href = "/" className = "flex items-center">
        <Image
        src = "/logo.png"
        alt="CivicNest Logo"
        width = {50}
        height = {50}
        className='mr-2'
        />
        <h1 className="text-3xl font-bold">CivicNest</h1>
        </Link>
      </div>
      <div>
        <Link href="/signin">
          <button className="bg-backgroundLight text-blueLight font-semibold py-2 px-4 rounded hover:bg-blueDark dark:hover:bg-blueLight dark:hover:text-foregroundDark">
            Sign In
          </button>
        </Link>
      </div>

    </header>
  );
};

export default Header;
