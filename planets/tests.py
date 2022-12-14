# Create your tests here.

import graphene
from django.test.testcases import TestCase

from graphene_schema.schema import Query, Mutation
from planets.models import Planet


class CharacterTestCase(TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.query = '''
            query{
                allPlanets {
                    name
                    diameter
                    climate
                    gravity
                    terrain
                    population 
                }
            }
            '''

    def test_get_character(self):
        schema = graphene.Schema(query=Query)

        planet = {
            "name": "Tierra",
            "diameter": "10465",
            "climate": "arid",
            "gravity": "1 standard",
            "terrain": "desert",
            "population": "200000"
        }

        Planet.objects.create(**planet)

        result = schema.execute(self.query)
        self.assertIsNone(result.errors)
        print(result.data)