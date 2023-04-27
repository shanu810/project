from django.shortcuts import render,redirect
from django.contrib import messages
from . models import *
from water.settings import RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY
import razorpay
# Create your views here.
def s1(request):
    return render(request,"survey/sindex.html")

def slogin(request):
    if request.method=="POST":
        try:
            Email=request.POST.get('email')
            Password=request.POST.get('Password')
            login=survey_reg.objects.get(Email= Email,Password= Password)
            request.session['Name']=login.Name
            request.session['id']=login.id
            return redirect('home')
        except survey_reg.DoesNotExist as e:
            messages.info(request,'Incorrect Password or Email')
    return render(request,"survey/slogin.html")

def sreg(request):
    if request.method=="POST":
        Name=request.POST.get("Name")
        Email=request.POST.get("Email")
        Contact=request.POST.get("Contact")
        Gender=request.POST.get("Gender")
        City=request.POST.get("city")
        Password=request.POST.get("Password")
        confirmpassword=request.POST.get("cpassword")

        if Password==confirmpassword:
            if survey_reg.objects.filter(Email=Email).exists():
                messages.info(request,'Email already exists')
        
            else:
                data=survey_reg(Name=Name,Email=Email,Contact=Contact,Gender=Gender,
                            City= City,Password=Password)
                data.save()
                return redirect("slog")
        else:
             messages.info(request,'password not match')
    return render(request,"survey/sreg.html")
def profile(request):
    hid=request.session['id']
    prof=survey_reg.objects.get(id=hid)
    return render(request,"survey/profile.html")

def c_editpro(request,id):
    edit=survey_reg.objects.get(id=id)
    if request.method=="POST":
        if len(request.FILES)!=0:
            
            edit.image=request.FILES.get('img')

            edit.Name=request.POST.get("Name")
            edit.Number=request.POST.get("Number")
            edit.Place=request.POST.get("Place")
            edit.Email=request.POST.get("Email")
            edit.Experience=request.POST.get("Experience")
                
            edit.Buisnessname=request.POST.get("Buisnessname")
            edit.Password=request.POST.get("Password")

            return redirect("Cdashboard")
        return render(request,'survey/editprofile.html',{'pro':edit})
def shome(request):
    return render(request,"survey/shome.html")

def image(request):
    if request.method=='POST':
        image=request.FILES.get('image')
        sur=request.session['id']
        file=addimg(image=image,survey_id=sur)
        file.save()
        return redirect('home')
    return render(request,'survey/image.html')


def profile(request):
    hid=request.session['id']
    prof=survey_reg.objects.get(id=hid)
    
    
    edit=survey_reg.objects.get(id=hid)
    if request.method=="POST":
        

        edit.Name=request.POST.get("Name")
        edit.Email=request.POST.get("email")
        edit.Contact=request.POST.get("contact")
        edit.City=request.POST.get("City")
        edit.Experience=request.POST.get("Experience")
        edit.Qualification=request.POST.get("Qualification")
            
        edit.Password=request.POST.get("Password")
        edit.save()
        return redirect("home")
    return render(request,"survey/profile.html",{'pro':prof,'pd':edit})


def viewimg(request):
    id=request.session['id']
    pro=addimg.objects.filter(survey=id)
    return render(request,'survey/viewimg.html',{'pro':pro})

client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))


def payment(request,pid):
    global amount
    # pro=addimg.objects.get(id=pid)
    # t=pro.trash
    # addimg.objects.filter(t !=0)
    addimg.objects.filter(id=pid).update(payment=True)
    addimg.objects.filter(id=pid).update(predict=False)
    amount=100
    print(amount)
    currency ="INR"
    api_key=RAZORPAY_API_KEY
    amt=int(amount)*100
    payment_order= client.order.create(dict(amount=amt,currency="INR",payment_capture=1))
    payment_order_id= payment_order['id'] 
    return render(request,'survey/payment.html',{'a':amount,'api_key':api_key,'order_id':payment_order_id})