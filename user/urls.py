from django.urls import path
from .views import *

app_name = "user"

urlpatterns = [
    path('registration/',RegistrationView.as_view()),
    path("me/", MeView.as_view(), name="me"),
    path('login/', UserLogin.as_view(), name="login"),
    path('profile/', ProfileView.as_view(), name="profile"),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('search/', SearchUserView.as_view(), name="search")
]