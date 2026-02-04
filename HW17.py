#Name: Coach Mack
#Class: 6th Hour
#Assignment: HW17
import random


#1. Create a def function that plays a single round of rock, paper, scissors where the user inputs
#1 for rock, 2 for paper, or 3 for scissors and compares it to a random number generated to serve
#as the "opponent's hand".
def rps():
    user_hand = int(input("Press 1 for Rock, 2 for Paper, 3 for Scissors"))
    oppo_hand = random.randint(1,3)
    '''
    if user_hand == 1 and oppo_hand == 2:
        print("Opponent Picked Paper! You Lose!")
    elif user_hand == 1 and oppo_hand == 3:
        print("Opponent Picked Scissors! You Win!")
    elif user_hand == 2 and oppo_hand == 1:
        print("Opponent Picked Rock! You Win!")
    elif user_hand == 2 and oppo_hand == 3:
        print("Opponent Picked Scissors! You Lose!")
    elif user_hand == 3 and oppo_hand == 1:
        print("Opponent Picked Rock! You Lose!")
    elif user_hand == 3 and oppo_hand == 2:
        print("Opponent Picked Paper! You Win!")
    else:
        print("You both picked the same thing! Tie!")
    '''

    if user_hand == oppo_hand:
        print("You both picked the same thing! Tie!")
    elif user_hand == 1 and oppo_hand == 3:
        print("Opponent Picked Scissors! You Win!")
    elif user_hand == 2 and oppo_hand == 1:
        print("Opponent Picked Rock! You Win!")
    elif user_hand == 3 and oppo_hand == 2:
        print("Opponent Picked Paper! You Win!")
    else:
        print("You lose!")
    repeat_game()

#2. Create a def function that prompts the user to input if they want to play another round, and
#repeats the RPS def function if they do or exits the code if they don't.

def repeat_game():
    user_repeat = input("Do you want to play again? Y/N").lower()

    if user_repeat == "y":
        rps()
    elif user_repeat == "n":
        print("Thanks for playing!")
    else:
        print("Invalid input. Please try again.")
        repeat_game()

rps()