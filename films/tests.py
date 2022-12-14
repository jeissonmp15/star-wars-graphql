# Create your tests here.
import json

from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from characters.models import Character
from planets.models import Planet


class EducationTestCase(TestCase):

    def setUp(self):
        # Creamos un usuario y generamos el acceso a la api para hacer pruebas de forma general
        user = get_user_model()(
            email='testing_login@dev.com',
            first_name='Testing',
            last_name='Testing',
            username='testing_login'
        )
        user.set_password('admin123')
        user.save()

        client = APIClient()
        response = client.post(
            '/api/token/', {
                'username': 'testing_login',
                'password': 'admin123',
            },
            format='json'
        )

        result = json.loads(response.content)
        self.access_token = result['access']
        self.user = user

    def test_create_character(self):
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.access_token)

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
            "planets": [
                1,
                2,
            ],
            "characters": [
                1,
                2,
                3,
            ]
        }

        response = client.post(
            '/films/',
            film,
            format='json'
        )

        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('id', result)
        self.assertIn('title', result)
        self.assertIn('episode', result)
        self.assertIn('opening_text', result)
        self.assertIn('director', result)
        self.assertIn('producer', result)
        self.assertIn('release_date', result)
        self.assertIn('characters', result)
        self.assertIn('planets', result)

        if 'id' in result:
            del result['id']

        self.assertEqual(result, film)
