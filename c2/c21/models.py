from django.db import models
# model company#
class company(models.Model):
    fullname=models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    birhday = models.DateField()
  
   
   
   
