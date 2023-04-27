from django.db import models

# Create your models here.
class survey_reg(models.Model):
    Name=models.CharField(max_length=200)
    Email=models.CharField(max_length=100)
    Contact=models.CharField(max_length=500)
    Gender=models.CharField(max_length=500)
    City=models.CharField(max_length=20)
    Qualification=models.CharField(max_length=500)
    Experience=models.CharField(max_length=200)
    Password=models.CharField(max_length=200)
    def __str__(self) :
        return self.Name
    
    
class addimg(models.Model):
    image=models.ImageField(upload_to='trash')
    approve=models.BooleanField(default=False)
    trash=models.CharField(max_length=50,default=0)
    employee=models.CharField(max_length=50,default=0)
    survey=models.ForeignKey(survey_reg,on_delete=models.CASCADE,null=True)
    payment=models.BooleanField(default="False")
    predict=models.BooleanField(default=False)

