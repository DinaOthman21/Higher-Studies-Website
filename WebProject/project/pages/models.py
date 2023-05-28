from enum import unique
from tkinter import CASCADE
from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=50)
    ID=models.IntegerField(primary_key=True)
    date=models.DateTimeField()
    university=models.CharField(max_length=50)
    Gender=models.CharField(max_length=10)
    department=models.CharField(max_length=10)
    statues=models.CharField(max_length=10)
    course1=models.CharField(max_length=50,null=True)
    course2=models.CharField(max_length=50,null=True)
    course3=models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.ID

    



class Courses(models.Model):
    CourseID=models.IntegerField(primary_key=True)
    coursename=models.CharField(max_length=50)
    HallNo=models.CharField(max_length=50)
    Hourses=models.CharField(max_length=50)
    CourseDay=models.CharField(max_length=50)
    Department=models.CharField(max_length=50)
    registercourse=models.ManyToManyField(Student)
   
    def __str__(self):
        return self.coursename

