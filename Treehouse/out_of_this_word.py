import random
import os

WORDS = ("treehouse", "python", "learner")

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def prompt_for_words(challenge):
    clear_screen()
    guesses = set()
    global player
    player += 1
    print("Player {}".format(player))
    print("-"*20)
    print("Try to find all the words in the word: " + challenge_word)
    print("(Enter Q to Quit)")
    while True:
        guess = input("{} words > ".format(len(guesses)))
        if guess.lower() == 'q' or guess.lower() == 'quit':
            break
        guesses.add(guess.capitalize())
    return guesses

def output_results(results):
    for word in results:
        print("* " + word)

player = 0
challenge_word = random.choice(WORDS)

player1_words = prompt_for_words(challenge_word)
player2_words = prompt_for_words(challenge_word)

clear_screen()
print("-- Player 1 Results --")
player1_unique = player1_words - player2_words
print("{} guesses, {} unique".format(len(player1_words),len(player1_unique)))
output_results(player1_unique)
print("-"*22)

print("-- Player 2 Results --")
player2_unique = player2_words - player1_words
print("{} guesses, {} unique".format(len(player2_words),len(player2_unique)))
output_results(player2_unique)
print("-"*22)

print("-- Shared Guesses --")
shared_words = player1_words & player2_words
output_results(shared_words)
