import logging

from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.authentication import TokenAuthentication
from heroes.serializers import Hero, HeroSerializer

logger = logging.getLogger('heroes.views')


# pylint: disable=missing-docstring
class HeroDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
    lookup_field = 'uuid'


# pylint: disable=missing-docstring
class HeroListAPIView(generics.ListCreateAPIView):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticatedOrReadOnly,)
