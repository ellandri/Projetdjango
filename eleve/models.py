from django.db import models

# Create your models here.
class Eleve(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    
class Personne(models.Model):
    first_name = models.CharField(max_length=30)
    second_name = models.CharField(max_length=30)
    third_name = models.CharField(max_length=30)

    last_name = models.CharField(max_length=30)
    
    