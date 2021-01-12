# Final-Crewmates-Project-

# What are the charcateristics of your favorite female volleyball player?
# How is your favorite volleyball team composed?

### Our goal

Our project aims to give the possibility to volleyball fans to know more about the characteristics of their favorite female players of Serie A of volleyball or discover the composition of the teams.

In this repository, it’s possible to find all the necessary things to reach these objectives.

### UML Volley Project

It is possible to find the image of the UML of our project in the repository.

### Dataset Volley

Thanks to ```dataset_volley.xls```, we have a list of all the female players of Serie A in Italy with their information about team, role, year of birth, height, and nationality.

The teams that play in Serie A for the year 2020 are 13.

The roles in the volleyball game can be:
- libero
- palleggiatrice
- schiacciatrice
- centrale
- opposto

In the column "birth" are written only the years of birth of the players.

In the column "heights" are expressed in cm all the heights of the players.

Although the players play in Italian teams, many of them have foreign nationalities.

### xls_read.py

In this file, we imported ```sqlite3``` and ```pandas``` to upload and manage the dataset and the functions.

Here is created the class ```DataBase()``` that imports data from an xls file, instantiates and handles the database of volleyball players of the Italian A1 Series.

In this class there are several functions, used to recall info from the database, created thanks to ```sqlite```.

The commands used are:
- CREATE TABLE
- SELECT * FROM
- PRAGMA
- SELECT … FROM … WHERE 

### function.py

In the file ```function.py``` there are all the functions related to the team, the role, the year of birth, the height, and the nationality of the players.

Here we imported from xlsx_read the ```Database```.

The function ```exist_db``` checks if the database has been created and then the ```exist_player``` function verifies that the player's name is in the database.

The function ```check_player_all_stats``` returns all the information about the female volley player searched.

In the functions ```check_player_height```, ```check_player_nationality```, ```check_player_birth```, ```check_player_role``` , and ```check_player_team``` , giving the name of the player, it is returned her height, nationality, birth, role, and team.

The function ```check_team```, provided the name of the team selected, returns the components of the team.

### extra_function.py

In this file, we created the functions regarding the management of the inputs that the user should provide.
Here we imported:
- ```sys``` that provides information about constants, functions, and methods of the Python interpreter.
- ```os.system``` that executes the command in a subshell.
- ```time.sleep``` to suspend the execution of the current thread for a given number of seconds and to create a sort of delay.
- ```xls_reader.function``` that is one of our .py files that contains all the functions related to the teams and the players.

### test_function.py

In our project, we decided also to make some tests and to do this, in ```test_function.py``` we imported ```unittest``` to test the .py file ```function```. If the test passes, it means that the database created in the ```xls_read``` file works correctly.

We made three types of unit tests: 
- ```test_smoke_function``` to reveal simple failures.
- ```test_invalid_inputs_1``` where the input is an unexpected string.
- ```test_corner_case``` where the input is an empty string.

### volley.py

Running this python file, the program is launched. ```volley.py``` is the core file that, according to the input given by the user, calls the right function.

In this .py file we imported:
- ```os.system``` that executes the command in a subshell.
- ```time.sleep``` to suspend the execution of the current thread for a given number of seconds and to create a sort of delay.
- ```argparse``` that provides the arguments required by the user.
- ```xls_reader.extra_function```, ```xls_reader.function``` and ```xls_reader.xls_read``` that are some of our .py files.

### requirements.txt

It is possible to find the requirements file in our repository. It contains the python packages required to run the program.
