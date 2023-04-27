from django.shortcuts import render,redirect
from django.contrib import messages
from . models import *
from survey. models import *
# Create your views here.
def e1(request):
    return render(request,"employee/eindex.html")

def elogin(request):
    if request.method=="POST":
        try:
            email=request.POST.get('email')
            Password=request.POST.get('Password')
            login=employee_reg.objects.get(email= email,Password= Password)
            request.session['Name']=login.Name
            request.session['id']=login.id
            return redirect('emp')
        except employee_reg.DoesNotExist as e:
            messages.info(request,'Incorrect Password or Email')
    return render(request,"employee/elogin.html")

def ereg(request):
    if request.method=="POST":
        Name=request.POST.get("Name")
        email=request.POST.get("email")
        contact=request.POST.get("contact")
        gender=request.POST.get("gender")
        dob=request.POST.get("dob")
        qualification=request.POST.get("qualification")
        experience=request.POST.get("experience")
        Password=request.POST.get("Password")
        confirmpassword=request.POST.get("cpassword")

        if Password==confirmpassword:
            if employee_reg.objects.filter(email=email).exists():
                messages.info(request,'Email already exists')
        
            else:
                data=employee_reg(Name=Name,email=email,contact=contact,gender=gender,
                            dob= dob,qualification=qualification,experience=experience,Password=Password)
                data.save()
                return redirect("elog")
        else:
             messages.info(request,'password not match')
    return render(request,"employee/ereg.html")
def eprofile(request):
    hid=request.session['id']
    prof=employee_reg.objects.get(id=hid)
    
    
    edit=employee_reg.objects.get(id=hid)
    if request.method=="POST":
        

        edit.Name=request.POST.get("Name")
        edit.email=request.POST.get("email")
        edit.contact=request.POST.get("contact")
        edit.Address=request.POST.get("Address")
        edit.experience=request.POST.get("experience")
        edit.qualification=request.POST.get("qualification")
            
        edit.Password=request.POST.get("Password")
        edit.save()
        return redirect("emp")
    return render(request,"employee/eprofile.html",{'pro':prof,'pd':edit})

    



def ehome(request):
    return render(request,"employee/ehome.html")


def ewaste(request):
    id=request.session['id']
    pro=employee_reg.objects.get(id=id)
    name=pro.Name
    was=addimg.objects.filter(approve=True,employee=name)
    return render(request,'employee/eimages.html',{'was':was})

def prediction(request,id):
    waste=addimg.objects.get(id=id)
    import cv2
    import tensorflow as tf
    import keras
    img=str(waste.image)
    if request.method=="POST":
        img='media/'+ img

        img = cv2.imread(img)
        img = img/255
        tensor_img = tf.convert_to_tensor(img,dtype=tf.float32)
        
        tensor_img = tf.image.resize(tensor_img,[224,224])
        tensor_img = tensor_img[tf.newaxis,...,]
        
        class_names = ['cardboard','metal','paper','plastic','trash']
        model_path = 'MobileNetV2'
        model = tf.keras.models.load_model(model_path)
        out=class_names[model.predict(tensor_img).argmax()]
        addimg.objects.filter(id=id).update(trash=out)
        addimg.objects.filter(id=id).update(predict=True)
        return render(request,"employee/eresult.html",{'was':waste,'out':out})
        # return redirect('eresult')

    
    return render(request,"employee/predict.html",{'w':waste})

# def eresult(request,id):
#     was=addimg.objects.get(id=id)
#     return render(request,"employee/predict.html",{'was':was})

