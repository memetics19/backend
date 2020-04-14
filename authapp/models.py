from django.db import models
from django.db.models import Model


class User(Model):
    email = models.EmailField(max_length=100)
    username = models.CharField(max_length=100)
