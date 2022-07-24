import csv
from classes.staff import Staff
from classes.student import Student
import os.path

class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.objects()
        self.students = Student.objects()

    def list_students(self):
        print('\n')
        for i, student in enumerate(self.students):
            print(f'{i + 1}. {student.name} {student.school_id}')

    def find_student_by_id(self, student_id):
        for student in self.students:
            if student.school_id == student_id:
                return student

    def add_student(self, student_data):
        self.students.append(Student(**student_data))
        self.save_students()
        return self.students

    def save_students(self, student_id=None):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/students.csv")
        with open(path, 'w') as csvfile:
            fieldnames = ["name", "age", "password", "role", "school_id"]
            writer = csv.DictWriter(csvfile, fieldnames)
            writer.writeheader()
            for s in self.students:
                if s.school_id != student_id:
                    writer.writerow({'name': s.name, 'age': s.age, 'password': s.password, 'role': s.role, 'school_id': s.school_id})

    def delete_student(self, student_id):
        self.save_students(student_id)
        
