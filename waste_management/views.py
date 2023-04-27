from django.shortcuts import render,redirect
from django.contrib import messages
from . models import *
from survey. models import *
from Employee. models import *
# Create your views here.
def w1(request):
    return render(request,"waste/windex.html")

def wlogin(request):
    if request.method=="POST":
        try:
            email=request.POST.get('email')
            Password=request.POST.get('Password')
            login=waste_reg.objects.get(email= email,Password= Password)
            request.session['compowner']=login.compowner
            request.session['id']=login.id
            return redirect('wast')
        except waste_reg.DoesNotExist as e:
            messages.info(request,'Incorrect Password or Email')
    return render(request,"waste/wlogin.html")

def wreg(request):
    if request.method=="POST":
        compowner=request.POST.get("compowner")
        compid=request.POST.get("compid")
        email=request.POST.get("email")
        contact=request.POST.get("contact")
        location=request.POST.get("location")
        pincode=request.POST.get("pincode")
        typeofbussiness=request.POST.get("typeofbussiness")
        Password=request.POST.get("Password")
        confirmpassword=request.POST.get("cpassword")

        if Password==confirmpassword:
            if waste_reg.objects.filter(email=email).exists():
                messages.info(request,'Email already exists')
        
            else:
                data=waste_reg(compowner=compowner,compid=compid,email=email,contact=contact,
                            location= location,pincode=pincode,typeofbussiness=typeofbussiness,Password=Password)
                data.save()
                return redirect("wlog")
        else:
             messages.info(request,'password not match')
    return render(request,"waste/wreg.html")



def wprofile(request):
    hid=request.session['id']
    prof=waste_reg.objects.get(id=hid)
    
    
    edit=waste_reg.objects.get(id=hid)
    if request.method=="POST":
        

        edit.compowner=request.POST.get("compowner")
        edit.email=request.POST.get("email")
        edit.contact=request.POST.get("contact")
        edit.location=request.POST.get("location")
        edit.compid=request.POST.get("compid")
        edit.pincode=request.POST.get("pincode")
        edit.typeofbussiness=request.POST.get("typeofbussiness")
            
        edit.Password=request.POST.get("Password")
        edit.save()
        return redirect("wast")
    return render(request,"waste/wprofile.html",{'pro':prof,'pd':edit})

def whome(request):
    return render(request,"waste/whome.html")

def vimg(request):
    pro=addimg.objects.all()
    return render(request,'waste/wimg.html',{'pro':pro})

def image(request,id):
    addimg.objects.filter(id=id).update(approve=True)
    # return redirect('selemp')
    pro=employee_reg.objects.all()
    if request.method=="POST":
        emp=request.POST.get('emp')
        addimg.objects.filter(id=id).update(employee=emp)
        return redirect('wast')
    return render(request,'waste/selemp.html',{'pro':pro})


# def selemp(request,id):
#     addimg.objects.get(id=id)
#     pro=employee_reg.objects.all()
#     if request.method=="POST":
#         emp=request.POST.get('emp')
#         addimg.objects.filter(id=id).update(employee=emp)
#         return redirect('wast')
#     return render(request,'waste/selemp.html',{'pro':pro})


    