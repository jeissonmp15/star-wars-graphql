import graphene

from characters.models import Character
from .types import CharacterType


class CreateCharacterMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        height = graphene.String()
        mass = graphene.String()
        hair_color = graphene.String()
        skin_color = graphene.String()
        eye_color = graphene.String()
        birth_year = graphene.String()
        gender = graphene.String()

    name = graphene.Field(CharacterType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        data = {
            'name': kwargs['name'].strip(), 'height': kwargs.get('height', 'unknown'),
            'mass': kwargs.get('mass', 'unknown'), 'hair_color': kwargs.get('hair_color', 'unknown'),
            'skin_color': kwargs.get('skin_color', 'unknown'), 'eye_color': kwargs.get('eye_color', 'unknown'),
            'birth_year': kwargs.get('birth_year', 'unknown'), 'gender': kwargs.get('gender', 'unknown')
        }

        obj = Character.objects.create(**data)
        return CreateCharacterMutation(name=obj)


class Mutation(graphene.ObjectType):
    create_character = CreateCharacterMutation.Field()
