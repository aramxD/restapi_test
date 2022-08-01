from django.db import models

# Create your models here.



class Contact(models.Model):
    full_name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()
    project= models.CharField(max_length=100, default='portfolio-dev')
    timestamp = models.DateTimeField(auto_now_add=True)