from django.db import models

# Create your models here.
class Post(models.Model):
    username = models.CharField(max_length=30)
    content = models.CharField(max_length=255)
    date = models.DateField(auto_now=True)