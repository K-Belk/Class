from array import array
from distutils.log import error
from db import DB

class Seed(DB):

    def __init__(self) -> None:
        super().__init__()

    def insert_data(self, table, columns, values):
        self.cur.execute(f"INSERT INTO {table} ({columns}) VALUES ({self.place_holders(columns)})", values)

    def place_holders(self, columns):
        arr = columns.split(', ')
        res = [ "%s" for i in range(len(arr))]
        return ', '.join(res)

    def main(self, table, columns, values):
        try:
            self.initialize_connection()
            self.insert_data(table, columns, values)
            self.conn.commit()
        except error:
            print("Ahh shit, someting didn't work")
            print(error)
        finally:
            self.close_connection()
