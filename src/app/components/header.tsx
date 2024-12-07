'use client'

import { useSession, signOut } from "next-auth/react";
import Image from "next/image";
import Link from "next/link";

const Header = () => {
  const { data: session } = useSession();

  return (
    <header className="bg-blueLight dark:bg-blueDark p-6 flex justify-between">
      <div className="flex-1 flex items-start">
        <Link href="/" className="flex items-center">
          <Image
            src="/logo.png"
            alt="CivicNest Logo"
            width={40}
            height={40}
            className="mr-3"
          />
          <h1 className="text-2xl font-bold">CivicNest</h1>
        </Link>
      </div>
      <div className="flex justify-end items-center">
        {session?.user ? (
          <>
          <Link href="/profile">
            <Image
              src={session.user.image || "/default-profile.png"} 
              alt="Profile Picture"
              width={40}
              height={40}
              className="rounded-full mr-3"
            />
          </Link>
            <button
              onClick={() => signOut()}
              className="
                bg-backgroundLight text-blueLight font-semibold rounded-md
                hover:bg-blueDark dark:hover:bg-blueLight dark:hover:text-foregroundDark
                py-2 px-4 mx-1 md:mx-7
              "
            >
              Sign Out
            </button>
          </>
        ) : (
          // Display "Sign In" button if user is not signed in
          <Link href="/signin">
            <button
              className="
                bg-backgroundLight text-blueLight font-semibold rounded-md
                hover:bg-blueDark dark:hover:bg-blueLight dark:hover:text-foregroundDark
                py-2 px-4 mx-1 md:mx-7
              "
            >
              Sign In
            </button>
          </Link>
        )}
      </div>
    </header>
  );
};

export default Header;
