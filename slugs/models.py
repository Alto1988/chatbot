from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Messages(models.Model):
    title = models.CharField(max_length=200)
    message = models.TextField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class Groups(models.Model):
    owner = models.ForeignKey(
        User, related_name='groups_created', on_delete=models.CASCADE)
    group = models.ForeignKey(
        Messages, related_name='messages', on_delete=models.CASCADE)

    title = models.TextField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    group_overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title


class Module(models.Model):
    course = models.ForeignKey(
        Groups, related_name='modules', on_delete=models.CASCADE)

    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
