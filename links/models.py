from django.db import models

# Create your models here.
class Python(models.Model):
    title = models.CharField(max_length=50)
    beskriv = models.TextField()
    link_app = models.CharField(max_length=50)
    link = models.URLField(blank=True)
    login = models.CharField(max_length=50, blank=True)
    objects = models.Manager()

    def __str__(self):
      return self.title

class Django(models.Model):
    title = models.CharField(max_length=50)
    beskriv = models.TextField()
    link_app = models.CharField(max_length=50)
    link = models.URLField(blank=True)
    login = models.CharField(max_length=50, blank=True)

    def __str__(self):
      return self.title
    
class Link(models.Model):
    name=models.CharField(max_length=50)
    link=models.URLField()

class Small(models.Model):
   name=models.TextField()
   foto=models.ImageField(upload_to='staticfiles/images/', blank=True)

class Apps(models.Model):
   app=models.CharField(max_length=250)
   kort=models.TextField()
   fordel=models.TextField()
   ulemp=models.TextField()