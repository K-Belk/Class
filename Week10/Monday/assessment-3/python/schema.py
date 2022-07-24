from distutils.log import error
from db import DB

class Schema(DB):

    def __init__(self) -> None:
        super().__init__()

    def create_tables(self, name, values):
        self.cur.execute(f"DROP TABLE IF EXISTS {name} CASCADE")
        self.cur.execute(f"CREATE TABLE {name} ({values})")
        

    def main(self, name, values):
        try:
            self.initialize_connection()
            self.create_tables(name, values)
            self.conn.commit()
        except error:
            print("Ahh shit, someting didn't work")
            print(error)
        finally:
            self.close_connection()
