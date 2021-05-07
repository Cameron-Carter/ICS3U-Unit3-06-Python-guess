#!/usr/bin/env python3

# Created by: Cameron Carter
# Created on May 2021
# This program lets the user guess a number from 1-10

import random
import string


def main():
    # This function lets the user guess a number from 1-10

    # Input
    guess_as_string = str(input("Guess an integer from 1-10: "))
    random_number = random.randint(1, 10)

    # Process and Output
    try:
        guess_as_number = int(guess_as_string)
        if guess_as_number == random_number:
            print("\nCorrect! The number was {}.".format(random_number))
        else:
            print("\nIncorrect! The number was {}.".format(random_number))
    except Exception:
        print("\n{} is not an integer!".format(guess_as_string))
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
