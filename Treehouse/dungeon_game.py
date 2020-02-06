import sys
import math
import random
import string
import time
import csv
import os

CELLS = [(0,0),(1,0),(2,0),(3,0),(4,0),
         (0,1),(1,1),(2,1),(3,1),(4,1),
         (0,2),(1,2),(2,2),(3,2),(4,2),
         (0,3),(1,3),(2,3),(3,3),(4,3),
         (0,4),(1,4),(2,4),(3,4),(4,4)]

# pick random location for player, monster, and door
def get_locations():
    return random.sample(CELLS, 3)

# draw player in the grid
def draw_map(player):
    print()
    print(" _"*5)
    tile = "|{}"
    
    for cell in CELLS:
        x, y = cell
        if x < 4:
            line_end = ""
            if cell == player:
                output = tile.format("X")
            else:
                output = tile.format("_")
        else:
            line_end = "\n"
            if cell == player:
                output = tile.format("X|")
            else:
                output = tile.format("_|")
        print(output, end=line_end)
    print()

# take input for movement
def get_moves(player):
    moves = ["Left", "Right", "Up", "Down"]
    x, y = player
    # if player y == 0, can't move up
    if y == 0:
        moves.remove("Up")
    # if player y == 4, can't move down
    if y == 4:
        moves.remove("Down")
    # if player x == 0, can't move left
    if x == 0:
        moves.remove("Left")
    # if player x == 4, can't move right
    if x == 4:
        moves.remove("Right")
    return moves

# move player, unless invalid move (past edges of grid)
def move_player(player, move):
    # get player's location
    x, y = player
    # if move up, y-1
    if move == "Up" or move == 'U':
        y -= 1
    # if move down, y+1
    if move == "Down" or move == 'D':
        y += 1
    # if move left, x-1
    if move == "Left" or move == 'L':
        x -= 1
    # if move right, x+1
    if move == "Right" or move == 'R':
        x += 1
    return x, y

# make a function for looping the game
def game_loop():
    monster, door, player = get_locations()
    while True:
        clear_screen()
        draw_map(player)
        moves = ["Left", "Right", "Up", "Down"]
        valid_moves = get_moves(player)
        
        print("You're currently in room {}.".format(player)) # fill in player position
        print("You can move {}".format(", ".join(valid_moves))) # fill in available move options
        print("(Enter 'Q' to Quit)")
        move = input("> ")
        
        if move.isalpha():
            move = move.capitalize()
        else:
            continue
        if move == 'Q' or move == 'Quit':
            clear_screen()
            sys.exit(1)
        if move in valid_moves:
        # good move? change the player position
            player = move_player(player, move)

            # check for win (find door) or loss (find monster)
            # on the door? they win!
            if player == door:
                input("Omg you found the door that leads out!\n"
                      "You escape this horrid place and the\n"
                      "monster that resided within.")
                while True:
                    clear_screen()
                    play_again = input("Would you like to try again?\n(Y for yes or N for no): ").lower()
                    if not play_again.isalpha():
                        continue
                    if play_again == 'y' or play_again == 'yes':
                        monster, door, player = get_locations()
                        break
                    elif play_again == 'n' or play_again == 'no':
                        clear_screen()
                        sys.exit(1)
            
            # on the monster? they lose!
            if player == monster:
                input("Oh no... you ran into the monster. It wasted\n"
                      "no time in gulping you down. Maybe in your\n"
                      "next life you'll do better.")
                while True:
                    clear_screen()
                    play_again = input("Would you like to try again?\n(Y for yes or N for no): ").lower()
                    if not play_again.isalpha():
                        continue
                    if play_again == 'y' or play_again == 'yes':
                        monster, door, player = get_locations()
                        break
                    elif play_again == 'n' or play_again == 'no':
                        clear_screen()
                        sys.exit(1)
            
        elif move not in moves:
            continue
        else:
        # bad move? don't change anything
            input("You ran into a wall! Ouch!")
            continue
        # otherwise, continue the loop

# clear screen
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

clear_screen()
print("Welcome to the dungeon!")
input("Press Enter to start!")
clear_screen()
game_loop()
