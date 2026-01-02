from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    follows = models.ManyToManyField("self")
    followers = models.ManyToManyField("self")

    def follow(self, user):
        user.followers.add(self)
        self.follows.add(user)

    def unfollow(self, user):
        user.followers.remove(self)
        self.follows.remove(user)
