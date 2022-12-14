from rest_framework.serializers import ModelSerializer

from planets.models import Planet


class PlanetSerializer(ModelSerializer):
    class Meta:
        model = Planet
        fields = '__all__'
