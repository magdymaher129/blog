from django.db import models

class info(models.Model):
    name=models.CharField(max_length=250)
    address=models.CharField(max_length=250)
    age=models.IntegerField()
    