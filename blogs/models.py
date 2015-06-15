from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField
from django.conf import settings
# Create your models here.

class Blog(models.Model):

    user = models.ForeignKey(User)
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField()
    date = models.DateTimeField(default=datetime.now, blank=True)
    # files = models.ForeignKey(Image)
    # files = models.FileField(upload_to="images")
    # files = models.ImageField("Image", upload_to="images/") 
    category = models.ForeignKey('blogs.AddCategory')
    tag = models.CharField(max_length=100, unique=True)


    def __unicode__(self):
        return self.title



class AddCategory(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __unicode__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(upload_to="images")
    blog = models.ForeignKey(Blog)

    def __unicode__(self):
        return self.image.name

