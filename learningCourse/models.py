from django.db import models

from account.models import User


class Student(models.Model):
    user = models.OneToOneField(User, primary_key=True, related_name='student', on_delete=models.PROTECT)
    bio = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.user.username


class Teacher(models.Model):
    user = models.OneToOneField(User, primary_key=True, related_name='teacher', on_delete=models.PROTECT)
    bio = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return self.user.username


class Course(models.Model):
    course_heading = models.CharField(max_length=50, blank=True)
    course_description = models.CharField(max_length=500, blank=True)
    max_student_capacity = models.IntegerField(default=0, blank=True)
    teacher = models.ForeignKey(Teacher, blank=True, on_delete=models.PROTECT, null=True)
    student = models.ManyToManyField(Student, blank=True, null=True)

    def __str__(self):
        return self.course_heading
