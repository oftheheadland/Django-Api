from django.db import models

class Score(models.Model):
    score = models.CharField(max_length=15)
    id = models.IntegerField(primary_key=True)
    