# Final-Crewmates-Project-

# What are the charcateristics of your favorite female volley player?
# How is your favorite volley team composed?

### Our goal

Our project aims to give the possibilityto volleyball fans to know more about the characteristics of their favorite female players of Serie A of volleyball or discover the composition of the teams.

In this repository, it’s possible to find all the necessary things to reach these objectives.

### UML Volley Project


```python

```

### Dataset Volley

Thanks to dataset_volley.csv and dataset_volley.xlsx, we have a list of all the female players of Serie A in Italy with their information about team, role, year of birth, height, and nationality.

The teams that play in Serie A for the year 2020 are 13 but the number can vary.

The roles in the volleyball game can be:
- libero
- palleggiatrice
- schiacciatrice
- centrale
- opposto

In the column "birth" are written only the years of birth of the players.

In the column "heights" are expressed in cm all the heights of the players.

Although the players play in Italian teams, many of them have foreign nationalities.

### xlsx_read.py

In this file, we imported ```sqlite3``` and ```pandas``` to upload and manage the dataset and the functions.

Here is created the class ```Database()``` where functions are loaded and where the dataset is managed.
In this class there are several functions created thanks to ```sqlite```, including ```get_all_by_name```, ```get_team_by_name``` , ```get_role_by_name``` , ```get_height_by_name``` , ```get_nationality_by_name``` , ```get_birth_by_name``` and ```get_player_by_team```.

The commands used are:
- CREATE TABLE
- SELECT * FROM
- PRAGMA
- SELECT … FROM … WHERE 

### extra_function.py

In this file, we created the functions regarding the input that the user should provide and the possibility to quit the program.
Here we imported:
- ```sys``` that provides information about constants, functions, and methods of the Python interpreter.
- ```os.system``` that executes the command in a subshell.
- ```time.sleep``` to suspend the execution of the current thread for a given number of seconds and to create a sort of delay.
- ```function``` that is one of our .py files that contains all the functions related to the team and the player.

### function.py

In the file ```function.py``` there are all the functions related to the team, the role, the year of birth, the height, and the nationality of the players.

Here we imported from xlsx_read the ```Database```.

The function ```exist_db``` checks if the database has been created and then with the ```exist_player``` function verifies that the player's name is in the database.

Thanks to the function ```check_player_all_stats``` the user can discover all the information about the female volley player searched.

In the functions ```check_player_height```, ```check_player_nationality```, ```check_player_birth```, ```check_player_role``` , and ```check_player_team``` , giving the name of the player is possible to verify its height, nationality, birth, role, and team.

With the function ```check_team```, the user can provide the name of a team and ask the system to know the components of the team.

### tests

In our project, we decided also to make some tests and to do this, in ```test_function.py``` we imported ```unittest``` to test a unit of source code and also two of our .py files: ```function``` and ```csv_read```.

We made three types of unit tests: 
- ```test_smoke_function``` to reveal simple failures 
- ```test_invalid_inputs_1``` where we entered a name other than those in the dataset
- ```test_corner_case``` where the input is empty

### volley.py

This is the file that interacts in the most direct way with the final user.

It is possible to see the info required by the user or to add instances if the database exists.

The user has to choose to input:
- "A" if he/she wants to know information about the player.
- "B" if he/she wants to know the composition of a team.
- "Q" if he/she wants to quit the program.

If he inputs something else, the algorithm will stop and quit.


In this .py file we imported:
- ```os.system``` that executes the command in a subshell
- ```time.sleep``` to suspend the execution of the current thread for a given number of seconds and to create a sort of delay.
- ```argparse``` that defines the location of the data folder that contains the excel file.
- ```extra_function```, ```function``` and ```xlsx_read``` that are some of our .py files.


```python

```
