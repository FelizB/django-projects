from django.db import models

# Create your models here.
class patient(models.Model):
    firt_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    age= models.IntegerField()