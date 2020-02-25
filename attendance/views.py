from django.shortcuts import render, redirect
from .models import Subject
from ams.decorators import student_required, teacher_required
from django.contrib.auth.decorators import login_required

# Create your views here.

def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'attendance/subject_list.html', {'subjects': subjects})

def home(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:
            return render(request, 'attendance/teacher-home.html')
        else:
            return render(request, 'attendance/student-home.html')
    return render(request, 'registration/home.html')

# @login_required
# @teacher_required
def teacher_home(request):
    return render(request, 'attendance/teacher-home.html')

# @login_required
# @student_required
def student_home(request):
    return render(request, 'attendance/student-home.html')