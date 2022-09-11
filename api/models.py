from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=100, null=False)
    roll_number = models.IntegerField(null=False, unique=True)
    email = models.EmailField(null=True)
    course_id = models.ForeignKey(
        'Course', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Name: {self.name}, Roll Number: {self.email}' + f'Email: {self.email}' if self.email != None else ""


class Course(models.Model):
    name = models.CharField(max_length=100, null=False)
