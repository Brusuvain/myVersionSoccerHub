import imp
from django import forms
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from .forms import CredentialsForm
from .models import Teams, Credentials
 
CurrentLoggedInUser=Credentials()

def home(request):
      return TemplateResponse(request, 'home.html', {})

def error(request):
      return TemplateResponse(request,'error.html',{})

def register(request):
     credform=CredentialsForm(request.POST)
     myteamnames=list(Teams.objects.values_list('teamname'))
     if credform.is_valid():
        credform.save()
        return TemplateResponse(request, 'loggedinHome.html',{"teamnames":myteamnames})

     credform=CredentialsForm()
     return TemplateResponse(request, 'register.html', context={"form":credform})

def register_to_homepage(request):
    myteamnames=list(Teams.objects.values_list('teamname'))
    return TemplateResponse(request, 'loggedinHome.html',{"teamnames":myteamnames})

def login(request):
    if request.method=="POST":
      loginCreds=request.POST
      username=loginCreds.get('username')
      passw=loginCreds.get('password')
      if Credentials.objects.get(username=username):
            myuser= Credentials.objects.get(username__exact=username)
            if passw==myuser.password:
           
               CurrentLoggedInUser=myuser
             
               return login_to_homepage(request)
            else:
                 return redirect('error')
      else:
           return redirect('error') 
    return TemplateResponse(request, 'login.html')


def login_to_homepage(request):
      contextdic={}
      print(CurrentLoggedInUser.username)
      if CurrentLoggedInUser:
        
         contextdic["name"]=CurrentLoggedInUser.username
         contextdic["role"]=CurrentLoggedInUser.role
         return TemplateResponse(request,'loggenInHomeChangeOtherName.html',{'name':CurrentLoggedInUser.username})
      return redirect('error')
      




