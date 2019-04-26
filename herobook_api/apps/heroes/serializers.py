from rest_framework import serializers

from heroes.models import Hero


class HeroSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source="uuid", required=False)

    class Meta:
        model = Hero
        exclude = ('uuid', 'created', 'modified')

