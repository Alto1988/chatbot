from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from .fields import OrderField


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
    messages = models.ForeignKey(
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
    groups = models.ForeignKey(
        Groups, related_name='modules', on_delete=models.CASCADE)

    title = models.CharField(max_length=200)
    order = OrderField(blank=True, for_fields=['groups'])

    def __str__(self):
        return self.title

    ordering = ['order']


class Content(models.Model):
    owner = models.ForeignKey(
        Module, related_name='contents', on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE,
                                     limit_choices_to={'model_int': ('text', 'video', 'image', 'file')})

    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')
    order = OrderField(blank=True, for_fields=['module'])

# Don't like the name of this class need to change it


class ItemBase(models.Model):
    owner = models.ForeignKey(
        User, related_name='%(class)s_related', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Text(ItemBase):
    content = models.TextField()


class Video(ItemBase):
    url = models.URLField()


class Image(ItemBase):
    file = models.FileField(upload_to='images')


class File(ItemBase):
    file = models.FileField(upload_to='files')
