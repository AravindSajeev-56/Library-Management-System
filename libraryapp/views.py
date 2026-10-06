from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from .models import books
from .models import Bookingbooks
# Create your views here.



@login_required
def home(request):
    return render(request,'sample.html')

def loginview(request):
    uname= request.POST['username']
    pwd = request.POST['password']
    user = authenticate(request, username=uname, password=pwd)
    if user is not None:
        login(request, user)
        return redirect('home')
    else:
        return render(request,"login.html")
    
def logout_view(request):
    logout(request)
    return redirect('login')

def sign_up(request):
        uform = UserCreationForm(request.POST)
        if request.method == "POST":
             if uform.is_valid():
                uname = uform.cleaned_data.get('username')
                pwd = uform.cleaned_data.get('password1')
                user1=User.objects.create_user(username=uname,password=pwd)
                user1.save()
                user = authenticate(request, username=uname, password=pwd)
                login(request,user)
                return redirect('home')
        else:
            form1 = UserCreationForm()
            return render(request, 'registration/sign_up.html', {'form': form1})
        return render(request, 'registration/sign_up.html', {'form': uform})

def Resethome(request):
    return render(request, 'registration/ResetPassword.html')

def resetPassword(request):
    responseDic={}
    try:
        usern = request.POST['uname']
        recepient=request.POST['email']
        pwd=request.POST['password']
        #subject
        try:
            user=User.objects.get(username=usern)
            if user is not None:
                user.set_password(pwd)
                user.save()
                #send
                responseDic["errmsg"]="Password Reset Successfully"
                return render(request,"registration/ResetPassword.html",responseDic)
        except Exception as e:
            print(e)
            responseDic["errmsg"]="Email doesnt exit"
            return render(request,"registration/ResetPassword.html",responseDic)
    
    except Exception as e:
        print(e)
        responseDic["errmsg"]="Failed to reset password"
        return render(request,"registration/ResetPassword.html",responseDic)
    
def sample(request):
    return render(request,"sample.html")

def history(request):
    return render(request,"history.html")

def biography(request):
    return render(request,"biography.html")

def poetry(request):
    return render(request,"poetry.html")

def fantasy(request):
    return render(request,"fantasy.html")

def classics(request):
    return render(request,"classics.html")

def about(request):
    return render(request,"about.html")

def display1(request):
    responseDic={}
    responseDic["obj1"]=books.objects.filter(book_type='History',availability__gt=0).values()
    return render(request,"history.html",responseDic)

def display2(request):
    responseDic={}
    responseDic["obj1"]=books.objects.filter(book_type='Biography',availability__gt=0).values()
    return render(request,"biography.html",responseDic)

def display3(request):
    responseDic={}
    responseDic["obj1"]=books.objects.filter(book_type='Classics',availability__gt=0).values()
    return render(request,"classics.html",responseDic)

def display4(request):
    responseDic={}
    responseDic["obj1"]=books.objects.filter(book_type='Fantasy',availability__gt=0).values()
    return render(request,"fantasy.html",responseDic)

def display5(request):
    responseDic={}
    responseDic["obj1"]=books.objects.filter(book_type='Poetry',availability__gt=0).values()
    return render(request,"poetry.html",responseDic)

def display6(request):
    responseDic={}
    responseDic["obj1"]=books.objects.filter(book_type='Shortstory',availability__gt=0).values()
    return render(request,"shortstory.html",responseDic)

def viewallbooks(request):
    responseDic={}
    responseDic["obj1"]=books.objects.filter(availability__gt=0).values()
    return render(request,"sample.html",responseDic)

def booking(request):
    responseDic = {}
    if request.method=="POST":
        try:
            nm= request.POST['firstname']
            ad = request.POST['address']
            pl = request.POST['place']
            ph = request.POST['number']
            em = request.POST['email']
            bk = request.POST['bookid']
            responseDic["output1"]=nm
            responseDic["output2"]=ad
            responseDic["output3"]=pl
            responseDic["output4"]=ph
            responseDic["output5"]=em
            responseDic["output6"]=bk
            out=Bookingbooks(name=nm,address=ad,place=pl,number=ph,email=em,bookid=bk)
            out.save()
            responseDic["msg1"] = "Token Created"
            return render(request, "receipt.html", responseDic)
        except Exception as e:
            print(e)
            responseDic["msg2"] = "Try again"
            return render(request, "booking.html", responseDic)
    else:
        return render(request, "booking.html")
    










