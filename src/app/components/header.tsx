'use client'

import { UserButton, useUser } from "@clerk/nextjs";
import Image from "next/image";
import Link from "next/link";
import { Button } from "./ui/button";

export function Header () {
  const { user, isSignedIn } = useUser();

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
      <div className="flex justify-end items-center gap-4">
          <div className="flex items-center gap-3 hover:bg-gray-100 dark:hover:bg-gray-800 rounded-lg transition-colors px-4 py-2">
            <UserButton
              appearance={{
                variables: {
                  colorPrimary: "#3B82F6",
                  colorText: "hsl(224 71% 4%)",
                  colorBackground: "hsl(0 0% 100%)",
                },
                elements: {
                  avatarBox: "h-10 w-10",
                  userButtonPopoverCard: "shadow-xl rounded-xl",
                }
              }}
            />
            <span className="font-semibold text-sm hidden md:block">
              {user?.fullName || user?.username}
            </span>
          </div>
      </div>
    </header>
  );
};

