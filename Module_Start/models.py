from django.db import models

# Create your models here.

class Page(models.Model):
    title = models.TextField(default='Sin Texto')
    us_jpg1 = models.ImageField(default='us_jpg1.png')
    us_jpg2 = models.ImageField(default='us_jpg2.png')
    us = models.TextField(default='Sin Texto')
    note = models.TextField(default='Sin Texto')
    service_one = models.TextField(default='Sin Texto')
    service_two = models.TextField(default='Sin Texto')

    def __str__(self):
        return self.note