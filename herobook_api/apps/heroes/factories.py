import factory

from heroes.serializers import Hero


class HeroFactory(factory.DjangoModelFactory):
    class Meta:
        model = Hero
