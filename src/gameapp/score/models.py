from django.db import models

class Score(models.Model):
    score = models.IntegerField()
    id = models.AutoField(primary_key=True)
    