interface SignInButtonProps {
  onClick: React.MouseEventHandler<HTMLButtonElement>;
  children: React.ReactNode;
}

const SignInButton: React.FC<SignInButtonProps> = ({ onClick, children }) => (
  <button
    onClick={onClick}
    className="w-full bg-blueLight dark:bg-blueDark text-foregroundLight dark:text-foregroundDark my-2 py-2 px-4 rounded hover:bg-blueDark dark:hover:bg-blueLight transition duration-200 flex items-center justify-center"
  >
    {children}
  </button>
);

export default SignInButton;
