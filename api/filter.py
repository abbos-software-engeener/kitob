from logging import Filter
from operator import mod
from django_filters import FilterSet
from .models import *
from django_filters import FilterSet, NumberFilter, CharFilter, DateTimeFilter, BooleanFilter, ModelMultipleChoiceFilter, ModelChoiceFilter,  ChoiceFilter
from django.db.models import fields


class BookFilter(FilterSet):
    min_price = NumberFilter(field_name='min_price',lookup_expr='lte')
    max_price = NumberFilter(field_name='max_price',lookup_expr='gte')
    category = CharFilter(field_name='category', lookup_expr='icontains')
    class Meta:
        model = Book
        fields = ['title','author','min_price','max_price']

class BookingFilter(FilterSet):
    class Meta:
        model = Booking
        fields = ['book']


class AchievementFilter(FilterSet):
    class Meta:
        model = Achievement
        fields  = ['title']



class AboutUsFilter(FilterSet):
    class Meta:
        model = AboutUs
        fields  =['title', 'phone', 'address']