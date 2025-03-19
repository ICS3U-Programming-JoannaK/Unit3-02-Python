#!/usr/bin/env python3

# Created by: Joanna Keza
# Date: March 18, 2025
# This program asks the user to enter
# number between 0 and 0 and try to guess
# the correct number

import constants


def main():
    # get number from the user
    number_picked = int(input("Enter the number: "))

    # check if user guess is correct
    if number_picked == constants.NUMBER:
        print("Good job, that is right")

    # check if user guess is not correct
    if number_picked != constants.NUMBER:
        print("Not quite, try again")


if __name__ == "__main__":
    main()
