# Shopping list app
import string
import os
import sys
import math


print("\nWhat should we pick up at the store?  ^_^")

# create a new empty list name shopping list
shopping_list = [0]

# Create a function for clearing the screen to make app look neater
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# create a function named add_to_list
def add_to_list(item):
    show_list()
    item = item.capitalize()
    if shopping_list[0] == 0:
        shopping_list.pop(0)
        shopping_list.append(item)
        return
    for add in range(len(shopping_list)):
        if item.lower() == shopping_list[add].lower():
            print("That item is already on the list.")
            return
    while True:
        position = input("Where should I add ** {} ** into the list?\n"
                                 "(or press enter to add to the end of the list)\n"
                                 "> ".format(item))
        if position == "":
            shopping_list.append(item)
            show_list()
            return
            break
        elif not position.isdigit():
            print("Please enter a valid number.")
            continue
        else:
            position = int(position)
        if position < 1 or position > len(shopping_list) + 1:
            print("Please enter a valid placement for the list.")
            continue
        else:
            shopping_list.insert(position - 1, item)
            break
    show_list()
    return

# create a function to help users
def show_help():
    if shopping_list[0] != 0:
        clear_screen()
    print("""\nEnter 'V' or 'VIEW' to view the current list.
Enter 'R' or 'Remove' to delete items from the list.
Enter 'H' or 'HELP' for this help.
Enter 'D' or 'DONE' to stop adding items.
Enter 'Q' or 'QUIT' to exit.""")

# function for showing the list
def show_list():
    if shopping_list[0] == 0:
        return
    clear_screen()
    print("\nCurrent items in list:\n" + "-" * 22)
    for items in range(len(shopping_list)):
        item_num = str(items+1) + ")"
        print("{:<4} {}".format(item_num, shopping_list[items]))
    print("-" * 22)
    return

# Create a function for removing items from the list
def remove_from_list():
    show_list()
    while True:
        del_item = input("Enter the number or name of the item you wish to remove.\n"
                             "(or press enter to cancel)>  ")
        try:
            shopping_list.remove(del_item.capitalize())
            show_list()
            return
        except ValueError:
            pass
        if del_item == "":
            return
            break
        elif not del_item.isdigit():
            print("Please enter an item on the list.")
            continue
        if del_item.isdigit():
            del_item = int(del_item)
            if del_item < 1 or del_item > len(shopping_list):
                print("Please enter an item on the list.")
                continue
            else:
                del shopping_list[del_item - 1]
                break
    show_list()
    return
            
show_help()
# Create a loop to ask for items to put on the list
while True:
    if shopping_list[0] == 0:
        print("\nThere are currently no items in your shopping list.\nPlease add items.")
    new_item = input("> ")
    new_item = new_item.lower()
    if new_item == 'done' or new_item == 'd':
        break
    elif new_item == 'help' or new_item == 'h':
        show_help()
        continue
    elif new_item == 'view' or new_item == 'v':
        show_list()
        continue
    elif new_item == 'r' or new_item == 'remove':
        remove_from_list()
        continue
    elif new_item == 'q' or new_item == 'quit':
        sys.exit(1)
    elif not new_item.isalpha() or (len(new_item) <= 2):
        print("Please enter a valid item name.\n")
        continue
    # call add_to_list with new_item as an argument
    else:
        add_to_list(new_item)
        continue
        
show_list()