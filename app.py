# write code for the description below
# let the player input rock, paper or scissors by entering 1, 2 or 3
# let the computer randomly choose rock, paper or scissors
# compare the player's choice and the computer's choice
# print out the result
# let the player play again
# let the player stop playing if he/she wants to stop
# print out the total number of wins and loses when the player stops playing
# print out the final result of the game

import random
from enum import Enum

# Define un enum simple
class Option(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


def main():
    playerPoints = 0
    computerPoints = 0

    while True:
        # Generate a random number (1, 2 o 3)
        computer = random.randint(1, 3)
        
        # get input from player that needs to handle invalid input like char or string
        try:
            player = int(input("Enter 1 for rock, 2 for paper, 3 for scissors: "))
        except ValueError:
            print("Invalid input!")
            continue

        # print out the player and computer selections
        print('player:', Option(player).name, 'vs', 'computer:', Option(computer).name)
        # check winner
        if player == 1:
            #switch for computer
            if computer == 1:
                print("Tie! Score is now: " + str(playerPoints) + " to " + str(computerPoints))
            elif computer == 2:
                computerPoints += 1
                print("You lose! Score is now: " + str(playerPoints) + " to " + str(computerPoints))
            elif computer == 3:
                playerPoints += 1
                print("You win! Score is now: " + str(playerPoints) + " to " + str(computerPoints))
        elif player == 2:
            if computer == 1:
                playerPoints += 1
                print("You win! Score is now: " + str(playerPoints) + " to " + str(computerPoints))
            elif computer == 2:
                print("Tie! Score is now: " + str(playerPoints) + " to " + str(computerPoints))
            elif computer == 3:
                computerPoints += 1
                print("You lose! Score is now: " + str(playerPoints) + " to " + str(computerPoints))
        elif player == 3:
            if computer == 1:
                computerPoints += 1
                print("You lose! Score is now: " + str(playerPoints) + " to " + str(computerPoints))
            elif computer == 2:                
                playerPoints += 1
                print("You win! Score is now: " + str(playerPoints) + " to " + str(computerPoints))
            elif computer == 3:
                print("Tie! Score is now: " + str(playerPoints) + " to " + str(computerPoints))
        else:
            print("Invalid input!")
        
        # ask if player wants to play again
        playAgain = input("Do you want to play again? (y/n): ")
        if playAgain == "y":
            continue
        elif playAgain == "n":
            print("Final score is: " + str(playerPoints) + " to " + str(computerPoints))
            break
        else:
            print("Invalid input!")
            break
        

main()