from django.db import models

# Create your models here.

class Regions(models.Model):
    region_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.region_name

class Station(models.Model):
    state_id = models.CharField(max_length=200)
    station_id = models.CharField(max_length=200)
    location_name = models.CharField(max_length=200)
    region = models.ForeignKey(Regions, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return f'{self.state_id}-{self.location_name}'