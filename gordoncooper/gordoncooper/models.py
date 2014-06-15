from django.db import models
import datetime


TYPE_CHOICES = (
    ('diary', 'Diary'),
    ('gallery', 'Gallery')
)

class Image(models.Model):
    image = models.ImageField(upload_to='%Y/%m')

    def __unicode__(self):
        return self.image.url

class Post(models.Model):
    publish = models.DateTimeField('publish', default=datetime.datetime.now)
    type = models.CharField('type', max_length=12, choices=TYPE_CHOICES)
    title = models.CharField('title', max_length=200)
    slug = models.SlugField('slug', unique_for_date='publish')
    body = models.TextField('body')
    images = models.ManyToManyField(Image, blank=True)
    active = models.BooleanField('active', default=False)

    def __unicode__(self):
        return self.title
