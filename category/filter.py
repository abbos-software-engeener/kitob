from django_filters import FilterSet
from .models import *

class CategoryFilter(FilterSet):
    class Meta:
        model = Category
        fields  = ['title']


class SubCategoryFilter(FilterSet):
    class Meta:
        model = SubCategory
        fields  = ['title']
