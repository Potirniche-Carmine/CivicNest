'use client'
import { SignIn, SignUp } from "@clerk/nextjs";
import { usePathname } from "next/navigation";
import { useTheme } from "next-themes";
import { useEffect, useState } from "react";

export default function AuthPage() {
  const pathname = usePathname();
  const { theme } = useTheme();
  const [mounted, setMounted] = useState(false);

  useEffect(() => {
    setMounted(true);
  }, []);

  if (!mounted) {
    return null;
  }

  const isDarkMode = theme === 'dark';

  const clerkAppearance = {
    variables: {
      colorPrimary: '#3b82f6', 
      colorText: isDarkMode ? '#f3f4f6' : '#1f2937', 
      colorBackground: isDarkMode ? '#1e293b' : '#ffffff', 
      colorInputBackground: isDarkMode ? '#334155' : '#f8fafc', 
      colorInputText: isDarkMode ? '#f3f4f6' : '#1f2937', 
      colorAlphaShade: isDarkMode ? '#94a3b8' : '#475569', 
    },
    elements: {
      card: `shadow-lg ${isDarkMode ? 'bg-zinc-600' : 'bg-white'}`,  
      headerTitle: isDarkMode ? 'text-gray-100' : 'text-gray-900',
      headerSubtitle: isDarkMode ? 'text-gray-300' : 'text-gray-600',
      socialButtonsBlockButton: isDarkMode ? 'bg-slate-700 hover:bg-slate-600' : 'bg-gray-50 hover:bg-gray-100',
      socialButtonsBlockButtonText: isDarkMode ? 'text-gray-100' : 'text-gray-900',
      dividerLine: isDarkMode ? 'bg-zinc-800' : 'bg-gray-200',
      dividerText: isDarkMode ? 'text-gray-300' : 'text-gray-600',
      formFieldLabel: isDarkMode ? 'text-gray-200' : 'text-gray-700',
      formFieldInput: isDarkMode ? 'bg-zinc-800 text-gray-100 border-slate-600' : 'bg-white text-gray-900 border-gray-300',
      footerActionLink: isDarkMode ? 'text-blue-400 hover:text-blue-300' : 'text-blue-600 hover:text-blue-500',
      formButtonPrimary: isDarkMode ? 'bg-blue-600 hover:bg-blue-500 text-white' : 'bg-blue-600 hover:bg-blue-700 text-white',
      identityPreviewText: isDarkMode ? 'text-gray-100' : 'text-gray-900',
    },
  };

  return (
    <main className="flex-1 flex items-center justify-center bg-background">
      <div className="py-12">
        {pathname.startsWith('/auth/sign-in') ? (
          <SignIn
            path="/auth/sign-in"
            routing="path"
            appearance={clerkAppearance}
            forceRedirectUrl="/home"
          />
        ) : (
          <SignUp
            path="/auth/sign-up"
            routing="path"
            appearance={clerkAppearance}
            forceRedirectUrl="/home"
          />
        )}
      </div>
    </main>
  );
}