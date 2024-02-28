from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100, default='Томск',)
    address = models.CharField(max_length=250, default='Вершинина, 39а',)

    def __str__(self):
        return self.user.username
