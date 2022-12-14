# Create your views here.
from django.db.models import Prefetch
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from characters.filtersets import CharacterFilterSet
from characters.models import Character
from characters.serializers import CharacterSerializer
from films.models import Film


class CharacterViewSet(ModelViewSet):
    model = Character
    serializer_class = CharacterSerializer
    filterset_class = CharacterFilterSet

    def get_queryset(self):
        return self.model.objects.prefetch_related(
            Prefetch('film_character_set', queryset=Film.objects.only('id', 'title'))
        )
