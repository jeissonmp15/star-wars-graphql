# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from planets.filtersets import PlanetFilterSet
from planets.models import Planet
from planets.serializers import PlanetSerializer


class PlanetViewSet(ModelViewSet):
    model = Planet
    serializer_class = PlanetSerializer
    filterset_class = PlanetFilterSet

    def get_queryset(self):
        return self.model.objects.all()
