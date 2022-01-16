import imp
from django.urls import path
from api import urls
from .views import *

app_name  = 'category'

urlpatterns = [
    path('category/',CategoryView.as_view()),
    path('category/<int:pk>/',CategoryView.as_view()),
    path('subcategory',SubCategoryView.as_view()),
    path('subcategory/<int:pk>/',SubCategoryView.as_view()),
    path('contact/',ContactView.as_view()),
]