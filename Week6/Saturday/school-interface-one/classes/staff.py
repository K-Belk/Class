from classes.person import Person
import os
import csv

class Staff(Person):

    def __init__(self, name, age, role,  password, employee_id,):
        super().__init__(name, age, role, password)
        self.employee_id = employee_id

    def all_staff():
        results = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/staff.csv")
    
        with open(path) as csvfile:
            students = csv.DictReader(csvfile)
            for row in students:
                results.append(Staff(**row))
        return results

