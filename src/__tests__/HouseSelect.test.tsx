import '@testing-library/jest-dom';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import HouseSelect, { houses } from '@/app/components/house_select';
import * as themes from 'next-themes';

// Mock fetch
global.fetch = jest.fn();

// Mock next-themes
jest.mock('next-themes');
const mockedUseTheme = jest.mocked(themes.useTheme);

describe('HouseSelect Component', () => {
  const mockHouses: houses[] = [
    { address: '123 Main St', lat: 40.7128, long: -74.0060, price: 500000, zpid: 1 },
    { address: '456 Elm St', lat: 34.0522, long: -118.2437, price: 750000, zpid: 2 },
    { address: '789 Oak Ave', lat: 41.8781, long: -87.6298, price: 600000, zpid: 3 },
  ];

  const mockOnSelect = jest.fn();

  beforeEach(() => {
    jest.clearAllMocks();
    
    // Mock the fetch response
    (global.fetch as jest.Mock).mockResolvedValue({
      ok: true,
      json: async () => ({ houses: mockHouses }),
    });

    // Mock the theme hook
    mockedUseTheme.mockReturnValue({ 
      theme: 'light', 
      systemTheme: 'light',
      setTheme: jest.fn(),
      resolvedTheme: 'light',
      themes: ['light', 'dark', 'system']
    } as any);
  });

  it('renders with loading state initially', () => {
    render(<HouseSelect onSelect={mockOnSelect} />);
    
    const input = screen.getByPlaceholderText('Loading houses...');
    expect(input).toBeInTheDocument();
    expect(input).toBeDisabled();
  });

  it('fetches houses on mount and updates state', async () => {
    render(<HouseSelect onSelect={mockOnSelect} />);
    
    // Wait for the loading state to finish
    await waitFor(() => {
      expect(global.fetch).toHaveBeenCalledWith('/api/locations');
      expect(screen.getByPlaceholderText('Search houses...')).toBeInTheDocument();
    });
  });

  it('filters houses based on search input', async () => {
    render(<HouseSelect onSelect={mockOnSelect} />);
    
    await waitFor(() => {
      expect(screen.getByPlaceholderText('Search houses...')).toBeInTheDocument();
    });
    
    const input = screen.getByPlaceholderText('Search houses...');
    fireEvent.focus(input);
    fireEvent.change(input, { target: { value: 'elm' } });
    
    await waitFor(() => {
      expect(screen.getByText('456 Elm St')).toBeInTheDocument();
      expect(screen.queryByText('123 Main St')).not.toBeInTheDocument();
    });
  });

  it('calls onSelect when a house is selected', async () => {
    render(<HouseSelect onSelect={mockOnSelect} />);
    
    await waitFor(() => {
      expect(screen.getByPlaceholderText('Search houses...')).toBeInTheDocument();
    });
    
    const input = screen.getByPlaceholderText('Search houses...');
    fireEvent.focus(input);
    fireEvent.change(input, { target: { value: 'main' } });
    
    await waitFor(() => {
      expect(screen.getByText('123 Main St')).toBeInTheDocument();
    });
    
    fireEvent.click(screen.getByText('123 Main St'));
    
    expect(mockOnSelect).toHaveBeenCalledWith(mockHouses[0]);
    expect(input).toHaveValue('123 Main St');
  });

  it('shows dropdown when input is focused and has value', async () => {
    render(<HouseSelect onSelect={mockOnSelect} />);
    
    await waitFor(() => {
      expect(screen.getByPlaceholderText('Search houses...')).toBeInTheDocument();
    });
    
    const input = screen.getByPlaceholderText('Search houses...');
    fireEvent.focus(input);
    fireEvent.change(input, { target: { value: 'a' } });
    
    await waitFor(() => {
      expect(screen.getByText('123 Main St')).toBeInTheDocument();
      expect(screen.getByText('789 Oak Ave')).toBeInTheDocument();
    });
  });

  it('displays "No houses found" when search has no matches', async () => {
    render(<HouseSelect onSelect={mockOnSelect} />);
    
    await waitFor(() => {
      expect(screen.getByPlaceholderText('Search houses...')).toBeInTheDocument();
    });
    
    const input = screen.getByPlaceholderText('Search houses...');
    fireEvent.focus(input);
    fireEvent.change(input, { target: { value: 'xyz' } });
    
    await waitFor(() => {
      expect(screen.getByText('No houses found')).toBeInTheDocument();
    });
  });

  it('handles API error gracefully', async () => {
    // Mock a failed API response
    (global.fetch as jest.Mock).mockResolvedValue({
      ok: false,
      status: 500
    });
    
    render(<HouseSelect onSelect={mockOnSelect} />);
    
    await waitFor(() => {
      expect(screen.getByPlaceholderText('Search houses...')).toBeInTheDocument();
    });
    
    const input = screen.getByPlaceholderText('Search houses...');
    fireEvent.focus(input);
    fireEvent.change(input, { target: { value: 'a' } });
    
    await waitFor(() => {
      expect(screen.getByText('No houses found')).toBeInTheDocument();
    });
  });

  it('applies dark mode styling when theme is dark', async () => {
    // Mock dark theme
    mockedUseTheme.mockReturnValue({ 
      theme: 'dark', 
      systemTheme: 'dark',
      setTheme: jest.fn(),
      resolvedTheme: 'dark',
      themes: ['light', 'dark', 'system']
    } as any);
    
    render(<HouseSelect onSelect={mockOnSelect} />);
    
    await waitFor(() => {
      expect(screen.getByPlaceholderText('Search houses...')).toBeInTheDocument();
    });
    
    const input = screen.getByPlaceholderText('Search houses...');
    fireEvent.focus(input);
    fireEvent.change(input, { target: { value: 'a' } });
    
    await waitFor(() => {
      const dropdown = screen.getByText('123 Main St').closest('div');
      expect(dropdown?.parentElement).toHaveClass('bg-card');
      expect(dropdown?.parentElement).toHaveClass('text-card-foreground');
    });
  });

  it('applies system theme when theme is set to system', async () => {
    // Mock system theme as dark
    mockedUseTheme.mockReturnValue({ 
      theme: 'system', 
      systemTheme: 'dark',
      setTheme: jest.fn(),
      resolvedTheme: 'dark',
      themes: ['light', 'dark', 'system']
    } as any);
    
    render(<HouseSelect onSelect={mockOnSelect} />);
    
    await waitFor(() => {
      expect(screen.getByPlaceholderText('Search houses...')).toBeInTheDocument();
    });
    
    const input = screen.getByPlaceholderText('Search houses...');
    fireEvent.focus(input);
    fireEvent.change(input, { target: { value: 'a' } });
    
    await waitFor(() => {
      const dropdown = screen.getByText('123 Main St').closest('div');
      expect(dropdown?.parentElement).toHaveClass('bg-card');
      expect(dropdown?.parentElement).toHaveClass('text-card-foreground');
    });
  });

  it('handles invalid response format gracefully', async () => {
    // Mock a response with incorrect format
    (global.fetch as jest.Mock).mockResolvedValue({
      ok: true,
      json: async () => ({ notHouses: 'wrong format' }),
    });
    
    render(<HouseSelect onSelect={mockOnSelect} />);
    
    await waitFor(() => {
      expect(screen.getByPlaceholderText('Search houses...')).toBeInTheDocument();
    });
    
    const input = screen.getByPlaceholderText('Search houses...');
    fireEvent.focus(input);
    fireEvent.change(input, { target: { value: 'a' } });
    
    await waitFor(() => {
      expect(screen.getByText('No houses found')).toBeInTheDocument();
    });
  });
});

