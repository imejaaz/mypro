from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User
from django.db.models.query import QuerySet
User=get_user_model()
from django.dispatch import receiver
from django.db.models.signals import post_save

class studentManager(models.Manager):
        def get_queryset(self):
                return super().get_queryset().filter(is_deleted=False)


class receipes(models.Model):
        view_count = models.IntegerField(default=1)
        user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
        name = models.CharField(max_length=20)
        desc = models.TextField(max_length=500)
        img = models.ImageField(upload_to='receipe/')

@receiver(post_save, sender=receipes)
def saved(sender, instance, created, **kwargs):
        if created:
                print('a new receipe has been created successfully')










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
        is_deleted = models.BooleanField(default=False)
        objects = studentManager()
        admin_object = models.Manager()

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


class studentReport(models.Model):
        student = models.ForeignKey(Student, related_name='studentresult', on_delete=models.CASCADE)
        Rank = models.IntegerField()
        date_of_report = models.DateTimeField(
         auto_now_add=True)
        class Meta:
                unique_together = ['student', 'Rank']