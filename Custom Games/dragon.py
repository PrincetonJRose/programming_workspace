import random
import time
import sys
import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def main_game():
    print("""You are in a land full of dragons. In front of you,
you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon
is greedy and hungry, and will eat you on sight.""")
    
    cave = ''
    while cave != '1' and cave != '2':
        cave = input("\nWhich cave will you enter? (1 or 2): ")
        
    print("\nYou approach the cave...")
    time.sleep(2)
    print("It is dark and spooky...")
    time.sleep(2)
    print("A large dragon jumps out in front of you!")
    time.sleep(2)
    print("He opens his jaws and...")
    time.sleep(2)
    
    friendly_cave = str(random.randint(1,2))
    
    if friendly_cave == cave:
        print("\nGives you his treasure! Yay!  ^_^")
    else:
        print("\nWastes no time in gobbling you down in one bite!  O_O")
        
    while True:
        play_again = input("Would you like to play again (Y/N)?  ")
        if play_again.lower() == 'y' or play_again.lower() == 'yes':
            print()
            clear_screen()
            main_game()
        elif play_again.lower() == 'n' or play_again.lower() == 'no':
            sys.exit(1)
        else:
            continue

main_game()