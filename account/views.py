from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
#from account.forms import RegistrationForm, AccountAuthenticationForm
from account.models import Account
from django.core.mail import send_mail
import random
import math

# Create your views here.
one_time_pwd = "123456"
gmail = "abc@example.com"



def otp_generate():
    #global one_time_pwd
    data = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    length = len(data)
    otpwd = ""
    for i in range(6):
        otpwd += data[math.floor(random.random()*length)]
    #one_time_pwd = otpwd
    return otpwd


def verify(request):
    global one_time_pwd
    global gmail
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        #adhaar = request.POST['adhaar']
        address = request.POST['address']
        phone = request.POST['phone']
        city = request.POST['city']
        state = request.POST['state']
        pin = request.POST['pin']
        password1 = request.POST['password1']
        otp = request.POST['otp']
        print("one",one_time_pwd)
        if gmail == email :
            if otp == one_time_pwd:
                user = Account.objects.create_user(username=username,password=password1,email=email,firstname=first_name,
                    lastname=last_name,address=address,city=city,state=state,phone_no=phone,pin=pin)
                user.save()
                print('user has been registered')
                return redirect('log_in')
            else:
                messages.info(request,"Your otp is wrong")
                return render(request,'register.html')
        else:
            messages.info(request,"Email id is not verified")
            return render(request,'register.html')
    else:
        return render(request,'register.html')

def log_in(request):
    if request.method=="POST":
        email =request.POST['email']
        password=request.POST['password']
        user = authenticate(email=email,password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            messages.info(request,'invalid credentials')
            return redirect("log_in")
    else:
        return render(request,'log_in.html')


def register(request):
    global one_time_pwd
    global gmail
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        #adhaar = request.POST['adhaar']
        address = request.POST['address']
        phone = request.POST['phone']
        city = request.POST['city']
        state = request.POST['state']
        pin = request.POST['pin']
        
        password1=request.POST['password1']
        password2=request.POST['password2']
        #print(address)
        if password1==password2:
            if Account.objects.filter(username=username).exists():
                messages.info(request,'user name is taken')
                return redirect('register')

            elif Account.objects.filter(email=email).exists():
                messages.info(request,'this email has already been registered')
                return redirect('register')
            else:
                one_time_pwd = otp_generate()
                print("one",one_time_pwd)
                gmail = email
                send_mail(
                    'Account Verification',
                    'Your one time password is '+one_time_pwd,
                    'sa.stutiagrawal@example.com',
                    [email],
                    fail_silently=False,
                )
                return render(request,'verify.html',{'username':username,'password':password1,'email':email,'first_name':first_name,
            'last_name':last_name,'address':address,'city':city,'state':state,'pin':pin,'phone':phone})
                
                
        else:
            messages.info(request,'password is not same')
            return redirect('register')
        
        return redirect('/')


    else:
        return render(request,'register.html')

def log_out(request):
    logout(request)
    return redirect('/')


def profile(request):
    return render(request,'profile.html')

def update(request):
    if request.method == "POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        address = request.POST['address']
        phone = request.POST['phone']
        city = request.POST['city']
        state = request.POST['state']
        pin = request.POST['pin']
        user = request.user
        user.firstname = first_name
        user.lastname = last_name
        user.address = address
        user.phone_no = phone
        user.city = city
        user.state = state
        user.pin = pin
        user.save()
        msg = "Your details has been updated"
        return render(request,'message.html',{'msg':msg})
    else:
        return render(request,'update.html')

