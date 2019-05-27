from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _

from shortuuidfield import ShortUUIDField


class User(AbstractUser):
    uuid = ShortUUIDField()
    name = models.CharField(_('Name of User'), blank=True, max_length=255)
    email = models.EmailField(_('email address'), blank=False, unique=True)
    api_secret = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.username
