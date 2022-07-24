import json
from django.http import JsonResponse
from . models import Students, Courses
from .serializer import StudentSerializer, CourseSerializer
from .forms import StudentForm, CoursesForm
from django.views.decorators.csrf import csrf_exempt

# student 
def all_students(request):
    every_students = Students.objects.all()
    serialzed_students = StudentSerializer(every_students).all_students()
    return JsonResponse(data=serialzed_students, status=200)

def student_detail(request, student_id):
    student = Students.objects.get(id=student_id)
    serialized_student = StudentSerializer(student).student_details()
    return JsonResponse(data=serialized_student, status=200)

@csrf_exempt
def create_student(request):
    if request.method == 'POST':
        data = json.load(request)
        form = StudentForm(data)
        if form.is_valid():
            student = form.save(commit=True)
            serialized_student = StudentSerializer(student).student_details()
            return JsonResponse(data=serialized_student, status=200)

@csrf_exempt
def edit_student(request, student_id):
    student = Students.objects.get(id=student_id)
    if request.method == 'POST':
        data = json.load(request)
        form = StudentForm(data, instance=student)
        if form.is_valid():
            student = form.save(commit=True)
            serialized_student = StudentSerializer(student).student_details()
            return JsonResponse(data=serialized_student, status=200)

@csrf_exempt
def delete_student(request, student_id):
    if request.method == 'POST':
        student = Students.objects.get(id=student_id)
        student.delete()
    return JsonResponse(data={'status': 'Successfully Deleted Student'}, status=200)

# course 
def all_courses(request):
    every_courses = Courses.objects.all()
    serialzed_courses = CourseSerializer(every_courses).all_courses()
    return JsonResponse(data=serialzed_courses, status=200)

def course_detail(request, course_id):
    course = Courses.objects.get(id=course_id)
    serialized_course = CourseSerializer(course).course_details()
    return JsonResponse(data=serialized_course, status=200)

@csrf_exempt
def create_course(request):
    if request.method == 'POST':
        data = json.load(request)
        form = CoursesForm(data)
        if form.is_valid():
            course = form.save(commit=True)
            serialized_course = CourseSerializer(course).course_details()
            return JsonResponse(data=serialized_course, status=200)

@csrf_exempt
def edit_course(request, course_id):
    course = Courses.objects.get(id=course_id)
    if request.method == 'POST':
        data = json.load(request)
        form = CoursesForm(data, instance=course)
        if form.is_valid():
            course = form.save(commit=True)
            serialized_course = CourseSerializer(course).course_details()
            return JsonResponse(data=serialized_course, status=200)

@csrf_exempt
def delete_course(request, course_id):
    if request.method == 'POST':
        course = Courses.objects.get(id=course_id)
        course.delete()
    return JsonResponse(data={'status': 'Successfully Deleted course'}, status=200)

