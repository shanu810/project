from django.db import models

# Create your models here.
class waste_reg(models.Model):
    compowner=models.CharField(max_length=200)
    compid=models.CharField(max_length=100)
    email=models.CharField(max_length=500)
    contact=models.CharField(max_length=500)
    location=models.CharField(max_length=20)
    pincode=models.CharField(max_length=500)
    typeofbussiness=models.CharField(max_length=200)
    Password=models.CharField(max_length=200)
    def __str__(self) :
        return self.compowner
    
# class showimg(models.Model):
    