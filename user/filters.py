from django.db.models import Q
from django_filters import rest_framework as filters
from .models import User


class UserSearchFilter(filters.FilterSet):
    q = filters.CharFilter(method='q_filter')

    class Meta:
        model = User
        fields = ['q']

    def q_filter(self, queryset, name, value):
        return queryset.filter(Q(username__istartswith=value) | Q(first_name__istartswith=value) |
                               Q(last_name__istartswith=value))