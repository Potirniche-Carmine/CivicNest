import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        backgroundDark: '#4a5e6c',
        backgroundDarkSlight: '#516878',
        backgroundLight: '#ffffff',
        backgroundLightSlight: '#f2f2f2',
        foregroundLight: '#121111',
        foregroundDark: '#fdfaff',
        blueLight: '#59d4ff',
        blueDark: '#0c5a8f',
      },
    },
  },
  plugins: [],
};
export default config;
