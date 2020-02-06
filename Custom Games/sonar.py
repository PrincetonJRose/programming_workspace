import random
import math
import sys
import os

MAX_CHESTS = 3      # number of maximum chests that can spawn
MAX_SONAR = 20      # maximum amount of sonar beacons that the player starts with

def clear_screen():     # clears the screen
    os.system("cls" if os.name == "nt" else "clear")
    
def create_board():     # creates a new board made from ~ and ` symbols that is 15x60 spaces
    new_board = []
    for row in range(15):
        new_board.append([])
        for column in range(60):
            if random.randint(0,1) == 0:
                new_board[row].append('~')
            else:
                new_board[row].append('`')
    return new_board

def place_chests():     # creates the chest coordinates
    new_chests = []
    for number in range(MAX_CHESTS):
        new_chests.append([random.randint(0,14), random.randint(0,59)])
    return new_chests                          

def draw_map(board, chests, sonars_placed):     # draws the board when called
    coord1 = []     # creating variables to help tidy up the display of sonar locations at the side of the board
    coord2 = []
    coord3 = []
    coord4 = []
    num = 0
    # makes it a little neater to display all the locations a player has done next to the board once it's more than 5
    for sonars in sonars_placed:
        if num < 5:
            coord1.append(sonars[::-1])
        if num > 4 and num < 10:
            coord2.append(sonars[::-1])
        if num > 9 and num < 15:
            coord3.append(sonars[::-1])
        if num > 14:
            coord4.append(sonars[::-1])
        num += 1
    print("\n    This is what the map looks like so far...\n")     # time to draw the entire board
    num_line = ''
    for x in range(1,6):
        num_line += ' ' * 9 + str(x)
    print("     " + num_line)
    print("     " + '0123456789' * 6)
    print("     " + '-' * 60)
    for row in range(15):
        if row == 3:
            print("   | " + ''.join(board[row]) + " | " + str(row) + "   Chests remaining = {} / {}".format(len(chests), MAX_CHESTS))
            continue
        if row == 6:
            print("   | " + ''.join(board[row]) + " | " + str(row) + "   Sonar beacons    = {} / {}".format(MAX_SONAR - len(sonars_placed), MAX_SONAR))
            continue
        if row == 9:
            print("   | " + ''.join(board[row]) + " | " + str(row) + "   Sonar locations  = {}".format(coord1))
            continue
        if row == 10 and len(coord2) > 0:
            print("   | " + ''.join(board[row]) + " | " + str(row) + "                     {}".format(coord2))
            continue
        if row == 11 and len(coord3) > 0:
            print("   | " + ''.join(board[row]) + " | " + str(row) + "                     {}".format(coord3))
            continue
        if row == 12 and len(coord4) > 0:
            print("   | " + ''.join(board[row]) + " | " + str(row) + "                     {}".format(coord4))
            continue
        print("   | " + ''.join(board[row]) + " | " + str(row))
    print("     " + "-" * 60)

def update_board(board, sonars_placed, chests):    # function to update the board with sonar placement locations
    # time to find the closest chest to each of the sonars that are on the board and mark the sonar locations
    for sweep in sonars_placed:
        chests_pinged = []
        for ping in chests:
            distance = round(math.sqrt((ping[0] - sweep[0])**2 + (ping[1] - sweep[1])**2))
            if distance < 10:
                chests_pinged.append(distance)
        if len(chests_pinged) == 0:
            board[sweep[0]][sweep[1]] = 'X'
        else:
            board[sweep[0]][sweep[1]] = str(min(chests_pinged))

def player_lose(chests):    # message for when the player loses  =(
    clear_screen()
    if len(chests) == MAX_CHESTS:
        print("\nAww, you didn't find any treasure out there on the sea.\nYou crew sails sadly back to port empty handed.\nMaybe you'll have better luck next time...  =(")
    else:
        print("\nDrats! You didn't manage to find all the treasure this time.\nAt least you have something to show for all your time and effort.\nYou head back to resupply and try again another day...")
    play_again()
    
def player_win():   # message for when the player wins!  ^_^
    clear_screen()
    print("\nNicely done! You and your crew celebrate as they head back with a cargo hold full \nof wonderful treasure! Good job out there captain!!!  ^_^")
    play_again()
    
def play_again():   # ask the player if they would like to play the game again
    clear_screen()
    again = input("\nWould you like to play again? (Yes/Quit):  ").lower()
    if again == 'y' or again == 'yes':
        main_game()
    else:
        sys.exit()
        
def instructions():
    clear_screen()
    print('''\nInstructions:
    
    You are the captain of the USS Leeman, a deep sea treasure-hunting ship. Your current mission
    is to use sonar beacons to find sunken treasure chests at the bottom of the ocean. But you
    only have low-budget sonar that can only tell you the distance a treasure chest is from it,
    but not which direction it is in.
    
    Enter the coordinates to drop a sonar beacon. The ocean map will be marked with how far away
    the nearest chest is, or an X if it is beyond the range of the sonar beacon. For example, the
    C marks are where the chests are. The sonar beacon shows a 3 because closest chest is 3 spaces
    away.
    
             012345678901234567890123456789
           0 ``~~~```````~~~```~``~~`~~``~`
           1 ~`~~~~``~``~~``````````~```~~`
           2 `~`C``3`~~~~C~```~~~~```~`~`~~
           3 ```````~~~~~``~~~``~`~~~~`~~`~
           4 ~`~~~~~~``~~C~```~`````~~```~`
        
        (In the real game, the chests are not visible.)
    
    Press enter to continue...''')
    input()
    print('''    When you drop a sonar device on a chest directly you retrieve it. The other sonar devices
    will update to now show how far away the next closest chest is to them. The chest on the far left
    is to far out of range and therefore shows and X.
    
             012345678901234567890123456789
           0 ``~~~```````~~~```~``~~`~~``~`
           1 ~`~~~~``~``~~``````````~```~~`
           2 `~`X``7`~~~~C~```~~~~```~`~`~~
           3 ```````~~~~~``~~~``~`~~~~`~~`~
           4 ~`~~~~~~``~~C~```~`````~~```~`
           
    Treasure chests don't move. The sonar beacons have a max range of a 9 unit radius. Try to collect
    all of the treasure chests before you run out of sonar beacons! Good luck out there captain!!! ^_^
    
    Press enter to continue...''')
    input()

def main_game():    # the main game starts here
    clear_screen()
    print("Welcome to S O N A R !")
    learn = input("Would you like to view the instructions? (Yes/No/Quit):  ").lower()  # ask the player if they would like to view the instructions
    if learn == 'yes' or learn == 'y':      # show instructions if the player says yes
        instructions()
    elif learn == 'quit' or learn == 'q':   # exit the program
        sys.exit()
    board = create_board()  # create the main games variables now
    chests = place_chests()
    sonars_placed = []
    while True:     # main game loop
        clear_screen()
        draw_map(board, chests, sonars_placed)  # draw the board
        while True:
            drop_sonar = input("\n    At what coordinates would you like to drop a sonar beacon?  X = (0-59)  &  Y = (0-14):  ").lower()   # ask for the player's coordinates
            if drop_sonar == "quit" or drop_sonar == 'q' or drop_sonar == 'exit' or drop_sonar == 'e' :
                sys.exit()
            if ', ' in drop_sonar:   # split the string into 2 parts for an x & y coordinate
                drop_sonar = drop_sonar.split(', ')
            elif ',' in drop_sonar:
                drop_sonar = drop_sonar.split(',')
            else:
                drop_sonar = drop_sonar.split()
            if len(drop_sonar) != 2:    # ensure that there are 2 values for coordinates before continuing
                print("    Please enter a valid set of two coordinates.")
                continue
            if drop_sonar[0].isdigit() and drop_sonar[1].isdigit(): # make sure that the input is numbers and if they are turn them into integers
                drop_sonar = drop_sonar[::-1]
                drop_sonar[0] = int(drop_sonar[0])
                drop_sonar[1] = int(drop_sonar[1])
            else:
                print("    Please enter numbers for coordinates.")
                continue
            if drop_sonar[1] > 59 or drop_sonar[1] < 0 or drop_sonar[0] > 14 or drop_sonar[0] < 0:  # check to see if the location is a valid placement on the board
                print("    Please enter a valid set of numbers between 0-59 & 0-14.")
                continue
            if drop_sonar in sonars_placed:     # check to see if they have already placed a sonar in the same spot
                print("    You've already placed a beacon there.")
                continue
            elif drop_sonar in chests:
                chests.remove(drop_sonar)
                sonars_placed.append(drop_sonar)
                if len(chests) == 0 and len(sonars_placed) <= 20:   # check to see if the player won
                    input("\n    Good job, you found the last chest!  ^_^\n(Press enter to continue...)\n")
                    player_win()
                input("\n    Good job, you've found a chest! Only {} more to go!  ^_^\n(Press enter to continue...)\n".format(len(chests)))
                break
            else:
                sonars_placed.append(drop_sonar)
                break
        update_board(board, sonars_placed, chests) # check to see if the player found any chests in range
        if len(sonars_placed) >= MAX_SONAR and len(chests) > 0:     # check to see if the player lost
            player_lose(chests)
    
main_game()