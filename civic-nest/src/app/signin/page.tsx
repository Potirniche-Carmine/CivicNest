"use client";
import { useState } from 'react';
const SignIn = () => {
  const [isRegistering, setIsRegistering] = useState(false);

  return (
    <div className="pt-10 flex flex-col bg-backgroundLight dark:bg-backgroundDark">
      <div className="flex-grow flex items-center justify-center p-4">
        <div className="bg-backgroundLightSlight dark:bg-backgroundDarkSlight text-foregroundLight dark:text-foregroundDark p-5 rounded shadow-md w-full max-w-md">
          <h2 className="text-2xl font-bold mb-2 text-center">
            {isRegistering ? 'Create an Account' : 'Sign In'}
          </h2>
          <form>
              <div className="mb-4">
                <label className="block text-foregroundLight dark:text-foregroundDark mb-2">Username</label>
                <input
                  type="text"
                  className="w-full px-3 py-2 border rounded"
                  placeholder="Enter your username"
                />
              </div>
            {isRegistering && (
              <div className="mb-4">
              <label className="block text-foregroundLight dark:text-foregroundDark mb-2">Email Address</label>
              <input
                type="email"
                className="w-full px-3 py-2 border rounded"
                placeholder="Enter your email"
              />
            </div>
            )}

            <div className="mb-4">
              <label className="block text-foregroundLight dark:text-foregroundDark mb-2">Password</label>
              <input
                type="password"
                className="w-full px-3 py-2 border rounded"
                placeholder="Enter your password"
              />
            </div>
            <button
              type="submit"
              className="w-full bg-blueLight dark:bg-blueDark text-white py-2 px-4 rounded hover:bg-blueDark dark:hover:bg-blueLight transition duration-200"
            >
              {isRegistering ? 'Sign Up' : 'Sign In'}
            </button>
          </form>
          <p className="mt-3 text-center">
            {isRegistering ? 'Already have an account?' : "Don't have an account?"}{' '}
            <button
              onClick={() => setIsRegistering(!isRegistering)}
              className="text-blueLight underline container"
            >
              {isRegistering ? 'Sign In' : 'Create one'}
            </button>
          </p>
        </div>
      </div>
    </div>
  );
};

export default SignIn;
