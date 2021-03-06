from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Topic(models.Model):
    text = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    image = models.ImageField(upload_to='topics', blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Topin(models.Model):
    text = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    image = models.ImageField(upload_to='topins', blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images', blank=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return f"{self.text[:50]}..."


class Entry1(models.Model):
    topin = models.ForeignKey(Topin, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', blank=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return f"{self.text[:50]}..."
