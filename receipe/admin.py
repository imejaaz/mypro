from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(receipes)
admin.site.register(Department)
admin.site.register(Student)
admin.site.register(StudentReg)
admin.site.register(Subject)
admin.site.register(studentReport)


class MarksAd(admin.ModelAdmin):
    list_display = ['student', 'subject', 'marks']

admin.site.register(Marks, MarksAd)
