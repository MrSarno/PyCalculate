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
    clear_screen()
    print("\n\n", INDENT, "Welcome to PyCalculate, version " + VERSION + ".")


def request_input():
    """Ask user for numbers and an operator."""
    number_1 = int(input("\n\n" + INDENT + "  Please enter the first number: "))
    number_2 = int(input(INDENT + "  Please enter the second number: "))
    operator_1 = str(input(INDENT + "  Please enter + to add the numbers, - to subtract the second number from the first,"
                                    " x to multiply the numbers, or / to divide the first number by the second. "))

    # store user input in a dictionary to have a single object for the function to return
    user_input = {"first_number": number_1, "second_number": number_2, "operator": operator_1}

    do_calculations(user_input)


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
    elif user_input.get("operator").__eq__("x") or user_input.get("operator").__eq__("X") or user_input.get("operator").__eq__("*"):
        clear_screen()
        print("\n\n", INDENT, number_1, user_input.get("operator"), number_2, "=", number_1 * number_2)
    elif user_input.get("operator").__eq__("/") or user_input.get("operator").__eq__("÷"):
        clear_screen()
        print("\n\n", INDENT, number_1, user_input.get("operator"), number_2, "=", number_1 / number_2)
    else:
        print("\n\n", INDENT, "ERROR: Unknown operation selected.")
        quit_calculator()

    more_calculations()


def more_calculations():
    """Prompt the user to choose between additional calculations & quitting the program."""
    more_calc_input = "invalid"
    while more_calc_input != "y" and more_calc_input != "n":
        print("\n\n", INDENT, "Would you like to run additional calculations?")
        more_calc_input = input( INDENT + "  Please enter 'y' to perform more calculations, or 'n' to quit the program: ")
        try:
            more_calc_input = more_calc_input.lower()
        except:
            pass
            # TODO: Better error handling
    if more_calc_input == "y":
        clear_screen()
        request_input()
    elif more_calc_input == "n":
        quit_calculator()


def clear_screen():
    """Clears the screen, regardless of the OS."""
    os.system("cls" if os.name == "nt" else "clear")


def quit_calculator():
    """Bring the program to an end."""
    print("\n")
    input(INDENT + "  Press Enter to close...")
    sys.exit()


# run program

if __name__ == '__main__':
    greet_user()
    request_input()
