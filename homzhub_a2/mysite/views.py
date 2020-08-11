from django.http import HttpResponse, FileResponse
from django.template import response
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import logout, login
from django.contrib import messages
from .models import StateMaster, RequestTypeMaster, StatusMaster, UserRequest
import datetime
from django.contrib.auth import logout as django_logout

def Login(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return HttpResponseRedirect('/request/')
        else:
           return render(request, 'Login.html')
    else:
        userid = request.POST["userid"]
        password = request.POST["password"]
        user = auth.authenticate(username=userid, password=password)

        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect('/request/')
        else:
            messages.info(request, 'Invalid login details')
            return HttpResponseRedirect('/Login/')

def Logout(request):
    if not request.user.is_authenticated:
        return render(request, 'Login.html')
    django_logout(request)
    return render(request, 'Login.html')

def Signup(request):
     if request.method == "GET":
         return render(request, 'Signup.html')
     else:
         username = request.POST['userid']
         email = request.POST['email']
         Password1 = request.POST['Password1']
         Password2 = request.POST['Password2']
         if Password1 != Password2:
             messages.info(request, 'Passwords not matching')
             return render(request, 'Signup.html')
         elif User.objects.filter(username=username).exists():
             messages.info(request, 'User already exist')
             return render(request, 'Signup.html')    
         elif User.objects.filter(email=email).exists():
             messages.info(request, 'email already exist')
             return render(request, 'Signup.html')
         else:
             authuser = User.objects.create_user(username = username, password=Password1, email=email)
             authuser.save()
             messages.info(request, 'Registered succesfully!')
             return HttpResponseRedirect('/Login/')
   


def RequestView(request):  
  if not request.user.is_authenticated:
      return render(request, 'Login.html')
  if request.method == 'GET':    
      return render(request, 'Base.html')            

def AddRequest(request):
  if not request.user.is_authenticated:
      return render(request, 'Login.html')
  if request.method == 'GET': 
      RequestType = RequestTypeMaster.objects.all()
      allstates =  StateMaster.objects.all()  
      context = {
        'RequestType':RequestType,
        'allstates':allstates,
      }
      return render(request, 'AddRequest.html', context) 
  else:
    count = 0
    Deep_cleaning = request.POST['Deep Cleaning']    
    Painting  = request.POST['Painting']
    Plumbing = request.POST['Plumbing']  
    Electrical = request.POST['Electrical'] 
    RequestDescription = request.POST['Rqdesc']    
    phonenum = request.POST['phonenum']
    ccode = request.POST['ccode']
    pcode = request.POST['pcode']
    state = request.POST['state']
    cityname = request.POST['cityname']
    print(Deep_cleaning)
    print(Painting)
    print(Plumbing)
    print(Electrical)
    print(RequestDescription)
    print(phonenum)
    print(ccode)
    print(pcode)
    print(state)
    print(cityname)          
    return render(request, 'AddRequest.html') 