import psycopg2

class DB:

    def __init__(self) -> None:
        self.conn = None
        self.cur = None

    def initialize_connection(self):
        self.conn = psycopg2.connect("dbname=sell_stuff user=kevinlbelk")
        self.cur = self.conn.cursor()
        
    def close_connection(self):
        self.cur.close()
        self.conn.close()