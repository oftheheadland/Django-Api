from django.db import models

class Subscribe(models.Model):
    subscribe = models.CharField(max_length=15)
    id = models.IntegerField(primary_key=True)
