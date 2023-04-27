from django.db import models

# Create your models here.
class employee_reg(models.Model):
    Name=models.CharField(max_length=200)
    dob=models.CharField(max_length=100)
    email=models.CharField(max_length=500)
    contact=models.CharField(max_length=500)
    Address=models.CharField(max_length=20)
    experience=models.CharField(max_length=500)
    gender=models.CharField(max_length=200)
    qualification=models.CharField(max_length=200)
    Password=models.CharField(max_length=200)
    def __str__(self) :
        return self.Name