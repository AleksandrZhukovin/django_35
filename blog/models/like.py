from django.db import models

from core.models import TimeStampedModelMixin
from django.core.mail import send_mail
from django_lifecycle import hook, AFTER_CREATE, LifecycleModelMixin


class Like(LifecycleModelMixin, TimeStampedModelMixin):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, null=True, related_name='likes')
    comment = models.ForeignKey('blog.Comment', on_delete=models.CASCADE, null=True, related_name='likes')
    user = models.ForeignKey('account.User', on_delete=models.SET_NULL, null=True, related_name='likes')

    class Meta:
        constraints = [  # обмеження
            models.CheckConstraint(
                check=(
                        models.Q(post__isnull=True, comment__isnull=False) |
                        models.Q(post__isnull=False, comment__isnull=True)
                ),
                name='post_or_comment_is_set'
            ),
        ]

    @hook(AFTER_CREATE)
    def notify_user(self):
        if self.post:
            send_mail('Subject', 'Text', from_email="your_email@gmail.com", recipient_list=[self.post.user.email])
        elif self.comment:
            send_mail('Subject', 'Text', from_email="your_email@gmail.com", recipient_list=[self.comment.user.email])

# SMTP - Simple Mail Transfer Protocol
