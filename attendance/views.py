from django.shortcuts import render, redirect
from .models import Subject, Attendance
from ams.decorators import student_required, teacher_required
from django.contrib.auth.decorators import login_required
from accounts.models import Student, User, Teacher

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:
            return redirect( 'teacher-home')
        else:
            return redirect('student-home')
    return render(request, 'registration/home.html')

@login_required
@teacher_required
def teacher_home(request):
    subjects = Subject.objects.all().values_list('sub_name', flat=True)
    student = Student.attendance_set.all()
    students = Student.objects.all()
    print(student)
    if request.method == 'POST':
        print(request.POST)
        status = request.POST.get('status')
        Attendance.objects.create(status=status)
        return redirect('teacher-home')
    return render(request, 'attendance/teacher-home.html', {'students':students,'subjects':subjects})

@login_required
@student_required
def student_home(request):

    return render(request, 'attendance/student-home.html')

@login_required
@student_required
def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'attendance/subject_list.html', {'subjects': subjects})