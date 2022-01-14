from django.contrib.auth.models import User
from django.db import models
from review.models import Review


class Comment(models.Model):
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    reviewed_by = models.ForeignKey(to=Review, on_delete=models.CASCADE)
