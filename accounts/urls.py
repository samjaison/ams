from django.urls import path, include
from accounts.views import classroom, students, teachers

urlpatterns = [
    path('', classroom.SignUpView.as_view(), name = 'signup'),
    path('accounts/signup/student/', students.StudentSignUpView.as_view(), name='student_signup'),
    path('accounts/signup/teacher/', teachers.TeacherSignUpView.as_view(), name='teacher_signup'),
     
]
