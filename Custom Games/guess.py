# This is a number guessing game
import random
import sys
import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def game_over(answer):
    print("\nSorry, you didn't guess the number before running\nout of tries. The number was {}.\n".format(answer))
    try_again()

def try_again():
    clear_screen()
    while True:
        play_again = input("Would you like to play again (Y/N)? ")
        if play_again.lower() == 'n' or play_again.lower() == 'no':
            sys.exit(1)
        elif play_again.lower() == 'y' or play_again.lower() == 'yes':
            main_game()
            break
        else:
            continue

def game_win(guesses_made):
    print("\nCongratulations! You guessed the number\ncorrectly in only {} tries!".format(len(guesses_made)))
    print("Give yourself a pat on the back!  ^_^\n")
    try_again()
    
def main_game():
    clear_screen()
    tries_left = 5
    guesses_made = []
    print('Hello, welcome to my number guessing game!')
    name = input("Please enter your name: ")
    answer = random.randint(1,20)
    input("Okay {}, I am thinking of a number between 1 and 20.\nTry to guess it. Good luck! ^_^\nPress Enter when ready.".format(name))
    while True:
        if tries_left == 0:
            game_over(answer)
        print("\nYou have {} tries remaining.".format(tries_left))
        print("Numbers you've already guessed so far = {}".format(guesses_made))
        try:
            guess = int(input("Guess a number: "))
        except ValueError:
            print("Please enter a number.")
            continue
        if guess in guesses_made:
            print("You've already guessed that number.")
            continue
        elif guess > 20 or guess < 1:
            print("Please enter a number between 1 and 20.")
            continue
        elif guess < answer:
            print("\nToo low, guess higher...")
            tries_left -= 1
            guesses_made.append(guess)
            continue
        elif guess > answer:
            print("\nToo high, guess lower...")
            tries_left -= 1
            guesses_made.append(guess)
            continue
        elif guess == answer:
            tries_left -= 1
            guesses_made.append(guess)
            game_win(guesses_made)
            
main_game()
