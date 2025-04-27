'use client'

import { UserButton, SignedIn, SignedOut, useUser } from "@clerk/nextjs";
import Image from "next/image";
import Link from "next/link";
import { Button } from "./ui/button";
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";
import { Menu } from 'lucide-react'; 
import React from 'react';

export function Header() {
  const { user, isLoaded } = useUser();

  const navLinks = [
    { href: "/home", label: "Map & Listings" },
    { href: "/insights", label: "Market Insights" },
    { href: "/features", label: "Features" },  ];

  return (
    <header className="sticky top-0 z-50 w-full border-b border-border/40 bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
      <div className="container flex h-20 max-w-screen-2xl items-center">
        <Link href={"/"} className="mr-6 flex items-center space-x-2">
          <Image
            src="/logo.png"
            alt="CivicNest Logo"
            width={50}
            height={50}
          />
          <span className="font-bold sm:inline-block">
            CivicNest
          </span>
        </Link>

        <nav className="hidden flex-1 items-center space-x-6 text-sm font-medium md:flex">
          {navLinks.map((link) => (
            <Link
              key={link.href}
              href={link.href}
              className="transition-colors hover:text-foreground/80 text-foreground/60"
            >
              {link.label}
            </Link>
          ))}
        </nav>

        <div className="flex flex-1 items-center justify-end space-x-4 md:hidden">
          <DropdownMenu>
            <DropdownMenuTrigger asChild>
              <Button variant="ghost" size="icon">
                <Menu className="h-5 w-5" />
                <span className="sr-only">Toggle Menu</span>
              </Button>
            </DropdownMenuTrigger>
            <DropdownMenuContent align="end" className="w-56 mt-2">
              {navLinks.map((link) => (
                <DropdownMenuItem key={link.href} asChild>
                  <Link href={link.href}>
                    {link.label}
                  </Link>
                </DropdownMenuItem>
              ))}

              <DropdownMenuSeparator />

              <SignedIn>
              {isLoaded && (
              <div className="flex items-left gap-3 hover:bg-sky-500/50 dark:hover:bg-sky-800/50 rounded-lg transition-colors px-4 py-2">
                <span className="text-sm font-small sm:inline">
                  Welcome, {user?.username}!
                </span>
                <UserButton
                  appearance={{
                    elements: {
                      avatarBox: "h-7 w-7",
                      userButtonPopoverCard: "shadow-xl rounded-xl",
                    }
                  }}
                />
              </div>
            )}
              </SignedIn>
              <SignedOut>
                <DropdownMenuItem asChild>
                  <Link href="/auth/sign-up">Sign Up</Link>
                </DropdownMenuItem>
                <DropdownMenuItem asChild>
                  <Link href="/auth/sign-in">Sign In</Link>
                </DropdownMenuItem>
              </SignedOut>
            </DropdownMenuContent>
          </DropdownMenu>
        </div>

        <div className="hidden flex-initial items-center justify-end space-x-2 md:flex">
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
            <Link href="/auth/sign-in">
              <Button variant="ghost" size="sm">
                Sign In
              </Button>
            </Link>
            <Link href="/auth/sign-up">
              <Button variant="outline" size="sm">
                Sign Up
              </Button>
            </Link>
          </SignedOut>
        </div>
      </div>
    </header>
  );
}