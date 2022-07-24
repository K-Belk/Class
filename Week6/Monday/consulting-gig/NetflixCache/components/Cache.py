from components.DatabaseAPI import DatabaseAPI
from structures.Queue import Queue

class Cache(Queue):
    MAX_ITEMS = 3

    def __init__(self):
        super().__init__()
        self.db_api = DatabaseAPI()
        for movie in self.db_api.get_all_movies():
            self.enqueue(movie)
        
    def enqueue(self,value):
        if len(self._base) >= Cache.MAX_ITEMS:
            self.dequeue()
        super().enqueue(value)
        return self.peek_back()

    def get_cached(self, item):
        if item in self._base:
            return self._base[self._base.index(item)]
        else:
            return self.enqueue(item)

    def get_top_recent(self):
        return self._base
