from django_filters import rest_framework as filters
from django_filters.rest_framework import FilterSet

from characters.models import Character


class CharacterFilterSet(FilterSet):
    name__in = filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Character
        fields = []
