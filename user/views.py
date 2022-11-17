from django.shortcuts import render,redirect
from .forms import CreateUserForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout 
# Create your views here.


def home(request):
    return render(request, 'home.html')


def userLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not  None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect!')
    return render(request, 'login.html')

def userLogout(request):
    logout(request)
    return redirect('login')

def userRegister(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')

    context = {'form':form}
    return render(request, 'register.html', context)