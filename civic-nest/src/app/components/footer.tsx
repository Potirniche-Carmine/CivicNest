"use client";

import { useState, useEffect } from 'react';
import { FaSun, FaMoon } from 'react-icons/fa';

const Footer = () => {
  const [darkMode, setDarkMode] = useState(false);

  useEffect(() => {
    if (darkMode) {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
  }, [darkMode]);

  return (
    <footer className="fixed bottom-0 left-0 w-full bg-blueLight dark:bg-blueDark p-4 text-foregroundLight dark:text-foregroundDark flex justify-between items-center">
      <div className="container mx-auto text-center">
        <p>&copy; 2024 CivicNest. All rights reserved.</p>
      </div>
      <button
        className="text-black dark:text-yellow-500 focus:outline-none transition-colors mr-6"
        onClick={() => setDarkMode(!darkMode)}
      >
        {darkMode ? <FaSun size={24} /> : <FaMoon size={24} />}
      </button>
    </footer>
  );
};

export default Footer;
