from django.db import models
from accounts.models import User


# Create your models here.
class Subject(models.Model):
    sub_name = models.CharField(max_length=30, unique=True)
    teacher_name = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.sub_name

    


