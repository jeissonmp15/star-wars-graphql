# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from films.filtersets import FilmFilterSet
from films.models import Film
from films.serializers import FilmSerializer


class FilmViewSet(ModelViewSet):
    model = Film
    serializer_class = FilmSerializer
    filterset_class = FilmFilterSet

    def get_queryset(self):
        return self.model.objects.all()
