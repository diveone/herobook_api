from rest_framework import serializers

from heroes.models import Hero


class HeroSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source="uuid")

    class Meta:
        model = Hero
        fields = '__all__'
        exclude = ('uuid', 'created', 'modified')

