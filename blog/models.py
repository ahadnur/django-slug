from django.db import models
from django.db.models.signals import pre_save
from django_slug_field.utils import unique_slug_generator

class Post(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, null=True, blank=True)
    text = models.TextField()

    def __str__(self):
        return self.title
    
    def body_preview(self):
        return self.text[:250]


def slug_generator(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator, sender=Post)
