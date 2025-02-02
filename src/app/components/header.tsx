'use client'

import { UserButton, useUser } from "@clerk/nextjs";
import Image from "next/image";
import Link from "next/link";

export function Header() {
  const { user, isSignedIn } = useUser();

  return (
    <header className="bg-zinc-400 dark:bg-zinc-800 text-white p-4 flex justify-between shadow-sm">
      <div className="p-4">
        <Link href="/" className="flex items-center">
          <Image
            src="/logo.png"
            alt="CivicNest Logo"
            width={40}
            height={40}
            className="mr-3"
          />
          <h1 className="text-2xl font-bold text-white dark:text-white">CivicNest</h1>
        </Link>
      </div>
      <div className="flex justify-end items-center gap-4">
        <div className="flex items-center gap-3 hover:bg-sky-500/50 dark:hover:bg-sky-800/50 rounded-lg transition-colors px-4 py-2">
          <UserButton
            appearance={{
              elements: {
                avatarBox: "h-10 w-10",
                userButtonPopoverCard: "shadow-xl rounded-xl",
              }
            }}
          />
          <span className="font-semibold text-sm hidden md:block text-white dark:text-white">
            {user?.username}
          </span>
        </div>
      </div>
    </header>
  );
}