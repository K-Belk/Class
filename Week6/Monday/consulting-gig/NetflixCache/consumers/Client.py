from components.NetflixServer import NetflixServer


class Client:

    def __init__(self):
        self._server_connection = NetflixServer()

    def request_movie(self,movie):
        return self._server_connection.get_movie(movie)

    def request_top_movies(self):
        return self._server_connection.get_top_movies()
    
