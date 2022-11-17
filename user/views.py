from django.shortcuts import render

# Create your views here.

def userLogin(request):
    return render(request, 'login.html')

def userRegister(request):
    return render(request, 'register.html')