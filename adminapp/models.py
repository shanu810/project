from django.db import models

# Create your models here.
class adminreg(models.Model):
    email=models.CharField(max_length=500)
    Password=models.CharField(max_length=200)
    def __str__(self) :
        return self.email