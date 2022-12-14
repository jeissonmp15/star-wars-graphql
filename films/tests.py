# Create your tests here.

import graphene
from django.test.testcases import TestCase

from characters.models import Character
from films.models import Film
from graphene_schema.schema import Query, Mutation
from planets.models import Planet


class CharacterTestCase(TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.query = '''
            query {
                allFilms {
                    title
                    episode
                    openingText
                    planets{
                        name
                    }
                    characters {
                        edges {
                            node {
                              name
                            }
                        }
                    }
              }
            }
            '''

    def test_get_character(self):
        schema = graphene.Schema(query=Query)
        characters = [
            {
                "name": "Felipe Manrique",
                "height": "170",
                "mass": "65",
                "hair_color": "black",
                "skin_color": "fair",
                "eye_color": "blue",
                "birth_year": "19BBY",
                "gender": "male"
            },
            {
                "name": "Felipe Manrique 2",
                "height": "170",
                "mass": "65",
                "hair_color": "black",
                "skin_color": "fair",
                "eye_color": "blue",
                "birth_year": "19BBY",
                "gender": "male"
            },
            {
                "name": "Felipe Manrique 3",
                "height": "170",
                "mass": "65",
                "hair_color": "black",
                "skin_color": "fair",
                "eye_color": "blue",
                "birth_year": "19BBY",
                "gender": "male"
            }
        ]

        Character.objects.bulk_create([Character(**character) for character in characters])

        planets = [
            {
                "name": "Tierra",
                "diameter": "10465",
                "climate": "arid",
                "gravity": "1 standard",
                "terrain": "desert",
                "population": "200000"
            },
            {
                "name": "Marte",
                "diameter": "10465",
                "climate": "arid",
                "gravity": "1 standard",
                "terrain": "desert",
                "population": "200000"
            }
        ]

        Planet.objects.bulk_create([Planet(**planet) for planet in planets])

        film = {
            "title": "Prueba",
            "episode": "8",
            "opening_text": "It is a period of civil war.\r\nRebel spaceships, striking\r\nfrom a hidden base, have won\r\ntheir first victory against\r\nthe evil Galactic Empire.\r\n\r\nDuring the battle, Rebel\r\nspies managed to steal secret\r\nplans to the Empire's\r\nultimate weapon, the DEATH\r\nSTAR, an armored space\r\nstation with enough power\r\nto destroy an entire planet.\r\n\r\nPursued by the Empire's\r\nsinister agents, Princess\r\nLeia races home aboard her\r\nstarship, custodian of the\r\nstolen plans that can save her\r\npeople and restore\r\nfreedom to the galaxy....",
            "director": "George Lucas",
            "producer": "Gary Kurtz, Rick McCallum",
            "release_date": "2022-11-14",
        }

        film_intance = Film.objects.create(**film)
        film_intance.planets.add(*[1, 2])
        film_intance.characters.add(*[1, 2, 3])

        result = schema.execute(self.query)
        self.assertIsNone(result.errors)
        print(result.data)
