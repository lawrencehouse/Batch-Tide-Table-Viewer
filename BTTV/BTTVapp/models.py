from django.db import models

# Create your models here.

class States(models.Model):
    state_name = models.CharField(max_length=200)

