import email
from django.db import models






# Create your models here.
class Staff(models.Model):
    name = models.CharField(max_length=100)
    departement = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    user_photo = models.ImageField(upload_to='media/cursos')    
    timestamp = models.DateTimeField(auto_now_add=True)
    

class Carrers(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)


class Postulation(models.Model):
    full_name=models.CharField(max_length=100)
    email=models.EmailField()
    linkedin_url=models.URLField()
    portfolio_url=models.URLField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)