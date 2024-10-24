"use client";

import { useState, useEffect } from 'react';
import { FaSun, FaMoon } from 'react-icons/fa';

const Header = () => {
  const [darkMode, setDarkMode] = useState(false);

  useEffect(() => {
    if (darkMode) {
      document.documentElement.classList.add('dark');
    } else {
      document.documentElement.classList.remove('dark');
    }
  }, [darkMode]);

  return (
    <header className="bg-blueLight dark:bg-blueDark p-6 flex justify-between items-center">
      <div className="container mx-auto">
        <h1 className="text-3xl font-bold">CivicNest</h1>
      </div>
      <button
        className="text-black dark:text-yellow-500 focus:outline-none transition-colors"
        onClick={() => setDarkMode(!darkMode)}
      >
        {darkMode ? <FaSun size={24} /> : <FaMoon size={24} />}
      </button>
    </header>
  );
};

export default Header;
