from django.db import models

class book(models.Model):
    chapter=models.CharField(max_length=250)
    lesson=models.CharField(max_length=250)
    page=models.CharField(max_length=250)
