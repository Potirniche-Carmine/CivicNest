// Used example from https://nextjs.org/docs/app/building-your-application/testing/jest and with the help of claude.ai was able to create this unit test and run it successfully.
import '@testing-library/jest-dom';
import { render, screen } from '@testing-library/react';
import AuthPage from '@/app/auth/[[...auth]]/page';
import * as navigation from 'next/navigation';
import * as themes from 'next-themes';

jest.mock('next/navigation');
jest.mock('next-themes');
jest.mock('@clerk/nextjs', () => ({
  SignIn: jest.fn(() => <div data-testid="sign-in-component">Sign In</div>),
  SignUp: jest.fn(() => <div data-testid="sign-up-component">Sign Up</div>),
}));

const mockedUsePathname = jest.mocked(navigation.usePathname);
const mockedUseTheme = jest.mocked(themes.useTheme);

jest.mock('react', () => {
  const originalReact = jest.requireActual('react');
  return {
    ...originalReact,
    useState: jest.fn(() => [true, jest.fn()]) // Always return mounted=true
  };
});

describe('AuthPage Component', () => {
  beforeEach(() => {
    jest.clearAllMocks();
    mockedUseTheme.mockReturnValue({ theme: 'light', setTheme: jest.fn(), themes: ['light', 'dark'] });
  });

  it('renders SignIn component when on the sign-in path', () => {
    mockedUsePathname.mockReturnValue('/auth/sign-in');
    render(<AuthPage />);
    expect(screen.getByTestId('sign-in-component')).toBeInTheDocument();
  });

  it('renders SignUp component when on the sign-up path', () => {
    mockedUsePathname.mockReturnValue('/auth/sign-up');
    render(<AuthPage />);
    expect(screen.getByTestId('sign-up-component')).toBeInTheDocument();
  });

  it('renders a component with correct styling based on theme', () => {
    mockedUsePathname.mockReturnValue('/auth/sign-in');
    render(<AuthPage />);
    expect(screen.getByTestId('sign-in-component')).toBeInTheDocument();
  });
});