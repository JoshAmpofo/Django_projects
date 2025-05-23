from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=250, blank=True)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    
    def __str__(self):
        return self.title