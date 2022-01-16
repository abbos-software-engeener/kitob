import imp
from django.urls import path
from .views import *

app_name = 'api'

urlpatterns = [
    path('book/',BookingView.as_view()),
    path('book/<int:pk>/',BookingView.as_view()),
    path('booking/',BookingView.as_view()),
    path('booking/<int:pk>/',BookingView.as_view()),
    path('achievements/',AchievementView.as_view()),
    path('achievements/<int:pk>/',AchievementView.as_view()),
    path('about-us/',AboutUsView.as_view()),
    path('about-us/<int:pk>/',AboutUsView.as_view()),
    path('card/',CardView.as_view()),
    path('card/<int:pk>/',CardView.as_view()),
    





]
