from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from learningCourse.models import Student, Teacher, Course
from learningCourse.serializers import TeacherSerializer, StudentSerializer, CourseSerializer


class StudentListView(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class TeacherListView(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherDetailView(generics.ListCreateAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class CourseListView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
