from django.db import models

# Create your models here.



class SignUp(models.Model):
    name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    email=models.EmailField()
    contact_number=models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)