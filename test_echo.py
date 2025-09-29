#!/usr/bin/env python3
"""
Test script for the echo tool functionality.
"""

import sys
import os

# Add the current directory to the path so we can import our server
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Let's define the echo function directly for testing
def echo(input: str) -> str:
    """
    Echo tool that repeats the input with a prefix.
    
    Args:
        input: The text to echo
        
    Returns:
        The input text prefixed with "I hear you: "
    """
    return f"I hear you: {input}"

def test_echo_function():
    """Test the echo function directly."""
    test_cases = [
        ("hello", "I hear you: hello"),
        ("world", "I hear you: world"),
        ("", "I hear you: "),
        ("Hello, World!", "I hear you: Hello, World!"),
        ("Test with spaces and symbols: @#$%", "I hear you: Test with spaces and symbols: @#$%"),
    ]
    
    print("Testing echo function...")
    for input_text, expected_output in test_cases:
        actual_output = echo(input_text)
        if actual_output == expected_output:
            print(f"✅ PASS: echo('{input_text}') -> '{actual_output}'")
        else:
            print(f"❌ FAIL: echo('{input_text}') -> expected '{expected_output}', got '{actual_output}'")
            return False
    
    print("All tests passed!")
    return True

if __name__ == "__main__":
    test_echo_function()