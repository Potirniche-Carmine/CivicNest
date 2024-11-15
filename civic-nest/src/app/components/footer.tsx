"use client";

import { FaSun, FaMoon } from 'react-icons/fa';
import { useDarkMode } from '../DarkModeContext';
import Link from 'next/link';

const Footer = () => {
  const {darkMode, toggleDarkMode} = useDarkMode();

  return (
    <footer className="w-full bg-blueLight dark:bg-blueDark p-4 text-foregroundLight dark:text-foregroundDark flex justify-center">
      <Link href='/policy' className= "flex-1 flex justify-center">
        <div className="">
          <p>&copy; 2024 CivicNest. All rights reserved.</p>
        </div>
      </Link>
      <button
        className="justify-end text-black dark:text-yellow-500 focus:outline-none transition-colors mr-6"
        onClick={toggleDarkMode}
      >
        {darkMode ? <FaSun size={24} /> : <FaMoon size={24} />}
      </button>
    </footer>
  );
};

export default Footer;
