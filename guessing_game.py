"""
Project 1 - Number Guessing Game
--------------------------------

For this first project you can use Workspaces. 

NOTE: If you prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random
from statistics import median 
from statistics import mode

def start_game():

# 1. Display an intro/welcome message to the player.
  print("Welcome to the great guessing game! I am excited for you to take a swing at your guessing skills")
  print()
# 2. Store a random number as the answer/solution.
solution = random.randint(1, 100)

"""3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
"""

guess = []
response = ""
while response != solution:
  response = input("Please choose a number between 1 and 100? ")
  guess.append(int(response))
  if int(response) > solution:
      print("It's lower")
  elif int(response) < solution:
      print("It's higher")
  else:
      print("You got the correct answer")
      print(f"It took you {len(guess)} tries")
"""
4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
"""

# 5. Save their attempt number to a list.

# 6. At the end of the game, show the player, 1) their number of attempts, 2) the mean, median, and mode of the saved attempts list.

guess.sort()
print(guess)
mean = round(sum(guess)/len(guess))
median = round(median(guess))
mode = mode(guess)
print("Overall Statistics")
print(mean)
print(median)
print(mode)
# 7. Ask the player if they want to play again.
restart = input("Would you like to play again? (Yes/No) ")
if restart.lower() == "yes":
    start_game()
else:
    print("GAME OVER")
    print()



# Kick off the program by calling the start_game function.
start_game()