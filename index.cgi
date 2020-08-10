#!/Python26/python
import random
from random import seed
from random import choice



print("Welcome to rock paper scissors by Murphy Towne!")

bad = 0

def StartGame():
    user_attack = input("Pick rock,paper,or scissors:")


    choices = ["rock", "paper", "scissors"]
    for _ in choices:
        selection = choice(choices)
    if selection == "rock" and user_attack.lower() == "paper":
        print("Rock")
        print("You win!")
    elif selection == "rock" and user_attack.lower() == "scissors":
        print("Rock")
        print("I win!")
    elif selection == "rock" and user_attack.lower() == "rock":
        print("Rock")
        print("It's a tie!")
    elif selection == "paper" and user_attack.lower() == "rock":
        print("Paper")
        print("I win!")
    elif selection == "paper" and user_attack.lower() == "scissors":
        print("Paper")
        print("You win!")
    elif selection == "paper" and user_attack.lower() == "paper":
        print("Paper")
        print("It's a tie!")
    elif selection == "scissors" and user_attack.lower() == "scissors":
        print("Scissors")
        print("It's a tie!")
    elif selection == "scissors" and user_attack.lower() == "rock":
        print("Scissors")
        print("You win!")
    elif selection == "scissors" and user_attack.lower() == "paper":
        print("Scissors")
        print("I win!")
    else:
        print("Shut up loser and pick an actual fucking option!")
        StartGame()
    Play_Again = input("Would you like to play again?")
    if Play_Again.lower() == "yes":
        StartGame()
    else:
        exit()

StartGame()
