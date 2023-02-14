# =====================================================================
# Day 4 Challange: Randomization
# =====================================================================
# [Task]:
# Create a rock, paper and scissor game

# =====================================================================
# Imports
# =====================================================================
import random
from typing import List

def get_designs()->List[str]:
    '''defines rock,paper and scissor game designs as strings

    :return: List containing game designs, which need to be in correct order
    :rtype: List[str]
    '''

    rock = '''
            _______
        ---'   ____)
             (_____)
             (_____)
             (____)
        ---.__(___)
        '''

    paper = '''
            _______
        ---'   ____)____
                  ______)
                 _______)
                _______)
        ---.__________)
        '''

    scissors = '''
            _______
        ---'   ____)____
                  ______)
              __________)
                (____)
        ---.__(___)
        '''
    return [rock,paper,scissors]

# =====================================================================
# Main
# =====================================================================

# [Solution]:
def main()->None:

    # get designs
    designs = get_designs()

    # define user choice
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

    # define computer choice
    computer_choice = random.randint(0,2)

    # get the result
    if user_choice >= 3 or user_choice < 0:
        print("You typed an invalid number, you lose!")

    else:
        print("User:")
        print(designs[user_choice])
        print("Computer")
        print(designs[computer_choice])

        if user_choice == 0 and computer_choice == 2:
            print("You win!")
        elif computer_choice == 0 and user_choice == 2:
            print("You lose")
        elif computer_choice > user_choice:
            print("You lose")
        elif user_choice > computer_choice:
            print("You win!")
        elif computer_choice == user_choice:
            print("It's a draw")

    return



if __name__ == '__main__':
    main()
