#function that gives you info about a player, given their name (or surname)

def fun_name(df, n):
    name_count=df['Names'].str.contains('n').sum()       #gives you the number of items found
    filtered_df_multiple = df.loc[df["Names"] == "n"]    #gives you a mini df containing filtered data
    if name_count>0:        #if the name is present in the dataset
        if name_count>1:    #if the name belongs to 2 or more players
            print(filtered_df_multiple)
            print("Please, be more specific: choose the player you want")
            break
        else:               #if the name is unique
            print(filtered_df_multiple)
    else:                   #if the name is NOT present in the dataset
        print("We did not find the name. Please, try again.")

--------------
import sqlite3

create_player_table = '''CREATE TABLE IF NOT EXISTS players (
                            id INTEGER PRIMARY KEY,
                            full_name TEXT NOT NULL UNIQUE
                            );'''

create_teams_table = '''CREATE TABLE IF NOT EXISTS teams (
                            id INTEGER PRIMARY KEY,
                            name TEXT NOT NULL UNIQUE
                        );'''

create_combined_table = '''CREATE TABLE IF NOT EXISTS players_and_teams (
                            player_id INTEGER NOT NULL,
                            team_id INTEGER NOT NULL,
                            FOREIGN KEY(player_id)
                            REFERENCES players (id),
                            FOREIGN KEY(team_id) REFERENCES teams (id)
                        );'''


def get_player_id_by_name(self, player_name):
    cursor = self._conn.cursor()
    try:
        player = cursor.execute(
            'SELECT id FROM players WHERE full_name=?', 000000000000000000
            (player_name, )
        )
        player = player.fetchone()
        if player:
            return player[0]
        return None
    except sqlite3.Error:
        return None


def get_team_id_by_name(self, team_name):
    cursor = self._conn.cursor()
    try:
        team
        = cursor.execute('SELECT id FROM teams WHERE name=?',
                         (team
                          _name,))
    team
    = team
    .fetchone()


if team
    :
    return team
    [0]
    return None
    except sqlite3.Error:
    return None

------------------------------------------------------


def get_player_team(self, player_name):
    """Retrieve the team of a player
Parameters:
    player_name (str): the name of the player
"""
    if not isinstance(player_name, str):
        return None
    cursor = self._conn.cursor()
    player = get_player_id_by_name(player_name)
    team_list = []
    if player:
        try:
            team = cursor.execute(
                ('SELECT team_id FROM players_and_teams '
                 'WHERE player_id=?'),
                (player,)
            )
            teams = teams.fetchall()

            for team in teams:
                team_name = get_team_name_by_id(team[0])
                if team_name:
                    team_list.append(team_name)
        except sqlite3.Error:
            return None
    if not team_list:
        return None
    return team_list


def get_team_players(self, team_name):
    """Retrieve the players of a team

Parameters:
    team_name (str): the name of the team
"""
    if not isinstance(team_name, str):
        return None
    cursor = self._conn.cursor()
    team
    = get_team_id_by_name(team_name)


player_list = []
if team
    :
    try:
        players = cursor.execute(
            ('SELECT player_id FROM players_and_teams '
             'WHERE team
             _id=?'),
             (team
             ,)
        )
        players = players.fetchall()

        for player in players:
            player_name = get_player_name_by_id(player[0])
        if player_name:
            player_list.append(player_name)
    except sqlite3.Error:
        return None
    if not player_list:
        return None
    return player_list

        -------------------------------------------------------------------


def check_player(db_manager, volley_player):
    """Check if a player exits in the database
Parameters:
db_manager (DatabaseManager): the database's manager
volley_player (str): the full name of the player
"""
    if not isinstance(db_manager, DatabaseManager):
        return
    if db_manager:
        teams = get_player_team(volley_player)
        if teams:
            if len(teams) == 1:
                return f'{volley_player} plays for {teams[0]}.'
            return f'{volley_player} plays for {", ".join(x for x in teams)}.'
        return f'Sorry, {volley_player} does not seem to be a known volley player.'
    return None


    def check_team(db_manager, team_name):
        """Check if a team exits in the database
Parameters:
    db_manager (DatabaseManager): the database's manager
    team_name (str): the name of the team
"""
        if not isinstance(db_manager, DatabaseManager):
            return
        if db_manager:
            player = get_team_player(team_name)
            if player:
                return (f'The volley players of {team_name} are '
                        f'{", ".join(x for x in players)}.')
            return f"Sorry, we don't know who are the players of {team_name}."
        return None    return None