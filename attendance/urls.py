from django.urls import path, include
from . import views

urlpatterns = [
    
    path('subjects/', views.subject_list, name='subject_list'),
    path('teacher-home/', views.teacher_home, name='teacher-home'),
    path('student-home/', views.student_home, name='student-home'),

]


