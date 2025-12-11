from django.db import models

from core.models import TimeStampedModelMixin


class Post(TimeStampedModelMixin):
    user = models.ForeignKey("account.User", on_delete=models.CASCADE)
    content = models.TextField()
