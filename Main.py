import Function
import sys
from os import system
from time import sleep

# A fuction to receive the choice of the user
def my_input():   
    print('What would you like to search?')
    x = input('Type "A" if you want to know more info about a volleyball player.\nType "B" if you want to know '
              'more info about a volleyball team.\nType "Q" if you want to quit the program.\nYour choice is: ')
    return x


def info_player():
    print("You chose to have more info about the volleyball player.\n")
    sys.exit("End program")


def info_team():
    print("You chose to have more info about the volleyball team.\n")
    sys.exit("End program")


def my_quit():
    sys.exit("You chose to quit the program.\n")


# map the inputs to the function blocks
options = {
    "A": info_player,
    "B": info_team,
    "Q": my_quit,
}

choice = my_input()    
    
while True:
    if choice == "A" or choice == "B" or choice == "Q":
        options[choice]()
    else:
        print("Your choice is not correct!!\n")
        # sleep for 2 seconds after printing output 
        sleep(2)
        system('cls')
        choice = my_input()
        