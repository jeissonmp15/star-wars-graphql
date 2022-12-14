# Create your tests here.

import graphene
from django.test.testcases import TestCase

from characters.models import Character
from graphene_schema.schema import Query, Mutation


class CharacterTestCase(TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.query = '''
            query{
              allCharacters {
                edges {
                  node {
                    id
                    name
                    height
                    birthYear
                  }
                }
              }
            }
            '''

        self.mutation = '''
            mutation {
                createCharacter(
                    name:"Felipe Manrique", height: "170", mass: "65", hairColor: "black", skinColor: "fair", 
                    eyeColor: "blue", birthYear: "19BBY", gender: "male"
                ){
                    name{
                        name
                }
              }
            }
        '''

    def test_get_character(self):
        schema = graphene.Schema(query=Query)

        character = {
            "name": "Felipe Manrique",
            "height": "170",
            "mass": "65",
            "hair_color": "black",
            "skin_color": "fair",
            "eye_color": "blue",
            "birth_year": "19BBY",
            "gender": "male"
        }

        Character.objects.create(**character)
        result = schema.execute(self.query)
        self.assertIsNone(result.errors)
        print(result.data)

    def test_create_character(self):
        schema = graphene.Schema(query=Query, mutation=Mutation)
        result = schema.execute(self.mutation)
        self.assertIsNone(result.errors)
        self.assertIn('name', result.data.get('createCharacter', {}))
        print(result.data)
