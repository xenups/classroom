from django.contrib.auth.models import User
from rest_framework import serializers, exceptions
import django.contrib.auth.password_validation as validators

from account.serializers import UserSerializer
from learningCourse import models
from learningCourse.models import Student, Teacher, Course


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Student
        fields = ('user', 'bio')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        student = Student.objects.create(user=user, bio=validated_data.pop('bio'))
        student.save()
        return student

    def update(self, instance, validated_data):
        print("update call")
        user = validated_data.get('user')
        instance.user.first_name = user.get('first_name')
        instance.user.last_name = user.get('last_name')
        instance.user.set_password(user.get('password'))
        instance.user.email = user.get('email')
        instance.user.save()

        instance.bio = validated_data['bio']
        instance.save()
        return instance


class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Student
        fields = ('user', 'bio')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        teacher = Teacher.objects.create(user=user, bio=validated_data.pop('bio'))
        teacher.save()
        return teacher

    def update(self, instance, validated_data):
        user = validated_data.get('user')
        instance.user.first_name = user.get('first_name')
        instance.user.last_name = user.get('last_name')
        instance.user.set_password(user.get('password'))
        instance.user.email = user.get('email')
        instance.user.save()

        instance.bio = validated_data['bio']
        instance.save()
        return instance


class CourseSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(many=False)
    student = StudentSerializer(many=True)

    class Meta:
        model = Course
        fields = '__all__'

    def create(self, validated_data):
        teacher_data = validated_data.pop('teacher')
        students_data = validated_data.pop('student')

        course = models.Course.objects.create(**validated_data)
        teacher = TeacherSerializer.create(TeacherSerializer(), validated_data=teacher_data)
        course.teacher = teacher

        for student in students_data:
            student, created = models.Student.objects.get_or_create(bio=student['bio'])
            course.student.add(student)
        course.save()
        return course

    def update(self, instance, validated_data):
        teacher_data = validated_data.pop('teacher')
        student_data = validated_data.pop('student')
        instance.course_heading = validated_data['course_heading']
        instance.course_description = validated_data['course_description']
        instance.max_student_capacity = validated_data['max_student_capacity']
        teacher, created = models.Course.objects.get_or_create(bio=teacher_data['bio'])
        instance.publisher = teacher
        students_list = []
        for student in student_data:
            student, created = models.Student.objects.get_or_create(bio=student['bio'])
            students_list.append(student)

        instance.student.set(students_list)
        instance.save()
        return instance
