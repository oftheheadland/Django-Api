from django.db import models

class Subscribe(models.Model):
    level = models.CharField(max_length=15)
    id = models.IntegerField(primary_key=True)
