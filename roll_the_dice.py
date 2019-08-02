'''This program will allow the user to play a game of dice. The die is a normal, 6-sided die. The user should be prompted to start the roll.
	The user can continue to roll as long as they'd like by entering 'yes', 'y', 'no', or 'n'. Yes or 'y' should continue the game while "no"
	or 'n' will end the game.'''

import random

dice=[1,2,3,4,5,6]

user_continue = input("Would you like to roll the dice?")


if user_continue == "yes":
	print(random.choice(dice))
else:
	print("Thanks for playing!")

	