//Official Middleware from Clerk
//https://docs.clerk.dev/nextjs/middleware

import { clerkMiddleware, createRouteMatcher } from '@clerk/nextjs/server'
import { NextResponse } from 'next/server'


const isAPIRoute = createRouteMatcher([
  '/api(.*)'
])

const isProtectedRoute = createRouteMatcher([
  '/insights(.*)'
]);

export default clerkMiddleware(async (auth, request) => {

  if (isAPIRoute(request) && request.headers.get('Sec-Fetch-Dest') === 'document' && (await auth()).sessionClaims?.metadata?.role !== 'admin') {
    const url = new URL('/home', request.url)
    return NextResponse.redirect(url)
  }

  if (isProtectedRoute(request) && (await auth()).sessionClaims?.metadata?.role !== 'admin') {
    const url = new URL('/home', request.url)
    return NextResponse.redirect(url)
  }
})

export const config = {
  matcher: [
    // Skip Next.js internals and all static files, unless found in search params
    '/((?!_next|[^?]*\\.(?:html?|css|js(?!on)|jpe?g|webp|png|gif|svg|ttf|woff2?|ico|csv|docx?|xlsx?|zip|webmanifest)).*)',
    // Always run for API routes
    '/(api|trpc)(.*)',
  ],
}