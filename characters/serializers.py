from rest_framework.serializers import ModelSerializer

from characters.models import Character
from films.serializers import ListFilmsSerializer


class CharacterSerializer(ModelSerializer):
    films_list = ListFilmsSerializer(many=True, source='film_character_set', read_only=True)

    class Meta:
        model = Character
        fields = '__all__'

