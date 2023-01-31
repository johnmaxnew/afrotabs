from django.db import models
from tinymce.models import HTMLField

from django.utils.text import slugify
from django.urls import reverse


class Home(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    body = HTMLField()
    technology = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length = 250, null = True, blank = True)
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)

        super(Home, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


    
class Cookie(models.Model):
    title = models.CharField(max_length=300)
    body = HTMLField()

    def __str__(self):
        return self.title
   
class About(models.Model):
    title = models.CharField(max_length=300)
    body = HTMLField()

    def __str__(self):
        return self.title

class Contact(models.Model):
    title = models.CharField(max_length=300)
    body = HTMLField()

    def __str__(self):
        return self.title

class Privacy(models.Model):
    title = models.CharField(max_length=300)
    body = HTMLField()

    def __str__(self):
        return self.title
    
class Terms(models.Model):
    title = models.CharField(max_length=300)
    body = HTMLField()

    def __str__(self):
        return self.title
  
