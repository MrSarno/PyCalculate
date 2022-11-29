#!/usr/bin/env python3


# specify imports

import os
import sys


# define constants

VERSION = "1.0"
INDENT = "     "


# write functions

def greet_user():
    """Print some initial text to the screen; request user's name."""
    print("\n\n", INDENT, "Welcome to PyCalculate, version " + VERSION + ".")
    user_name = input(INDENT + "  Please enter your name to continue: ")
    return user_name


def request_input():
    """Ask user for numbers and an operator."""
    number_1 = int(input("\n\n" + INDENT + "Please enter the first number: "))
    number_2 = int(input(INDENT + "Please enter the second number: "))
    operator_1 = str(input(INDENT + "Please enter + to add the numbers, - to subtract the second number from the first,"
                                    " x to multiply the numbers, or / to divide the first number by the second. "))

    # store user input in a dictionary to have a single object for the function to return
    user_input = {"first_number": number_1, "second_number": number_2, "operator": operator_1}

    return user_input


def do_calculations(user_input):
    """This function performs the calculations & presents the result to the user."""
    number_1 = int(user_input.get("first_number"))
    number_2 = int(user_input.get("second_number"))

    if user_input.get("operator").__eq__("+"):
        clear_screen()
        print("\n\n", INDENT, number_1, user_input.get("operator"), number_2, "=", number_1 + number_2)
    elif user_input.get("operator").__eq__("-"):
        clear_screen()
        print("\n\n", INDENT, number_1, user_input.get("operator"), number_2, "=", number_1 - number_2)
    elif user_input.get("operator").__eq__("x"):
        clear_screen()
        print("\n\n", INDENT, number_1, user_input.get("operator"), number_2, "=", number_1 * number_2)
    elif user_input.get("operator").__eq__("/"):
        clear_screen()
        print("\n\n", INDENT, number_1, user_input.get("operator"), number_2, "=", number_1 / number_2)
    else:
        print("ERROR: Unknown operation selected.")


def clear_screen():
    """Clears the screen, regardless of the OS."""
    os.system("cls" if os.name == "nt" else "clear")


def quit_calculator():
    """Bring the program to an end."""
    input(INDENT + "  Press Enter to close...")
    sys.exit()


# run program

if __name__ == '__main__':
    greet_user()
    clear_screen()
    user_input = request_input()
    do_calculations(user_input)
    quit_calculator()
