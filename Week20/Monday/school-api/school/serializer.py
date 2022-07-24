from builtins import object

class StudentSerializer(object):
    def __init__(self, body) -> None:
        self.body = body

    def all_students(self):
        every_student = { 'students' : []}
        for student in self.body:
            student_details = {
                'id' : student.id,
                'first name' : student.first_name,
                'last name' : student.last_name,
            }
            every_student['students'].append(student_details)
        return every_student

    def student_details(self):
        student_details = {
            'id' : self.body.id,
            'first name' : self.body.first_name,
            'last name' : self.body.last_name,
        }
        return student_details

class CourseSerializer(object):
    def __init__(self, body) -> None:
        self.body = body

    def get_course_students(self, course_students):
        output = []
        for student in course_students:
            output.append(student.first_name + ' ' + student.last_name)
        return output

    def all_courses(self):
        every_course = { 'courses' : []}
        for course in self.body:
            course_details = {
                'id' : course.id,
                'course name' : course.course_name,
                'enrolled students' : self.get_course_students(course.enrolled_students.all())
            }
            every_course['courses'].append(course_details)
        return every_course
    
    def course_details(self):
        course_details = {
            'id' : self.body.id,
            'course name' : self.body.course_name,
            'enrolled students' : self.get_course_students(self.body.enrolled_students.all())
        }
        return course_details