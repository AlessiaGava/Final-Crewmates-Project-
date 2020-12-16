import sqlite3
import pandas as pd


class DataBase():
    """
        classe che carica e gestisce il dataset
        varie funzioni
    """

    def __init__(self):
        self._table_name = "volley_player"
        self._df = pd.read_excel("Data/dataset_volley.xlsx")
        self._connect()
        self._create_team()

    def _connect(self):
        try:
            self.conn = sqlite3.connect(':memory:')
            self._df.to_sql(self._table_name, con=self.conn, if_exists='replace', index=True)
        except Exception:
            pass

    def _create_team(self):
        cursor = self.conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS volley_team(
                            TEAM TEXT PRIMARY KEY NOT NULL UNIQUE);''')

    def show_all(self):
        return self.conn.execute("SELECT * FROM volley_player").fetchall()

    def show_col(self):
        return self.conn.execute("PRAGMA table_info(volley_player);").fetchall()

    def get_all_by_name(self, player_name):
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
