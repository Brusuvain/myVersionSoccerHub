import imp
from django import forms
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from .forms import CredentialsForm

def home(request):
      return TemplateResponse(request, 'home.html', {})

def register(request):
     credform=CredentialsForm(request.POST)
     if credform.is_valid():
        credform.save()
        return redirect("website-home")
     credform=CredentialsForm()
     return TemplateResponse(request, 'register.html', context={"form":credform})


