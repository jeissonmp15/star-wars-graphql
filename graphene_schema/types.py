import graphene
from django.db.models import Prefetch
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType

from characters.models import Character
from films.models import Film
from planets.models import Planet


class CharacterType(DjangoObjectType):
    class Meta:
        model = Character
        filter_fields = {'name': ['icontains']}
        interfaces = (relay.Node,)


class FilmType(DjangoObjectType):
    class Meta:
        model = Film


class PlanetType(DjangoObjectType):
    class Meta:
        model = Planet


class Query(object):
    # all_characters = graphene.List(CharacterType, name=graphene.String(required=False))
    all_characters = DjangoFilterConnectionField(CharacterType)
    all_films = graphene.List(FilmType)
    all_planets = graphene.List(PlanetType)

    # def resolve_all_characters(self, info, name=None, **kwargs):
    #     qs = Character.objects.prefetch_related(
    #         Prefetch('film_character_set', queryset=Film.objects.only('id', 'title'))
    #     )
    #     if name:
    #         qs = qs.filter(name__icontains=name)
    #     return qs

    def resolve_all_characters(self, info, **kwargs):
        return Character.objects.prefetch_related(
            Prefetch('film_character_set', queryset=Film.objects.only('id', 'title'))
        )

    def resolve_all_films(self, info, **kwargs):
        return Film.objects.prefetch_related('planets', 'characters')

    def resolve_all_planets(self, info, **kwargs):
        return Planet.objects.all()
