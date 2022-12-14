from django_filters import rest_framework as filters
from django_filters.rest_framework import FilterSet

from planets.models import Planet


class PlanetFilterSet(FilterSet):
    name__in = filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Planet
        fields = []
