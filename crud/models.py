from django.db import models

# Create your models here.
class Employees(models.Model):
    name = models.CharField(max_length=200)
    email= models.EmailField(max_length=150)
    address = models.CharField(max_length=200)
    phone = models.IntegerField() 
    
    def __str__(self):
        return self.name
    