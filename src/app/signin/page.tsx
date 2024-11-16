"use client"
import { signIn, useSession } from "next-auth/react";
import { useRouter } from "next/navigation";
import { useEffect } from "react";

const SignIn = () => {
  const { data: session } = useSession(); // Get session data
  const router = useRouter();

  useEffect(() => {
    // Automatically redirect to the main page if already signed in
    if (session) {
      router.push("/");
    }
  }, [session, router]);

  // Sign in with different providers and redirect to the homepage after success

  const handleGoogleSignIn = async() => {
    await signIn("google", {callbackUrl: "/"});
  };

  const handleGitHubSignIn = async () => {
    await signIn("github", { callbackUrl: "/" });
  };

  return (
    <div className="pt-10 flex flex-col bg-backgroundLight dark:bg-backgroundDark">
      <div className="flex-grow flex items-center justify-center p-4">
        <div className="bg-backgroundLightSlight dark:bg-backgroundDarkSlight text-foregroundLight dark:text-foregroundDark p-5 rounded shadow-md w-full max-w-md">
          <h2 className="text-2xl font-bold mb-4 text-center">Sign In</h2>

          <button
            onClick={handleGoogleSignIn}
            className="w-full bg-blueLight dark:bg-blueDark text-foregroundLight dark:text-foregroundDark my-5 py-2 px-4 rounded hover:bg-blueDark dark:hover:bg-blueLight transition duration-200 flex items-center justify-center"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 24 24"
              fill="currentColor"
              className="w-5 h-5 mr-2"
            >
              <path d="M21.35 11.1H12v2.77h5.37c-.23 1.16-.95 2.14-1.96 2.77v2.3h3.16c1.85-1.7 2.93-4.18 2.93-6.94 0-.5-.04-.98-.15-1.43z"/>
              <path d="M12 22c2.4 0 4.38-.8 5.85-2.13l-3.16-2.3c-.83.55-1.87.88-2.99.88a5.93 5.93 0 0 1-5.58-3.9H3.75v2.4A9.93 9.93 0 0 0 12 22z"/>
              <path d="M6.42 13.55A5.94 5.94 0 0 1 6 12c0-.53.09-1.05.22-1.55V8.05H3.75A9.97 9.97 0 0 0 2 12c0 1.62.38 3.16 1.04 4.55l3.38-2.29z"/>
              <path d="M12 6.17c1.3 0 2.48.45 3.42 1.34l2.52-2.52A9.93 9.93 0 0 0 12 2 9.93 9.93 0 0 0 6.03 5.44l3.38 2.3A5.91 5.91 0 0 1 12 6.17z"/>
            </svg>
            Sign in using Google
          </button>
          
          <button
            onClick={handleGitHubSignIn}
            className="w-full bg-blueLight dark:bg-blueDark text-foregroundLight dark:text-foregroundDark py-2 px-4 rounded hover:bg-blueDark dark:hover:bg-blueLight transition duration-200 flex items-center justify-center"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              viewBox="0 0 24 24"
              fill="currentColor"
              className="w-5 h-5 mr-2"
            >
              <path d="M12 .5C5.73.5.5 5.73.5 12c0 5.09 3.29 9.4 7.86 10.94.58.1.77-.25.77-.55v-2.06c-3.18.69-3.87-1.38-3.87-1.38-.52-1.32-1.27-1.67-1.27-1.67-1.04-.72.08-.7.08-.7 1.15.08 1.76 1.18 1.76 1.18 1.02 1.75 2.68 1.24 3.33.95.1-.74.4-1.24.72-1.52-2.54-.29-5.21-1.28-5.21-5.68 0-1.25.45-2.26 1.18-3.06-.12-.29-.52-1.45.11-3.02 0 0 .96-.31 3.15 1.18.91-.25 1.88-.38 2.85-.39.97.01 1.94.14 2.85.39 2.18-1.49 3.15-1.18 3.15-1.18.64 1.57.24 2.73.12 3.02.73.8 1.18 1.81 1.18 3.06 0 4.4-2.68 5.38-5.23 5.67.41.36.76 1.09.76 2.2v3.26c0 .31.2.66.78.55 4.57-1.54 7.85-5.85 7.85-10.94C23.5 5.73 18.27.5 12 .5z" />
            </svg>
            Sign in using GitHub
          </button>
                 
        </div>
      </div>
    </div>
  );
};

export default SignIn;
