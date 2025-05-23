from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Enzyme(models.Model):
    name = models.CharField(max_length=200)
    curator = models.ForeignKey(User, on_delete=models.CASCADE)
    ec_number = models.CharField(max_length=200, unique=True)
    temperature = models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name