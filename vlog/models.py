from django.db import models

# Create your models here.

class Contact(models.Model):
    name    = models.CharField(max_length=80)
    email   = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.CharField(max_length=500)



    