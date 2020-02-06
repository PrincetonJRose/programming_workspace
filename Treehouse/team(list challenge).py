# Practicing list functions

import sys
import math
import random
import string

# TODO Create an empty list to maintain the player names
roster = []

# TODO Ask the user if they'd like to add players to the list.
# If the user answers "Yes", let them type in a name and add it to the list.
# If the user answers "No", print out the team 'roster'
while True:
    ask = input("\nWould you like to add a player to the team's roster?\n(Y=Yes  N=No): ")        
    if ask.lower() == 'yes' or ask.lower() == 'y':
        name = input("What is the player's name? ")
        if not name.isalpha() or len(name) <= 1:
            print("Please enter a name.")
            continue
        else:
            roster.append(name)
            continue
    elif ask.lower() == 'no' or ask.lower() == 'n':
        print("\nThe current roster is:\n{}".format(roster))
        break
    else:
        print("Please enter the correct response.")
        continue


# TODO print the number of players on the team
print("\nThere are currently {} players on the team.".format(len(roster)))

# TODO Print the player number and the player name
# The player number should start at the number one
for x in range(len(roster)):
    print("Player #{}: {}".format(x + 1, roster[x]))

# TODO Select a goalkeeper from the above roster
while True:
    try:
        goalie = int(input("\nChoose the number for the player who\nis going to be the goal keeper:  "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    if goalie < 1 or goalie > len(roster):
        print("Please choose a team member on the roster to be the goal keeper.")
        for x in range(len(roster)):
            print("Player #{}: {}".format(x + 1, roster[x]))
        continue
    else:
        goalie -= 1
        break

# TODO Print the goal keeper's name
# Remember that lists use a zero based index
print("Great! The goal keeper is {}!".format(roster[goalie]))
