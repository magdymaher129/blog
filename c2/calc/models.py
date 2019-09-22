from django.db import models

class op(models.Model):
    name=models.CharField(max_length=250)
    address=models.CharField(max_length=250)
    email=models.CharField(max_length=250)
    age=models.IntegerField()
    birthdate=models.DateTimeField()
    
class jobsInfo(models.Model):
    title=models.CharField(max_length=100)
    depart=models.CharField(max_length=100)
    
    
   
    
    
  
 
