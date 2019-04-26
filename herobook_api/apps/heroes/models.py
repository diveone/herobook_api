from django.db import models

from shortuuidfield import ShortUUIDField


class Hero(models.Model):
    uuid = ShortUUIDField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=300)
    alignment = models.CharField(max_length=300)
    gender = models.CharField(max_length=300)
    eye_color = models.CharField(max_length=300)
    race = models.CharField(max_length=300)
    hair_color = models.CharField(max_length=300)
    publisher = models.CharField(max_length=300)
    skin_color = models.CharField(max_length=300)
    height = models.CharField(max_length=300)
    weight = models.CharField(max_length=300)
    intelligence = models.CharField(max_length=300)
    strength = models.CharField(max_length=300)
    speed = models.CharField(max_length=300)
    durability = models.CharField(max_length=300)
    power = models.CharField(max_length=300)
    combat = models.CharField(max_length=300)

    def __repr__(self):
        return f"{self.name} - {self.alignment}"
