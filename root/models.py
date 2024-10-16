from django.db import models

# Create your models here.
class User(models.Model):
    id = models.BigIntegerField(primary_key=True)
    key = models.CharField(max_length=18)
    email = models.CharField(max_length=100)
    #username = models.CharField(max_length=50)
    #dob = models.DateField()
    joined_at = models.DateField()
    password = models.CharField(max_length=48)