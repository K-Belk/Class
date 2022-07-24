class DatabaseAPI:

    def __init__(self):
        self._movies = self._initialize_db_api()

    @staticmethod
    def _initialize_db_api():
        with open("data/movie_database.txt", 'r') as movie_file:
            return (movie.strip() for movie in movie_file.readlines())

    def get_all_movies(self):
        return self._movies