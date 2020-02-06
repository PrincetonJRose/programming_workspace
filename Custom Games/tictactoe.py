import random
import os
import sys

def clear_screen():
    # clears the screen
    os.system("cls" if os.name == "nt" else "clear")
    
def show_board(game_board):
    # function that draws the board
    spaces = 0
    print()
    for board in range(len(game_board)):
        display = ''
        spaces += 1
        if spaces == 5:
            spaces = 0
            display = '\n'
        print(game_board[board], end = display)

def game_start():
    # function that creates the variables and the board to start the game
    clear_screen()
    game_board = [' ','|',' ','|',' ',
                  '-','+','-','+','-',
                  ' ','|',' ','|',' ',
                  '-','+','-','+','-',
                  ' ','|',' ','|',' ',
                  ]
    computer = ''
    player = ''
    print("\nWelcome to Tic-Tac-Toe!")
    while True:
        player = input("Do you want to be X or O? ")
        player = player.upper()
        if player == 'X' or player == 'O':
            break
    if player == 'X':
        computer = 'O'
    else:
        computer = 'X'
    turn = random.randint(0,1)
    if turn == 0:
        turn = 'Computer'
    else:
        turn = 'Player'
    main_game(game_board, player, computer,turn)
    
def player_turn(game_board, player):
    clear_screen()
    # this is the player's turn to move
    print("It's currently your turn!\nHere is where you can move:")
    move_check = game_board.copy()
    number = 0
    for moves in range(len(move_check)):
        if move_check[moves] == ' ':
            number += 1
            move_check[moves] = number
    show_board(move_check)
    # give the player a choice of numbers on the board to choose from, filling in empty spaces with the numbers for visual reference
    while True:
        move_here = input("\nWhere would you like to move?\n(Enter the number of the space): ")
        if not move_here.isdigit():
            print("Please enter a number.")
            continue
        move_here = int(move_here)
        if move_here > number or move_here < 1:
            print("Please enter a valid placement.")
            continue
        else: 
            for moves in range(len(move_check)):
                if move_check[moves] == move_here:
                    game_board[moves] = player
                    break
            break
    # quick check to see if that last move won the game before letting the computer move
    if check_winner(game_board, player):
        player_win(game_board)
    return game_board

def computer_turn(game_board, computer, player):
    # small AI for the computer to try and find the best move
    move_check = game_board.copy()
    
    # check to see if the next move the computer can make can win and do that if possible
    for x in range(len(move_check)):
        move_check1 = game_board.copy()
        if move_check[x] == ' ':
            move_check1[x] = computer
            if check_winner(move_check1, computer):
                game_board[x] = computer
                return game_board
    
    # check to see if player's next move can win and block it
    for x in range(len(move_check)):
        move_check1 = game_board.copy()
        if move_check[x] == ' ':
            move_check1[x] = player
            if check_winner(move_check1, player):
                game_board[x] = computer
                return game_board
    
    # check corners and take one if they are free
    corners = [0,4,20,24]
    corners_open = []
    if move_check[0] == ' ' or move_check[4] == ' ' or move_check[20] == ' ' or move_check[24] == ' ':
        for moves in range(len(corners)):
            if move_check[corners[moves]] == ' ':
                corners_open.append(corners[moves])
        move = random.choice(corners_open)
        game_board[move] = computer
        return game_board

    # take center if it's free
    if move_check[12] == ' ':
        game_board[12] = computer
        return game_board
    
    # take one of the sides if none of the other spaces are available
    sides = [2,10,14,22]
    sides_open = []
    if move_check[2] == ' ' or move_check[10] == ' ' or move_check[14] == ' ' or move_check[22] == ' ':
        for moves in range(len(sides)):
            if move_check[sides[moves]] == ' ':
                sides_open.append(sides[moves])
        move = random.choice(sides_open)
        game_board[move] = computer
        return game_board

def check_winner(b, l):
    #Check if the player or computer wins
    return ((b[0] == l and b[2] == l and b[4] == l) or (b[10] == l and b[12] == l and b[14] == l) or (b[20] == l and b[22] == l and b[24] ==l) or (b[0] == l and b[10] == l and b[20] == l) or (b[2] == l and b[12] == l and b[22] ==l) or (b[4] == l and b[14] == l and b[24] == l) or (b[0] ==l and b[12] == l and b[24] == l) or (b[4] == l and b[12] == l and b[20] == l))

def player_win(board):
    # let the player know they won
    clear_screen()
    show_board(board)
    print("\nTic Tac Toe, three in a row! Yay!")
    print("Congratulations! You won! Good job!!!  ^_^")
    play_again()
    
def player_lose(board):
    # let the player know they lost
    clear_screen()
    show_board(board)
    print("\nAww, the computer beat you. Maybe next time...  ^_^")
    play_again()

def game_tie(board):
    # let the player know that the game was a tie due to no more spaces left on the board
    clear_screen()
    show_board(board)
    print("\nOops, looks like nobody was able to win\nand the match ends in a draw...  O_O")
    play_again()
    
def play_again():
    # ask the player if they want to play again
    while True:
        again = input("\nWould you like to play again (Y/N)? ")
        if not again.isalpha():
            continue
        else:
            again = again.lower()
        if again == 'y' or again == 'yes':
            game_start()
        elif again == 'n' or again == 'no' or again == 'quit' or again == 'exit' or again == 'q':
            clear_screen()
            sys.exit(1)
        else:
            continue

def main_game(game_board, player, computer,turn):
    # the main loop for the game
    while True:
        filled = 0
        for full in game_board:
            if full == ' ':
                filled += 1
        if filled == 0:
            game_tie(game_board)
        clear_screen()
        print("\nPlayer   = " + player + "\nComputer = " + computer)
        print("This is what the board looks like so far:")
        show_board(game_board)
        print()
        if turn == 'Player':
            game_board = player_turn(game_board, player)
            turn = 'Computer'
            continue
        else:
            input("It's the computers turn. (Press enter to continue)")
            game_board = computer_turn(game_board, computer, player)
            if check_winner(game_board, computer):
                player_lose(game_board)
            turn = 'Player'
            continue

game_start()