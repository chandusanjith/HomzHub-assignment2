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
from rest_framework import viewsets
from .serializers import UserRequestSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


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
      Requests = UserRequest.objects.filter(RequestedUser=request.user)
      context = {
        'Requests':Requests
      }
      return render(request, 'Base.html', context)            

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
    RequestType =  request.POST['rtype'];
    RequestDescription = request.POST['Rqdesc']    
    phonenum = request.POST['phonenum']
    ccode = request.POST['ccode']
    pcode = request.POST['pcode']
    state = request.POST['state']
    cityname = request.POST['cityname']
    Request_Instance = RequestTypeMaster.objects.get(id=RequestType)
    State_Instance = StateMaster.objects.get(id=state)
    Status_Instance = StatusMaster.objects.get(id=1)
    Request = UserRequest(RequestedUser=request.user,RequestType=Request_Instance,RequestDesc=RequestDescription,City=cityname,State=State_Instance,Pincode=pcode,PhoneCode=pcode,Phone=phonenum,Status=Status_Instance,Remark='pending')
    Request.save()
    return HttpResponseRedirect('/request/')


class RequestViewSet(viewsets.ModelViewSet):
  authentication_classes = [SessionAuthentication, BasicAuthentication]
  permission_classes = [IsAuthenticated]
  serializer_class = UserRequestSerializer
  queryset = UserRequest.objects.all() 
  def get_queryset(self):
    if self.action == 'list':       
      return self.queryset.filter(RequestedUser=self.request.user)
    return self.queryset
   

   