from django.shortcuts import render,redirect
from django.contrib import messages
from . models import *
from survey . models import *
from Employee. models import *
from waste_management. models import *

# Create your views here.
def ahome(request):
    return render(request,"admin/index.html")

def alogin(request):
    if request.method=="POST":
        try:
            email=request.POST.get('email')
            Password=request.POST.get('password')
            login=adminreg.objects.get(email= email,Password= Password)
            request.session['Name']=login.email
            request.session['id']=login.id
            return redirect('ahome')
        except adminreg.DoesNotExist as e:
            messages.info(request,'Incorrect Password or Email')
    return render(request,"admin/login.html")

def areg(request):
    if request.method=="POST":
        email=request.POST.get("email")
        Password=request.POST.get("password")
        confirmpassword=request.POST.get("cpassword")

        if Password==confirmpassword:
            if adminreg.objects.filter(email=email).exists():
                messages.info(request,'Email already exists')
        
            else:
                data=adminreg(email=email,Password=Password)
                data.save()
                return redirect("alogin")
        else:
             messages.info(request,'password not match')
    return render(request,"admin/register.html")

def tables(request):
    su=survey_reg.objects.all()
    emp=employee_reg.objects.all()
    was=waste_reg.objects.all()
    return render(request,"admin/tables.html",{'su':su,'emp':emp,'was':was})
