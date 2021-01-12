from os import system
from time import sleep
import argparse
from xls_reader import extra_function
import xls_reader.function as function
import xls_reader.xls_read as xls_read

# Definition of positional and optional arguments
parser = argparse.ArgumentParser()
# The path must contain also the name of the xls file
parser.add_argument("xlsfile_fullpath", help="insert the full path of the xls file")
parser.add_argument("-v", "--verbosity", action="count", help="increase output verbosity")
# -v additional info for the user
# -vv additional info for the user and the developer
args = parser.parse_args()
file_full_path = args.xlsfile_fullpath

if args.verbosity is not None:
    print("Verbosity turned on.")
if args.verbosity == 1:
    print("The xls file is in this path: " + file_full_path)

# Database instance creation
db = xls_read.DataBase(file_full_path)
# Check if the database had been created
if function.exist_db(db):
    if args.verbosity == 2:
        name = "SALA CHIARA"
        print("TEST db: " + db.get_team_by_name(name))
    # Cleaning the screen
    system('cls')
    # First question (what would you like to search)
    choice = extra_function.input_request()
    # According to the answer, a function is called
    while True:
        if choice == "A" or choice == "B" or choice == "Q":
            if choice == "A":
                print(extra_function.info_player(db))
            if choice == "B":
                print(extra_function.info_team(db))
            if choice == "Q":
                print(extra_function.quit_program())
        else:
            print("Your choice is not correct!\n")
            # sleep for 2 seconds after printing output
            sleep(2)
            system('cls')
            choice = extra_function.input_request()

else:
    print("There was an error in the creation of the database.")
