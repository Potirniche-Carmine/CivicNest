import NextAuth from "next-auth"
import Facebook from "next-auth/providers/facebook";
import GitHubProvider from "next-auth/providers/github"
import Google from "next-auth/providers/google"
import LinkedIn from "next-auth/providers/linkedin";
 
export const { handlers, auth } = NextAuth({
    pages: {
        signIn: "/auth/signin",
    },
    callbacks: {
        authorized({ auth, request: { nextUrl } }) {
          const isLoggedIn = !!auth?.user;
          const isOnProfile = nextUrl.pathname.startsWith('/profile');
          if (isOnProfile) {
            if (isLoggedIn) return true;
            return false; // Redirect unauthenticated users to login page
          } else if (isLoggedIn) {
            return Response.redirect(new URL('/profile', nextUrl));
          }
          return true;
        },
      },
    providers: [
        GitHubProvider({
            clientId: process.env.AUTH_GITHUB_ID,
            clientSecret: process.env.AUTH_GITHUB_SECRET,
        }),
        Google({
            clientId: process.env.AUTH_GOOGLE_ID,
            clientSecret: process.env.AUTH_GOOGLE_SECRET,
        }),
        Facebook({
            clientId: process.env.AUTH_FACEBOOK_ID,
            clientSecret: process.env.AUTH_FACEBOOK_SECRET,
        }),
    ],
    secret: process.env.AUTH_SECRET,
    
});