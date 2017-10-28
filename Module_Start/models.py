from django.db import models

# Create your models here.

class Page(models.Model):
    title = models.TextField(default='Sin Texto')
    us_img1 = models.ImageField(default='us_img1.png')
    us_img2 = models.ImageField(default='us_img2.png')
    us = models.TextField(default='Sin Texto')
    note = models.TextField(default='Sin Texto')
    service_img = models.ImageField(default='services.png')
    service_one = models.TextField(default='Sin Texto')
    service_two = models.TextField(default='Sin Texto')
    reference_one = models.TextField(default='Sin Texto')
    reference_two = models.TextField(default='Sin Texto')
    reference_tree = models.TextField(default='Sin Texto')
    phone_one = models.IntegerField(default=0)
    phone_two = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=100, null=False)
    rut = models.CharField(max_length=10, null=False)
    email = models.EmailField(null=False)
    city = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=100, null=False)
    gender = models.CharField(max_length=100, null=False)
    prevision = models.CharField(max_length=100, null=False)
    message = models.TextField(null=False)

    def __str__(self):
        return self.name+ ' ' + self.rut