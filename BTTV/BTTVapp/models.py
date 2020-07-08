from django.db import models

# Create your models here.

class Station(models.Model):
    state_id = models.CharField(max_length=200)
    station_id = models.CharField(max_length=200)
    location_name = models.CharField(max_length=200)

class Regions(models.Model):
    region_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.region_name