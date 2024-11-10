"use client";
import { useSession } from "next-auth/react";
import { useRouter } from "next/navigation";
import Image from "next/image";
import { useEffect } from "react";

const Profile = () => {
  const { data: session } = useSession();
  const router = useRouter();

  useEffect(() => {
    // Redirect to the sign-in page if user is not authenticated
    if (!session?.user) {
      router.push("/signin");
    }
  }, [session, router]);

  // Show nothing if the user isnt logged in or we are just waiting for the page to respond
  if (!session?.user) return null;

  return (
    <div className="pt-10 flex flex-col bg-backgroundLight dark:bg-backgroundDark min-h-screen">
      <div className="flex-grow flex items-center justify-center p-4">
        <div className="bg-backgroundLightSlight dark:bg-backgroundDarkSlight text-foregroundLight dark:text-foregroundDark p-5 rounded shadow-md w-full max-w-md">
          <h2 className="text-2xl font-bold mb-4 text-center">Profile</h2>

          <div className="text-center">
            <Image
              src={session.user.image || "/default-profile.png"}
              alt={`${session.user.name}'s avatar`}
              width={96}
              height={96}
              className="w-24 h-24 rounded-full mx-auto mb-4"
            />
            <h3 className="text-xl font-semibold">{session.user.name}</h3>
            <p className="text-sm text-gray-600 dark:text-gray-400">
              {session.user.email}
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Profile;
