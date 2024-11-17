import { NextResponse } from 'next/server'
import { getToken } from 'next-auth/jwt'
import type { NextRequest } from 'next/server'

export async function middleware(req: NextRequest) {
  const session = await getToken({ req, secret: process.env.AUTH_SECRET })
  const isLoggedIn = !!session
  const { pathname } = req.nextUrl

  const isOnProfile = pathname.startsWith('/profile')

  if (isOnProfile) {
    if (isLoggedIn) {
      // Allow access to /profile if the user is authenticated
      return NextResponse.next()
    } else {
      // Redirect unauthenticated users to the sign-in page
      return NextResponse.redirect(new URL('/auth/signin', req.url))
    }
  } else if (isLoggedIn && !pathname.startsWith('/api/auth')) {
    // Redirect authenticated users to /profile when accessing other routes
    return NextResponse.redirect(new URL('/profile', req.url))
  }

  // Allow unauthenticated users to access other routes
  return NextResponse.next()
}

export const config = {
  matcher: ['/profile/:path*', '/((?!_next/static|_next/image|favicon.ico).*)'],
}
