import sqlite3
import pandas as pd

'''possibili agiunte sistema di gestione csv e xls caricamneto/salvataggio INTELIGENTE '''


class DataBase():

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

    def close_con(self):
        self.conn.close()


if __name__ == "__main__":
    test = DataBase()
    print(test.show_all())
    test.close_con()