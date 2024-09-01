# command_line_script.py
"""
This script template allows users to input parameters via command line arguments.

Usage:
    Run the script with command line arguments (e.g., python command_line_script.py arg1 arg2)

Example:
    $ python command_line_script.py hello world
    Output: Your inputs were hello and world
"""

import sys

def main(args):
    if len(args) != 2:
        print("Usage: python command_line_script.py <parameter1> <parameter2>")
        sys.exit(1)

    parameter1, parameter2 = args
    print(f"Your inputs were {parameter1} and {parameter2}")

if __name__ == "__main__":
    main(sys.argv[1:])
