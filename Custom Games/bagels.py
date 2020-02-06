import random
import sys
import os

MAX_GUESSES = 10
NUM_LENGTH = 3

def clear_screen():
    # clears the screen
    os.system("cls" if os.name == "nt" else "clear")

def get_number():
    secret_number = []
    while len(secret_number) != NUM_LENGTH:
        num = random.randint(0,9)
        if num in secret_number:
            continue
        else:
            secret_number.append(num)
    return secret_number

def player_won(guesses):
    print("\nNice job!!! You guess the number correctly in only {} tries!\nGive yourself a pat on the back!!!  ^_^".format(guesses))
    play_again()
    
def player_lose(secret_number):
    print("\nAww, you ran out of attempts and didn't manage to guess the number sequence.  =(\nThe number was {}. Better luck next time...".format(secret_number))
    
def play_again():
    while True:
        again = input("\nWould you like to play again? (Yes/No): ")
        again = again.lower()
        if again == 'yes' or again == 'y':
            main_game()
        elif again == 'no' or again == 'n' or again == 'exit' or again == 'q' or again == 'quit':
            sys.exit(1)
        else:
            continue

def main_game():
    secret_number = get_number()
    clear_screen()
    print("""Welcome to Bagel! The goal of the game it to guess the correct number sequence.\nI will give you clues to help you figure it out. Those clues are...\n""")
    print("Bagel  =  None of the numbers are in the sequence")
    print("Fermi  =  A number is a match and in the right place")
    print("Pico   =  A number is a match and not in the right place")
    print("\nThe number is {} digits long. You have {} tries to guess it. Good luck!!!  ^_^".format(NUM_LENGTH, MAX_GUESSES))
    guesses = 0
    while True:
        if guesses == MAX_GUESSES:
            player_lose(secret_number)
        while True:
            guess = input("\nWhat is your guess? (You have {} tries remaining): ".format(MAX_GUESSES - guesses))
            if not guess.isdigit():
                print("Please enter a number.")
                continue
            elif len(guess) != NUM_LENGTH:
                print("Please enter number that is {} digits long".format(NUM_LENGTH))
                continue
            else:
                break
        guesses += 1
        guess = list(guess)
        for x in range(len(guess)):
            guess[x] = int(guess[x])
        if guess == secret_number:
            player_won(guesses)
        clue = []
        for x in range(len(secret_number)):
            if guess[x] == secret_number[x]:
                clue.append("Fermi")
            elif guess[x] in secret_number:
                clue.append("Pico")
        if len(clue) == 0:
            clue.append("Bagel")
        clue.sort()
        print(' '.join(clue))

main_game()