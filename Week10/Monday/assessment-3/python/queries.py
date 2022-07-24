from distutils.log import error
from db import DB

class Queries(DB):

    def __init__(self) -> None:
        super().__init__()

    def get_query(self, query):
        self.cur.execute(query)

    def main(self, query):
        try:
            self.initialize_connection()
            self.get_query(query)
            print(self.cur.fetchall())
        except error:
            print("Ahh shit, someting didn't work")
            print(error)
        finally:
            self.close_connection()

