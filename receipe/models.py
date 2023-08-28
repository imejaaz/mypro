

from django.db import models
from django.contrib.auth.models import User


class receipes(models.Model):
        view_count = models.IntegerField(default=1)
        user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
        name = models.CharField(max_length=20)
        desc = models.TextField(max_length=500)
        img = models.ImageField(upload_to='receipe/')

        def __str__(self):
                return self.name





class StudentReg(models.Model):
        sReg = models.CharField(max_length=20)

        def __str__(self):
                return self.sReg


class Department(models.Model):
        department = models.CharField(max_length=30)

        def __str__(self):
                return self.department


class Student(models.Model):
        department = models.ForeignKey(Department, related_name='students', on_delete=models.CASCADE)
        studentId = models.OneToOneField(StudentReg, related_name='student', on_delete=models.CASCADE)
        studentName = models.CharField(max_length=50)
        studentAge = models.IntegerField(default=18)
        studentEmail = models.EmailField(unique=True)
        studentAddress = models.TextField()

        def __str__(self):
                return self.studentName

        class Meta:
                ordering = ['studentName']
                verbose_name = "student"



class Subject(models.Model):
        subject = models.CharField(max_length=20)
        def __str__(self):
                return self.subject

class Marks(models.Model):
        student = models.ForeignKey(Student, on_delete=models.CASCADE)
        subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
        marks = models.IntegerField(blank=None)
        def __str__(self):
                return f'Student: {self.student.studentName} got {self.marks} marks in: {self.subject.subject}got:marks.'

        class Meta:
                unique_together = ['student','subject']