from django.urls import path
from account import views
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    # path('register/', views.RegisterUserView.as_view()),
    path('validation/', views.PhoneValidationView.as_view()),
    path('otplogin/', views.LoginView.as_view()),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

]
