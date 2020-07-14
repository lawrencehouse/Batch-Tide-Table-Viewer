from django.db import models

# Create your models here.

class Region(models.Model):
    region_name = models.CharField(max_length=200)
    path_name = models.CharField(max_length=200)
    

    def __str__(self):
        return self.region_name

class Station(models.Model):
    state_id = models.CharField(max_length=200)
    station_id = models.CharField(max_length=200)
    location_name = models.CharField(max_length=200)
    region = models.ForeignKey(Region, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return f'{self.state_id}-{self.location_name}'