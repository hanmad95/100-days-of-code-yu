# =====================================================================
# Day 7 Challange:
# =====================================================================
# [Task]:
#

import random
from layout import layout

# =====================================================================
# Main
# =====================================================================


def main() -> None:

    # =================================================================
    # Init layout
    stages, logo = layout()
    win = False
    print(logo)

    # =================================================================
    # Create a random word from list of words
    word_list = ["baboon", "elephant", "beekeeper"]
    random_word = random.sample(word_list, 1)[0]

    # init progress bar based on random word
    progress = ["_" for k in range(len(random_word))]

    # =================================================================
    # until stages are left
    while stages:

        # ask for letter
        guess_letter = str(input("Guess a letter: "))
        guess_state = False

        # see if there is a match
        for num, ele in enumerate(random_word):
            if ele == guess_letter:
                progress[num] = guess_letter
                guess_state = True

        # when match -> print progress
        if guess_state:
            print("".join(progress))
        else:  # -> remove stage from list and print it
            print(stages.pop())

        # case no "_" is left -> win
        if "_" not in progress:
            print("Congratulatoins you won!")
            win = True
            break

    # otherwise lost
    if not win:
        print("You lost ... ")
        print(f"Word would have been {random_word}")

    return


if __name__ == "__main__":
    main()
