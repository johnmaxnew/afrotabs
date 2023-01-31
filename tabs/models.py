from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager
from tinymce.models import HTMLField
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length = 250, null = True, blank = True)

    class Meta:
        verbose_name_plural='Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse('tab_detail', kwargs={'slug': self.slug})

class Tab(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='img/', default='thumbnail.jpg', blank=True)
    artiste = models.CharField(max_length=255)
    body = HTMLField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    featured = models.BooleanField(default=False)
    categories = models.ManyToManyField('Category', related_name='tabs')
    tags = TaggableManager()
    slug = models.SlugField(max_length = 250, null = True, blank = True)


    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)

        super(Tab, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


    def get_absolute_url(self):
            return reverse('tab_detail', kwargs={'slug': self.slug})
