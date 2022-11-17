from django.shortcuts import render,redirect
from .forms import CreateUserForm
# Create your views here.

def userLogin(request):
    return render(request, 'login.html')

def userRegister(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'register.html', context)