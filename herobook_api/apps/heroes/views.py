import logging

from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from heroes.serializers import Hero, HeroSerializer

logger = logging.getLogger('heroes.views')


# pylint: disable=missing-docstring
class HeroDetailAPIView(generics.RetrieveAPIView):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


# pylint: disable=missing-docstring
class HeroListAPIView(generics.ListAPIView):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
