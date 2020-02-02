from django.contrib import admin

# Register your models here.
from learningCourse.models import Course, Student, Teacher

admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Teacher)
