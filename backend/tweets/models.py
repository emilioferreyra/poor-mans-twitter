from django.db import models
from django.db.models.fields import CharField


class Post(models.Model):
    """Manage post model"""
    author = models.CharField(max_length=50, unique=False)
    content = models.TextField(max_length=50)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        verbose_name_plural = 'Posts'
        ordering = ['-id']
