import csv
import os.path

class Video:

    def __init__(self, id, title, rating, release_year, copies_available):
        self.id = id
        self.title = title
        self.rating = rating
        self.release_year = int(release_year)
        self.copies_available = int(copies_available)

    @classmethod
    def read_inventory(cls):
        rentals = {}
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/inventory.csv")
        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                rentals[row['id']] = (Video(**dict(row)))
        return rentals

    