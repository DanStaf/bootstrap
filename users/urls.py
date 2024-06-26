from django.urls import path
from users.apps import UsersConfig
from users.views import RegisterView, UserProfileView, UserResetPasswordView, email_verification
from django.contrib.auth.views import LoginView, LogoutView

app_name = UsersConfig.name

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('email_confirm/<str:token>/', email_verification, name='email_confirm'),

    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password_reset/', UserResetPasswordView.as_view(), name='password_reset'),
]
