from django.db import models

from shortuuidfield import ShortUUIDField


class Hero(models.Model):
    PLACEHOLDER_IMAGE = 'https://via.placeholder.com/380x280.png?text=Hero'

    uuid = ShortUUIDField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    image = models.URLField(null=True, default=PLACEHOLDER_IMAGE)
    name = models.CharField(max_length=300)
    alignment = models.CharField(max_length=300)
    gender = models.CharField(max_length=300)
    power = models.CharField(max_length=300)
    eye_color = models.CharField(max_length=300, null=True)
    race = models.CharField(max_length=300, null=True)
    hair_color = models.CharField(max_length=300, null=True)
    publisher = models.CharField(max_length=300, null=True)
    skin_color = models.CharField(max_length=300, null=True)
    height = models.CharField(max_length=300, null=True)
    weight = models.CharField(max_length=300, null=True)
    intelligence = models.CharField(max_length=300, null=True)
    strength = models.CharField(max_length=300, null=True)
    speed = models.CharField(max_length=300, null=True)
    durability = models.CharField(max_length=300, null=True)
    combat = models.CharField(max_length=300, null=True)

    def __repr__(self):
        return f"{self.name} - {self.alignment}"
