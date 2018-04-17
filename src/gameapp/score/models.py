from django.db import models

# Create your models here.


class score(models.Model):
    score = models.IntegerField()
    id = models.AutoField(primary_key=True)
    