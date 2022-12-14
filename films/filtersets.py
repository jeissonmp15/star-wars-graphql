from django_filters import rest_framework as filters
from django_filters.rest_framework import FilterSet

from films.models import Film


class FilmFilterSet(FilterSet):
    title__in = filters.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Film
        fields = []
