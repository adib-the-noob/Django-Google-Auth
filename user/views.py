from django.shortcuts import render,redirect
from .forms import CreateUserForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout 

from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        return redirect('login')


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

@login_required(login_url='login')
def userLogout(request):
    logout(request)
    return redirect('login')

def userRegister(request):
    form = CreateUserForm()
    if request.user.is_authenticated:
        return redirect('home')        

    else:
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login')
        form = CreateUserForm()
        context = {'form':form}
        return render(request, 'register.html', context)