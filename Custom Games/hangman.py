import random
import os
import sys

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def start_game():
    clear_screen()
    print("\nWelcome to HANGMAN! Try to guess the word\nbefore this poor man hangs. His life is in\nyour hands! No pressure. Good luck!  ^_^")
    HANGMAN_PICS = ['''
  +---+
  |   |
      |
      |
      |
      |
    =====''','''
  +---+
  |   |
  O   |
      |
      |
      |
    =====''','''
  +---+
  |   |
  O   |
  |   |
      |
      |
    =====''','''
  +---+
  |   |
  O   |
 /|   |
      |
      |
    =====''','''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
    =====''','''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
      |
    =====''','''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
    =====''','''
  +---+
  |   |
 [O   |
 /|\  |
 / \  |
      |
    =====''','''
  +---+
  |   |
 [O]  |
 /|\  |
 / \  |
      |
    =====''']

    while True:
        difficulty = input("\nSelect your difficulty level:\nEasy   - 8 attempts\nNormal - 6 attempts\nHard   - 4 attempts and topic not shown\n(E/N/H)? ")
        if not difficulty.isalpha() or len(difficulty) < 1 or difficulty == '':
            continue
        difficulty = difficulty.lower()
        if difficulty == 'easy' or difficulty == 'e':
            break
        elif difficulty == 'normal' or difficulty == 'n':
            del HANGMAN_PICS[8]
            del HANGMAN_PICS[7]
            break
        elif difficulty == 'hard' or difficulty == 'h':
            difficulty = 'hard'
            del HANGMAN_PICS[8]
            del HANGMAN_PICS[7]
            del HANGMAN_PICS[5]
            del HANGMAN_PICS[3]
            break
        else:
            continue

    main_game(difficulty, HANGMAN_PICS)

def random_word():
    words = {'Colors':'purple red blue violet green yellow brown black white cyan pink orange magenta indigo gray'.split(),
             'Shapes':'square triangle rectangle octagon hexagon trapezoid circle pentagon ellipse chevron rhombus septagon sphere'.split(),
             'Fruits':'apple banana orange lemon cherry strawberry grape grapefruit watermelon lime pear mango tomato cantaloupe'.split(),
             'Animals':'bear beaver lion lizard monkey moose goose otter panda snake rabbit shard sheep tiger turkey chicken cougar wolf zebra whale eagle fish'.split(),
             'Technology':'computer programmer cellphone facebook google virus keyboard internet microsoft console remote speaker microphone television monitor rocket spaceship satellite network wireless hotspot circuit electricity conducter'.split(),
             'Entertainment':'music game nintendo playstation controller gamepad joystick simulation virtual headset sports basketball baseball football'.split()
             }
    subject = words.keys()
    subject = random.choice(list(subject))
    answer = random.choice(words[subject])
    return subject, answer


def game_over(answer, HANGMAN_PICS):
    clear_screen()
    print(HANGMAN_PICS[len(HANGMAN_PICS)-1])
    print("\nAww, you didn't get the word right and the poor man was hanged.\nThe correct answer was " + answer.capitalize() + ".")
    play_again()

def game_win():
    clear_screen()
    print("\nCongratulations! You've managed to save the poor man!\nHe gives you a tearful hug and thanks you profusely.\nGood job! ^_^")
    play_again()

def play_again():
    while True:
        try_again = input("\nWould you like to play again (Y/N)? ")
        try_again = try_again.lower()
        if try_again == 'y' or try_again == 'yes':
            start_game()
        elif try_again == 'n' or try_again == 'no' or try_again == 'exit' or try_again == 'quit':
            sys.exit(1)
        else:
            continue

def main_game(difficulty, HANGMAN_PICS):
    missed_letters = []
    guessed_letters = []
    correct_letters = []
    subject, answer = random_word()

    while True:
        if len(missed_letters) == len(HANGMAN_PICS) - 1:
            game_over(answer, HANGMAN_PICS)
        print()
        print(HANGMAN_PICS[len(missed_letters)])
        print()
        display = ''
        for letter in answer:
            if letter in correct_letters:
                display += letter
            else:
                display += '-'
        if difficulty != 'hard':
            print(" - Topic: " + subject + " -")
        print("-> " + display.capitalize())
        if display == answer:
            game_win()
        print("\nLetters you've guessed so far = {}".format(guessed_letters))
        guess = input("Enter your guess: ")
        if guess.lower() == 'quit' or guess.lower() == 'exit':
            clear_screen()
            sys.exit(1)
        if not guess.isalpha() or len(guess) > 1 or len(guess) < 1:
            print("\nPlease guess a single letter.")
            clear_screen()
            continue
        guess = guess.lower()
        if guess in guessed_letters:
            print("\nYou've already guessed that letter")
            clear_screen()
            continue
        if guess in answer:
            correct_letters.append(guess)
        else:
            missed_letters.append(guess)
        guessed_letters.append(guess)

start_game()
