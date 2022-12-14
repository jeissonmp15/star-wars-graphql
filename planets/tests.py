# Create your tests here.
import json

from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


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

        planet = {
            "name": "Tierra",
            "diameter": "10465",
            "climate": "arid",
            "gravity": "1 standard",
            "terrain": "desert",
            "population": "200000"
        }

        response = client.post(
            '/planets/',
            planet,
            format='json'
        )

        result = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('id', result)
        self.assertIn('name', result)
        self.assertIn('diameter', result)
        self.assertIn('climate', result)
        self.assertIn('gravity', result)
        self.assertIn('terrain', result)
        self.assertIn('population', result)

        if 'id' in result:
            del result['id']

        self.assertEqual(result, planet)
