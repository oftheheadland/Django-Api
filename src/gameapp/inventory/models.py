from django.db import models

# Create your models here.

class Inventory(models.Model):
    description = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)