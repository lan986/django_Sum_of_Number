from imaplib import _Authenticator
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def registers(request):
 
    if request.method=='POST' :

        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        user_name=request.POST['user_name']
        email=request.POST['email']
        password=request.POST['password']
        Confpassword=request.POST['conf_password']

        if password==Confpassword:
            if User.objects.filter(username=user_name):
                print("user already exist ")
                messages.info(request,' user exist  ')
                return redirect('registers')

            else :
                user=User.objects.create_user(username=user_name,first_name=first_name,last_name=last_name,email=email,password=password)
                user.save()
                print("user created")
                messages.info(request,' user created  ')
                return redirect('/index')
        
        else :
            print("password not matched ")
            messages.info(request,'password not matching ')
            return redirect('registers')
    else:
        return render(request,'registers.html')



def login(request):
            if request.method =='POST ' :
               username=request.POST['first_name']
               email=request.POST['email']
               user=_Authenticate(username=username,password=password)
               if user is not None:
                 print("authonticated")
                 return redirect("/index")
               else :
                print("not authonticated") 
                return redirect("login") 

            else :
                return render(request,'login.html')      