from rest_framework import serializers

from heroes.models import Hero


class HeroSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source="hero.uuid")

    class Meta:
        model = Hero
        fields = '__all__'

