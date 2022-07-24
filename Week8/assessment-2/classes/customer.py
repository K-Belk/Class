from terminaltables import AsciiTable
import csv
import os.path

class Customer:

    def __init__(self, id, account_type, first_name, last_name, current_video_rentals) -> None:
        self.id = id
        self.account_type = account_type
        self.first_name = first_name
        self.last_name = last_name
        if len(current_video_rentals) != 0:
            self.current_video_rentals = current_video_rentals.split("/")
        else:
            self.current_video_rentals = []

    def display_customer(self):
        display = []
        index = 0
        display.append(['','current video rentals'])
        for video in self.current_video_rentals:
            display.append([index, video])
            index +=1
        customer_display = AsciiTable(display)
        customer_display.title = self.id + ' - ' + self.first_name + ' ' + self.last_name
        return customer_display.table

    def account_restrictions(self, video):
        if self.account_type == 'sx' and len(self.current_video_rentals) == 1:
            return False
        elif self.account_type == 'px' and len(self.current_video_rentals) == 3:
            return False
        elif self.account_type == 'sf' and (len(self.current_video_rentals) == 1 or video.rating == 'R' ):
            return False
        elif self.account_type == 'pf' and (len(self.current_video_rentals) == 3 or video.rating == 'R' ):
            return False
        else:
            return True
        
    @classmethod
    def read_customers(cls):
        customers = {}
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/customers.csv")
        with open(path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                customers[row['id']] = (Customer(**dict(row)))
        return customers