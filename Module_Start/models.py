from django.db import models

# Create your models here.

class Page(models.Model):
    note = models.TextField()

    def __str__(self):
        return self.note