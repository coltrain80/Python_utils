# interactive_script.py
"""
This script template allows users to input parameters via an interactive prompt.

Usage:
    Run the script in a Python environment (e.g., python interactive_script.py)
    Follow the prompts to input your parameters.

Example:
    $ python interactive_script.py
    Enter first parameter: hello
    Enter second parameter: world
    Output: Your inputs were hello and world
"""

def main():
    # Interactive input prompts
    parameter1 = input("Enter first parameter: ")
    parameter2 = input("Enter second parameter: ")

    print(f"Your inputs were {parameter1} and {parameter2}")

if __name__ == "__main__":
    main()
