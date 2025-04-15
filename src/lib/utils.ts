//Automatically from shadcn
import { clsx, type ClassValue } from "clsx"
import { twMerge } from "tailwind-merge"

export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs))
}

export const generateClusterColors = () => {
  return [
      '#3366CC', // Blue
      '#DC3912', // Red
      '#FF9900', // Orange
      '#109618', // Green
      '#990099', // Purple
      '#0099C6', // Teal
      '#DD4477', // Pink
      '#66AA00', // Lime
      '#B82E2E', // Dark Red
      '#316395', // Dark Blue
      '#994499', // Dark Purple
      '#22AA99'  // Dark Teal
  ];
};

export const formatPrice = (price: number): string => {
  return new Intl.NumberFormat('en-US', {
      style: 'currency',
      currency: 'USD',
      minimumFractionDigits: 0,
      maximumFractionDigits: 0
  }).format(price);
};
