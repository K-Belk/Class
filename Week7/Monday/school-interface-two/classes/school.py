from classes.staff import Staff
from classes.student import Student

class School:
    def __init__(self, name):
        self.name = name
        self.staff = Staff.objects()
        self.students = Student.objects()

    def list_students(self):
        
        for i, s in enumerate(self.students):
            print(f'{i+1}. {s.name} {s.school_id}')

    def find_student(self, student_id):
        for s in self.students:
            if s.school_id == student_id:
                return s