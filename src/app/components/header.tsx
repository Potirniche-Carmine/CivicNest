'use client'

import { UserButton, useUser } from "@clerk/nextjs";
import Image from "next/image";
import Link from "next/link";
import { Button } from "./ui/button";

const Header = () => {
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
      <div className="flex justify-end items-center">
        {isSignedIn ?
        <UserButton />
        :
        <Link href={"/signin"}>
        <Button>Login</Button>
        </Link> 
        }
      </div>
    </header>
  );
};

export default Header;
