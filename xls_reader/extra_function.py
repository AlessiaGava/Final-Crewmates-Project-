import sys
import xls_reader.function as function
from os import system
from time import sleep


def quit_program():
    """
    This function allows, through a system call, to quit the program.
    """
    sys.exit("You chose to quit the program.\n")


def input_request():
    """
    This function allows the user to make a choice among the proposed possibilities.

    :return: a letter in uppercase
    :rtype: String
    """
    print('What would you like to search?')
    x = input('Type "A" if you want to know more info about a volleyball player.\nType "B" if you want to know '
              'more info about a volleyball team.\nType "Q" if you want to quit the program.\nYour choice is: ')
    return x.upper()


def input_request_a():
    """
    This function allows the user to insert the name of a volleyball player.

    :return: the name of a volleyball player in uppercase
    :rtype: String
    """
    print('Who is the player you want more info about?')
    x = input('Type firstly the surname and secondly the name of the player: ')
    return x.upper()


def input_request_b():
    """
    This function allows the user to insert the name of a volleyball team.

    :return: the name of a volleyball team
    :rtype: String
    """
    print('Who is the team you want more info about?')
    x = input('Type the complete name of the team: ')
    return x.upper()


def input_request_a_info():
    """
    This function allows the user to make a choice among the proposed possibilities.

    :return: a letter in uppercase
    :rtype: String
    """
    print('What would you like to know about the volleyball player chosen?')
    x = input('Type "H" if you want to know the volleyball player\'s height \nType "N" if you want to know '
              'the volleyball player\'s nationality \nType "B" if you want know the volleyball player\'s birthday\n'
              'Type "R" if you want know the volleyball player\'s role \nType "T" if you want know the volleyball '
              'player\'s team \nType "Q" if you want to quit the program \nYour choice is: ')
    return x.upper()


def info_player(db):
    """
    This function uses the return value of the function input_request_a to check, using the function exist_player
    of the file function.py, if the name inserted is in the database and, if it exists in the database, the function
    uses the return value of the function input_request_a_info to call a function of the function.py file.

    :param db: an object that identifies the database
    :type db: Object
    """
    fullname_player = input_request_a()

    if function.exist_player(db, fullname_player):

        choice = input_request_a_info()

        while True:
            if choice == "H" or choice == "N" or choice == "B" or choice == "R" or choice == 'T' or choice == "Q":
                if choice == "H":
                    print(function.check_player_height(db, fullname_player))
                if choice == "N":
                    print(function.check_player_nationality(db, fullname_player))
                if choice == "B":
                    print(function.check_player_birth(db, fullname_player))
                if choice == "R":
                    print(function.check_player_role(db, fullname_player))
                if choice == "T":
                    print(function.check_player_team(db, fullname_player))
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
    """
    This function uses the return value of the function input_request_b to call the function check_team of the
    function.py file.

    :param db: an object that identifies the database
    :type db: Object
    """
    print("You chose to have more info about the members of the volleyball team.\n")
    fullname_team = input_request_b()

    print(function.check_team(db, fullname_team))

    sleep(2)
    quit_program()
