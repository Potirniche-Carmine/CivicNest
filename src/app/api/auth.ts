import NextAuth from "next-auth"
import GitHubProvider from "next-auth/providers/github"
import Google from "next-auth/providers/google"
 
export const { handlers, auth } = NextAuth({
    providers: [
        GitHubProvider({
            clientId: process.env.AUTH_GITHUB_ID,
            clientSecret: process.env.AUTH_GITHUB_SECRET,
        }),
        Google({
            clientId: process.env.AUTH_GOOGLE_ID,
            clientSecret: process.env.AUTH_GOOGLE_SECRET,
        })
    ],
    secret: process.env.AUTH_SECRET,
    
});