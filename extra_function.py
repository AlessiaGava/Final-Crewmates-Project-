import sys
import function
from os import system
from time import sleep


def quit_program():
    sys.exit("You chose to quit the program.\n")


def input_request():
    print('What would you like to search?')
    x = input('Type "A" if you want to know more info about a volleyball player.\nType "B" if you want to know '
              'more info about a volleyball team.\nType "Q" if you want to quit the program.\nYour choice is: ')
    return x.upper()


def input_request_a():
    print('Who is the player you want more info about?')
    x = input('Type firstly the surname and secondly the name of the player: ')
    return x.upper()


def input_request_b():
    print('Who is the team you want more info about?')
    x = input('Type the complete name of the team: ')
    return x


def input_request_a_info():
    print('What would you like to know about the volleyball player chosen?')
    x = input('Type "H" if you want to know the volleyball player\'s height. \nType "N" if you want to know '
              'the volleyball player\'s nationality. \nType "B" if you want know the volleyball player\'s birthday\n'
              'Type "R" if you want know the volleyball player\'s role \nType "Q" if you want to quit the program. '
              '\nYour choice is: ')
    return x.upper()


def info_player(db):
    fullname_player = input_request_a()

    if function.exist_player(db, fullname_player):

        choice = input_request_a_info()

        while True:
            if choice == "H" or choice == "N" or choice == "B" or choice == "R" or choice == "Q":
                if choice == "H":
                    print(function.check_player_height(db, fullname_player))
                if choice == "N":
                    print(function.check_player_nationality(db, fullname_player))
                if choice == "B":
                    print(function.check_player_birth(db, fullname_player))
                if choice == "R":
                    print(function.check_player_role(db, fullname_player))
                if choice == "Q":
                    print(quit_program())
                sleep(2)
                quit_program()
            else:
                print("Your choice is not correct!\n")
                # sleep for 2 seconds after printing output
                sleep(2)
                system('cls')
                choice = input_request_a_info()
    else:
        print("Player not found.")
        # sleep for 2 seconds after printing output
        sleep(2)
        system('cls')
        info_player(db)


def info_team(db):
    print("You chose to have more info about the members of the volleyball team.\n")
    fullname_team = input_request_b()

    print(function.check_team(db, fullname_team))

    sleep(2)
    quit_program()
