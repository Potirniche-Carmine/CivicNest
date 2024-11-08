"use client";

import { FaSun, FaMoon } from 'react-icons/fa';
import { useDarkMode } from '../DarkModeContext';

const Footer = () => {
  const {darkMode, toggleDarkMode} = useDarkMode();

  return (
    <footer className="w-full bg-blueLight dark:bg-blueDark p-4 text-foregroundLight dark:text-foregroundDark flex justify-between items-center">
      <div className="container mx-auto text-center">
        <p>&copy; 2024 CivicNest. All rights reserved.</p>
      </div>
      <button
        className="text-black dark:text-yellow-500 focus:outline-none transition-colors mr-6"
        onClick={toggleDarkMode}
      >
        {darkMode ? <FaSun size={24} /> : <FaMoon size={24} />}
      </button>
    </footer>
  );
};

export default Footer;
