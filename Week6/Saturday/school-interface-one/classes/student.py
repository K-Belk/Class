from classes.person import Person
import csv
import os

class Student(Person):

    def __init__(self, name, age, role, password, school_id):
        super().__init__(name, age, role, password)
        self.school_id = school_id

    def all_students():
        results = []
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/students.csv")
    
        with open(path) as csvfile:
            students = csv.DictReader(csvfile)
            for row in students:
                results.append(Student(**row))
        return results