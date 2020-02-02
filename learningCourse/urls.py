from learningCourse import views
from django.urls import path, include

urlpatterns = [

    path('students/', (views.StudentListView.as_view())),
    path('students/<int:pk>/', views.StudentDetailView.as_view()),

    path('teachers/', (views.TeacherListView.as_view())),
    path('teachers/<int:pk>/', views.TeacherDetailView.as_view()),

    path('courses/', (views.CourseListView.as_view())),
    path('courses/<int:pk>/', views.CourseDetailView.as_view()),
]
