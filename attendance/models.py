from django.db import models
from accounts.models import User, Teacher, Student
from datetime import date


class Attendance(models.Model):
    date = models.DateField(default=date.today)
    status = models.BooleanField(default=False)
    name = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)

class Subject(models.Model):
    sub_name = models.CharField(max_length=30, unique=True)
    teacher_name = models.ForeignKey(Teacher, related_name='teachers', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.sub_name