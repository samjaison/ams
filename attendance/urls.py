from django.urls import path, include
from . import views

urlpatterns = [
    
    path('teacher-home/', views.teacher_home, name='teacher-home'),
    path('student-home/', views.student_home, name='student-home'),
    path('student-home/subjects/', views.subject_list, name='subject_list'),


]


