import sqlite3
import pandas as pd

'''possibili aggiunte sistema di gestione csv e xls caricamneto/salvataggio INTELIGENTE'''


class DataBase():
    """
    Class that import from an xlsx, instantiate and handle the database of player
    contain several function to reacall info from database

    :var self._table_name: The name of core table
    :type self._table_name: str
    :var self._df: pandas dataframe containing dataset of player
    :type self._df: pandas.DataFrame
    """

    def __init__(self):
        """
        Constructor method
        """
        self._table_name = "volley_player"
        self._df = pd.read_excel("Data/dataset_volley.xlsx")
        self._connect()
        self._create_team()

    def _connect(self):
        """
        Load dataset from dataframe

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
        Generate a table whit primary key team name

        :var self.cursor: The cursor obj of dataset
        :type self.cursor: sqlite3.cursor
        """
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS volley_team(
                            TEAM TEXT PRIMARY KEY NOT NULL UNIQUE);''')

    def show_all(self):
        """
        Function that select all data of dateset and print them

        :return: All data of players
        :rtype: list
        """
        return self.conn.execute("SELECT * FROM volley_player").fetchall()

    def show_col(self):
        """
        Extract from dataset all columns name

        :return: Columns name
        :rtype: list
        """
        return self.conn.execute("PRAGMA table_info(volley_player);").fetchall()

    def get_name(self):
        """
        Extract from dataset all name of player

        :return: Players name
        :rtype: list
        """
        lis = self.conn.execute('SELECT NAME FROM volley_player').fetchall()
        name = []
        for i in lis:
            name.append(i[0])
        return name

    def get_all_by_name(self, player_name):
        """
        Extract from dataset all info of selected player

        :param player_name: Full name of player searched
        :return: Info of selected player
        :rtype: list
        """
        cursor = self.conn.cursor()
        try:
            team = cursor.execute('SELECT * FROM volley_player WHERE name=?', (player_name,))
            team = team.fetchall()

            if team:
                return team[0]
            return None

        except sqlite3.Error:
            print("A error has occured")
            return None

    def get_team_by_name(self, player_name):
        """
        Extract from dataset the name of the team to which the selected player belongs

        :param player_name: Full name of player searched
        :return: team name
        :rtype: list
        """
        cursor = self.conn.cursor()
        try:
            team = cursor.execute('SELECT TEAM FROM volley_player WHERE name=?', (player_name,))
            team = team.fetchone()

            if team:
                return team[0]
            return None

        except sqlite3.Error:
            print("A error has occured")
            return None

    def get_role_by_name(self, player_name):
        """
        Extract from dataset the role of the selected player

        :param player_name: Full name of player searched
        :return: player roles
        :rtype: list
        """
        cursor = self.conn.cursor()
        try:
            team = cursor.execute('SELECT ROLE FROM volley_player WHERE name=?', (player_name,))
            team = team.fetchone()

            if team:
                return team[0]
            return None

        except sqlite3.Error:
            print("A error has occured")
            return None

    def get_height_by_name(self, player_name):
        """
        Extract from dataset height of the selected player

        :param player_name: Full name of player searched
        :return: player heights
        :rtype: list
        """
        cursor = self.conn.cursor()
        try:
            team = cursor.execute('SELECT HEIGHT FROM volley_player WHERE name=?', (player_name,))
            team = team.fetchone()

            if team:
                return team[0]
            return None

        except sqlite3.Error:
            print("A error has occured")
            return None

    def get_nationality_by_name(self, player_name):
        """
        Extract from dataset nationality of the selected player

        :param player_name: Full name of player searched
        :return: player nationalities
        :rtype: list
        """
        cursor = self.conn.cursor()
        try:
            team = cursor.execute('SELECT NATIONALITY FROM volley_player WHERE name=?', (player_name,))
            team = team.fetchone()

            if team:
                return team[0]
            return None

        except sqlite3.Error:
            print("A error has occured")
            return None

    def get_birth_by_name(self, player_name):
        """
        Extract from dataset year of birth of the selected player

        :param player_name: Full name of player searched
        :return: player year of births
        :rtype: list
        """
        cursor = self.conn.cursor()
        try:
            team = cursor.execute('SELECT BIRTH FROM volley_player WHERE name=?', (player_name,))
            team = team.fetchone()

            if team:
                return team[0]
            return None

        except sqlite3.Error:
            print("A error has occured")
            return None

    def get_player_by_team(self, team):
        """
        Extract form dataset names of all players belonging to a team

        :param team: Name of a team
        :return: Players names
        :rtype: list
        """
        cursor = self.conn.cursor()
        try:
            player = cursor.execute('SELECT NAME FROM volley_player WHERE TEAM=?', (team,))
            player = player.fetchall()

            if player:
                return player
            return None

        except sqlite3.Error:
            print("A error has occured")
            return None

    def close_con(self):
        self.conn.close()


# testing thing
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
