import sqlite3


class Data:
    __data_list = []

    def __init__(self, list=None):
        self.__data_list = list

    def make_connection(self):
        conn = sqlite3.connect("data")
        return conn

    def add_data(self):
        with self.make_connection() as conn:
            command = "INSERT INTO pizza VALUES(?, ?, ?, ?, ?)"
            conn.execute(command, self.__data_list)
            conn.commit()

    def get_data(self, table_name):
        with self.make_connection() as conn:
            command = "SELECT * FROM " + table_name
            table = conn.execute(command)
            return table.fetchall()
