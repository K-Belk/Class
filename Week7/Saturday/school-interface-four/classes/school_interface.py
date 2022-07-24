from classes.school import School

class SchoolInterface:

    def __init__(self, school_name):
        self.school = School(school_name)

    def run(self):
        if self.authenticate_user() == True:
            while True:
                mode = input(self.menu())

                if mode == '1':
                    self.school.list_students()
                elif mode == '2':
                    student_id = input(self.enter_student_id())
                    student_string = str(self.school.find_student_by_id(student_id))
                    print(student_string)
                elif mode == '3':
                    student_data = self.get_student_data()
                    self.school.add_student(student_data)
                elif mode == '4':
                    student_id = input(self.enter_student_id())
                    self.school.delete_student(student_id)
                elif mode == '5':
                    break  
        else:
            return 'Unauthorized user'

    def menu(self):
        return "\nWhat would you like to do?\nOptions:\n1. List All Students\n2. View Individual Student <student_id>\n3. Add a Student\n4. Remove a Student <student_id>\n5. Quit\n"

    def get_student_data(self):
        student_data = {'role':'student'}
        student_data['name']      = input('Enter student name:\n')
        student_data['age']       = input('Enter student age: \n')
        student_data['school_id'] = input('Enter student school id: \n')
        student_data['password']  = input('Enter student password: \n')
        return student_data

    def enter_student_id(self):
        return "Please enter the student's id:\n"

    def authenticate_user(self):
        staff = self.school.staff
        attempts = 0
        print(f"""
Welcome to {self.school.name}
_________________________
        """)
        while attempts < 3:
            id = input('Please enter a valid employee id:\n')
            pw = input('\nPlease enter a valid password:\n')
            for s in staff:
                if s.employee_id == id and s.password == pw:
                    return True
            attempts +=1
            print('Incorrect employee id or password')
        return print('No more attempts left. Bye.')
