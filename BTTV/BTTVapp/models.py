from django.db import models

# Create your models here.

class Regions(models.Model):
    region_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.region_name

class WestUS(models.Model):
    state_name = models.CharField(max_length=200)

class EastUS(models.Model):
    state_name = models.CharField(max_length=200)