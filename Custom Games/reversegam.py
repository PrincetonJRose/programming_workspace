import random
import sys
import os

def clear_screen():     # clears the screen
    os.system("cls" if os.name == "nt" else "clear")

def create_visual_board():
    # this first board is used to draw a much cooler looking visual for the player and has no effect on the game
    board = [['.','.','.','.','1','.','2','.','3','.','4','.','5','.','6','.','7','.','8','.','.'],
             ['.','.','.','+','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','+','.'],
             ['.','.','1','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|','1'],
             ['.','.','.','+','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','+','.'],
             ['.','.','2','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|','2'],
             ['.','.','.','+','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','+','.'],
             ['.','.','3','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|','3'],
             ['.','.','.','+','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','+','.'],
             ['.','.','4','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|','4'],
             ['.','.','.','+','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','+','.'],
             ['.','.','5','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|','5'],
             ['.','.','.','+','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','+','.'],
             ['.','.','6','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|','6'],
             ['.','.','.','+','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','+','.'],
             ['.','.','7','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|','7'],
             ['.','.','.','+','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','+','.'],
             ['.','.','8','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|',' ','|','8'],
             ['.','.','.','+','-','-','-','-','-','-','-','-','-','-','-','-','-','-','-','+','.'],
             ['.','.','.','.','1','.','2','.','3','.','4','.','5','.','6','.','7','.','8','.','.']]
    return board

def create_board():
    # create a much smaller and simpler board that will hold that actual game on it
    board = []
    for row in range(0,10):
        board.append([])
        for column in range(0,10):
            board[row].append(' ')
    board[5][4] = 'X'
    board[4][4] = 'O'
    board[5][5] = 'O'
    board[4][5] = 'X'
    return board

def draw_board(drawing_board, board, computer, computer_score, player, player_score, turn):  # function for drawing the board
    print("\nHere is what the board looks like so far...\n")
    rows = 1
    columns = 1
    drawing = []
    for row in range(len(drawing_board)):
        drawing.append(drawing_board[row])
    for row in range(len(drawing)):     # fill in the board for visual reference with the actual game board
        for column in range(len(drawing[row])):
            if drawing[row][column] == ' ':
                drawing[row][column] = board[rows][columns]
                columns += 1
        if columns >= 8:
            columns = 1
            rows += 1
    for row in range(len(drawing)):     # tidy up the visual board a bit
        for column in range(len(drawing[row])):
            if drawing[row][column] == '.':
                drawing[row][column] = ' '
    for row in range(len(drawing)):     # time to actually draw the board along with the game info
        if row == 5:
            print(''.join(drawing[row]) + "\t   Computer's symbol =  {}".format(computer))
            continue
        if row == 7:
            print(''.join(drawing[row]) + "\t   Computer's score  =  {}".format(computer_score))
            continue
        if row == 11:
            print(''.join(drawing[row]) + "\t   Player's symbol   =  {}".format(player))
            continue
        if row == 13:
            print(''.join(drawing[row]) + "\t   Player's score    =  {}".format(player_score))
            continue
        if row == 17:
            print(''.join(drawing[row]) + "\t   Current turn      => {}".format(turn))
            continue
        print(''.join(drawing[row]))

def check_move(turn, board, player, computer, location):   # function to check and see if the move is a valid spot
    if turn == 'Player':
        symbol = player
        other_symbol = computer
    else:
        symbol = computer
        other_symbol = player
    

def update_board(board, player, computer, location):
    flip = []
    check = []
    

def main_game():    # main game function
    clear_screen()
    print("""
Welcome to Reversegam!!!

The object of the game is to have more tiles on the board than the computer.
Good luck!!!  ^_^""")
    while True:     # ask the player which symbol they want to be and make the computer the opposite
        pick = input("\nWhat symbol would you like to be? \n(X or O): ").upper()
        if pick == 'Q' or pick == 'QUIT' or pick == 'E' or pick == 'EXIT':
            sys.exit()
        if pick == 'X':
            player = 'X'
            computer = 'O'
            break
        elif pick == 'O':
            player = 'O'
            computer = 'X'
            break
        else:
            print("Please pick either X or O.")
            continue
            
    player_score = 0    # create all the variables to play the game and decide who goes first. then display the board
    computer_score = 0
    drawing_board = create_visual_board()
    board = create_board()
    turn = random.randint(0,1)
    if turn == 0:
        turn = 'Computer'
    else:
        turn = 'Player'
    draw_board(drawing_board, board, computer, computer_score, player, player_score, turn)
    
    while True:
        if turn == 'Player':
            location = input("It's your turn, where would you like to move? \n(Enter the numbers for a space on the board or type \"hint\" to see where you can move.):  ").lower()
            if location == "quit" or location == 'q' or location == 'exit' or location == 'e' :
                sys.exit()
            if location == 'hint' or location == 'hints':     # show where the player can move
                show_hints(board, player, computer)
                continue
            if ', ' in location:    # split the string into 2 parts for an x & y coordinate
                location = location.split(', ')
            elif ',' in location:
                location = location.split(',')
            else:
                location = location.split()
            if len(location) != 2:    # ensure that there are 2 values for coordinates before continuing
                print("Please enter a set of two numbers.")
                continue
            if location[0].isdigit() and location[1].isdigit(): # make sure that the input is numbers and if they are turn them into integers
                location[0] = int(location[0])
                location[1] = int(location[1])
            else:
                print("Please enter numbers for coordinates.")
                continue
            if location[0] >= 1 and location[0] <= 8 and location[1] >= 1 and location[1] <= 8:  # check to see if the location is a valid placement on the board
                print("Please enter a valid set of numbers between 1-8 & 1-8.")
                continue
            if board[location[0]][location[1]] != ' ':  # make sure the space they are trying to move to is empty
                print("That space is already occupied. Please choose an empty space.")
                continue
            if check_move(turn, board, player, computer, location):
                update_board(board, player, computer, location)
            else:
                print("That's not a valid move. Try again.")
                continue
        
        if turn == 'Computer':
            input("\nIt's the computer's turn. Press enter to continue...")
            board_copy = []
            for row in range(len(board)):
                board_copy.append(board[row])
            for row in range(len(board_copy)):
                for column in range(len(board_copy[row])):
                    if board_copy[row][column] == '!':
                        board_copy[row][column] = ' '
            
        
main_game()