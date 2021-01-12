import sqlite3
import pandas as pd


class DataBase():
    """
    Class that imports data from an xls file, instantiates and handles the database of volleyball players of
    the Italian A1 Series. It contains several functions to recall info from the database.

    :var self._table_name: the name of the core table
    :type self._table_name: String
    :var self._df: pandas dataframe containing the dataset of players
    :type self._df: pandas.DataFrame
    """

    def __init__(self, file_full_path):
        """
        Constructor method.
        """
        self._table_name = "volley_player"
        self._df = pd.read_excel(file_full_path)
        self._connect()
        self._create_team()

    def _connect(self):
        """
        Load dataset from dataframe.

        :var self.conn: loaded dataset in sqlite3
        :type self.conn: sqlite3.Connection
        """
        try:
            self.conn = sqlite3.connect(':memory:')
            self._df.to_sql(self._table_name, con=self.conn, if_exists='replace', index=True)
        except Exception:
            pass

    def _create_team(self):
        """
        Generate a table whit primary key team name.

        :var self.cursor: the cursor obj of dataset
        :type self.cursor: sqlite3.cursor
        """
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS volley_team(
                            TEAM TEXT PRIMARY KEY NOT NULL UNIQUE);''')

    def show_all(self):
        """
        Function that selects all data of dataset and prints them.

        :return: all data of players
        :rtype: List
        """
        return self.conn.execute("SELECT * FROM volley_player").fetchall()

    def show_col(self):
        """
        Function that extracts from dataset all columns' names.

        :return: columns' names
        :rtype: List
        """
        return self.conn.execute("PRAGMA table_info(volley_player);").fetchall()

    def get_name(self):
        """
        Function that extracts from dataset all names of the players.

        :return: players' names
        :rtype: List
        """
        lis = self.conn.execute('SELECT NAME FROM volley_player').fetchall()
        name = []
        for i in lis:
            name.append(i[0])
        return name

    def get_all_by_name(self, player_name):
        """
        Function that extracts from dataset all info of the selected player.

        :param player_name: full name of the player searched
        :return: info of the selected player
        :rtype: List
        """
        cursor = self.conn.cursor()
        try:
            team = cursor.execute('SELECT * FROM volley_player WHERE name=?', (player_name,))
            team = team.fetchall()

            if team:
                return team[0]
            return None

        except sqlite3.Error:
            print("A error has occurred.")
            return None

    def get_team_by_name(self, player_name):
        """
        Function that extracts from dataset the name of the team to which the selected player belongs

        :param player_name: full name of the player searched
        :return: team name
        :rtype: List
        """
        cursor = self.conn.cursor()
        try:
            team = cursor.execute('SELECT TEAM FROM volley_player WHERE name=?', (player_name,))
            team = team.fetchone()

            if team:
                return team[0]
            return None

        except sqlite3.Error:
            print("A error has occurred.")
            return None

    def get_role_by_name(self, player_name):
        """
        Function that extracts from dataset the role of the selected player.

        :param player_name: full name of the player searched
        :return: player's role
        :rtype: List
        """
        cursor = self.conn.cursor()
        try:
            team = cursor.execute('SELECT ROLE FROM volley_player WHERE name=?', (player_name,))
            team = team.fetchone()

            if team:
                return team[0]
            return None

        except sqlite3.Error:
            print("A error has occurred.")
            return None

    def get_height_by_name(self, player_name):
        """
        Function that extracts from dataset the height of the selected player.

        :param player_name: full name of the player selected
        :return: player's height
        :rtype: List
        """
        cursor = self.conn.cursor()
        try:
            team = cursor.execute('SELECT HEIGHT FROM volley_player WHERE name=?', (player_name,))
            team = team.fetchone()

            if team:
                return team[0]
            return None

        except sqlite3.Error:
            print("A error has occurred.")
            return None

    def get_nationality_by_name(self, player_name):
        """
        unction that extracts from dataset the nationality of the selected player.

        :param player_name: full name of the player selected.
        :return: player's nationality
        :rtype: List
        """
        cursor = self.conn.cursor()
        try:
            team = cursor.execute('SELECT NATIONALITY FROM volley_player WHERE name=?', (player_name,))
            team = team.fetchone()

            if team:
                return team[0]
            return None

        except sqlite3.Error:
            print("A error has occurred.")
            return None

    def get_birth_by_name(self, player_name):
        """
        Function that extracts from dataset the year of birth of the selected player.

        :param player_name: full name of the player selected
        :return: player's year of birth
        :rtype: List
        """
        cursor = self.conn.cursor()
        try:
            team = cursor.execute('SELECT BIRTH FROM volley_player WHERE name=?', (player_name,))
            team = team.fetchone()

            if team:
                return team[0]
            return None

        except sqlite3.Error:
            print("A error has occurred.")
            return None

    def get_player_by_team(self, team):
        """
        Function that extracts form dataset the names of all players belonging to the same team.

        :param team: name of a team
        :return: players' names
        :rtype: List
        """
        cursor = self.conn.cursor()
        try:
            player = cursor.execute('SELECT NAME FROM volley_player WHERE TEAM=?', (team,))
            player = player.fetchall()

            if player:
                return player
            return None

        except sqlite3.Error:
            print("A error has occurred.")
            return None

    def close_con(self):
        """
        Connection closed.
        """
        self.conn.close()


# testing
if __name__ == "__main__":
    test = DataBase()
    name = "SALA CHIARA"
    print(test.show_col())
    print(test.get_team_by_name(name))
    print(test.get_birth_by_name(name))
    print(test.get_role_by_name(name))
    print(test.get_height_by_name(name))
    print(test.get_nationality_by_name(name))
    print(test.get_all_by_name(name))
    test.close_con()
