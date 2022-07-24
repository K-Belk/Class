from consumers.Client import Client

if __name__ == "__main__":
    c = Client()
    print(c.request_top_movies())
    print(c.request_movie("The Room"))
    print(c.request_top_movies())
    print(c.request_movie("Bill and Ted's Excellent Adventure"))
    print(c.request_top_movies())
    print(c.request_movie("Star Wars"))
    print(c.request_top_movies())
