# =====================================================================
# Day 5 Challange:
# =====================================================================
# [Task]: Create a password generator
#

# =====================================================================
# Imports
# =====================================================================
import random
import string
from typing import List, Union


# =====================================================================
# Main
# =====================================================================

# [Solution]:
def main() -> Union[str, List[str]]:

    # define possible characters
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation

    print("Welcome to password generator!\n")
    num_letters = int(input("How many letters should your password have?"))
    num_numbers = int(input("How many numbers should your password have?"))
    num_symbols = int(input("How many symbols should your password have?"))

    # draw random numbers
    rand_symbols = random.choices(symbols, k=num_symbols)
    rand_numbers = random.choices(numbers, k=num_numbers)
    rand_letters = random.choices(letters,
                                  k=(num_letters-num_numbers-num_symbols))

    # combine
    digits = rand_symbols + rand_numbers + rand_letters
    password = random.sample(digits, len(digits))
    password = "".join(password)  # type: ignore

    return password


if __name__ == '__main__':
    password = main()
    print(password)
