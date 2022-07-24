from terminaltables import AsciiTable
import os.path
import csv
from classes.video import Video
from classes.customer import Customer

class Inventory:

    def __init__(self) -> None:
        self.customers = Customer.read_customers()
        self.videos = Video.read_inventory()
        self.rented_to = Inventory.read_rented()

    def display_inventory(self):
        display = []
        header = ['id','title','rating','release_year','copies_available']
        display.append(header)
        for v in self.videos:
            video = self.videos[v]
            display.append([video.id, video.title, video.rating, video.release_year, video.copies_available])
        inventory_display = AsciiTable(display)
        return inventory_display.table

    def display_customers(self):
        display = []
        header = ['id','account_type','first_name','last_name']
        display.append(header)
        for c in self.customers:
            customer = self.customers[c]
            display.append([customer.id,customer.account_type,customer.first_name,customer.last_name])
        customer_display = AsciiTable(display)
        return customer_display.table

    def save_customers(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/customers.csv")
        with open(path, 'w') as csvfile:
            customer_csv = csv.writer(csvfile, delimiter=',')
            customer_csv.writerow(['id','account_type','first_name','last_name','current_video_rentals'])
            for c in self.customers:
                customer = self.customers[c]
                joined_rentals = '/'.join(customer.current_video_rentals)
                customer_csv.writerow([customer.id, customer.account_type, customer.first_name, customer.last_name, joined_rentals])
        return 'Saved'

    def next_customer_id(self):
        id_numbers = list(self.customers.keys())
        id_numbers.sort()
        return int(id_numbers[-1]) + 1

    def add_customer(self):
        new_customer = {}
        new_customer['id'] = str(self.next_customer_id())
        while True:
            new_customer['account_type'] = input("Please enter the account type\n sx = standard\n px = premium\n sf = standard family\n pf = premium family\n")
            if new_customer['account_type'] in ['sx','px','sf', 'pf']:
                break
        new_customer['first_name'] = input("Please enter customers first name\n")
        new_customer['last_name'] = input("Please enter customers last name\n")
        new_customer['current_video_rentals'] = ''
        self.customers[new_customer['id']] = Customer(**new_customer)
        self.save_customers()
        return self.customers

    def save_inventory(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/inventory.csv")
        with open(path, 'w') as csvfile:
            inventory_csv = csv.writer(csvfile, delimiter=',')
            inventory_csv.writerow(['id','title','rating','release_year','copies_available'])
            for v in self.videos:
                rental = self.videos[v]
                inventory_csv.writerow([rental.id,rental.title,rental.rating,rental.release_year,rental.copies_available])
        return 'Saved'
    
    @classmethod
    def read_rented(cls):
        rented = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/rented.csv")
        with open(path) as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                rented.append(row)
        return rented

    def save_rented(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/rented.csv")
        with open(path, 'w') as csvfile:
            rented_csv = csv.writer(csvfile, delimiter=',')
            for r in self.rented_to:
                rented_csv.writerow(r)
        return 'saved'
    
    def save_all(self):
        self.save_customers()
        self.save_inventory()
        self.save_rented()
        return 'saved all'

    def rent_video(self, video_id, customer_id):
        video = self.videos[video_id]
        customer = self.customers[customer_id]
        video.copies_available -= 1
        customer.current_video_rentals.append(video.title)
        self.rented_to.append([video.title, customer_id])
        self.save_all()
        return 'rented'

    def find_video_by_title(self, video_title):
        for v in self.videos:
            if self.videos[v].title == video_title:
                return v
        return 'Not found'

    def return_video(self, customer_id, video_index):
        customer = self.customers[customer_id]
        video_title = customer.current_video_rentals.pop(int(video_index))
        self.videos[self.find_video_by_title(video_title)].copies_available += 1
        self.rented_to = [r for r in self.rented_to if r != [video_title, customer_id]]
        self.save_all()
        return 'returned'