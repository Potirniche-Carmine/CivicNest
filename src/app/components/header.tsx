'use client'

import { UserButton, SignedIn, SignedOut, useUser} from "@clerk/nextjs";
import Image from "next/image";
import Link from "next/link";
import { Button } from "./ui/button";

export function Header() {
  const { user, isLoaded } = useUser();

  return (
    <header className="bg-zinc-600 dark:bg-zinc-800 text-white p-5">
      <div className="relative w-full max-w-[2560px] mx-auto flex flex-wrap items-center justify-between">
        <div>
          <Link href={user ? "/home" : "/"} className="flex items-center px-5">
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
        <div className="flex items-center">
          <SignedIn>
            {isLoaded && (
              <div className="flex items-center gap-3 hover:bg-sky-500/50 dark:hover:bg-sky-800/50 rounded-lg transition-colors px-4 py-2">
                <span className="text-sm font-medium hidden sm:inline">
                  Welcome, {user?.username}!
                </span>
                <UserButton
                  appearance={{
                    elements: {
                      avatarBox: "h-10 w-10",
                      userButtonPopoverCard: "shadow-xl rounded-xl",
                    }
                  }}
                />
              </div>
            )}
          </SignedIn>
          <SignedOut>
            <div>
              <Button
                className="text-black dark:text-white whitespace-nowrap"
                variant={'outline'}
                size={'lg'}
              >
                <Link href="/auth/sign-in">Sign In</Link>
              </Button>
            </div>
          </SignedOut>
        </div>
      </div>
    </header>
  );
}