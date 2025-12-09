from django.db import models
from django.contrib.auth.models import User

from core.models import TimeStampedModelMixin


class Post(TimeStampedModelMixin):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
