from django.db import models

# Create your models here.
class Post(models.Model):
    name = models.TextField(max_length=20)
    data = models.TextField(max_length=350) 
    
                                      