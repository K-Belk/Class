from components.Cache import Cache

class NetflixServer:

    def __init__(self):
        self._cache = Cache()

    def get_movie(self, movie):
        return self._cache.get_cached(movie)

    def get_top_movies(self):
        return self._cache.get_top_recent()
        