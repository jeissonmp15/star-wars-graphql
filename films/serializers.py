from rest_framework.serializers import ModelSerializer

from films.models import Film


class FilmSerializer(ModelSerializer):
    class Meta:
        model = Film
        fields = '__all__'


class ListFilmsSerializer(ModelSerializer):
    class Meta:
        model = Film
        fields = ['id', 'title']
