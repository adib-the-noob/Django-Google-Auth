from django.shortcuts import render,redirect
from .forms import CreateUserForm
from django.contrib import messages
# Create your views here.

def userLogin(request):
    return render(request, 'login.html')

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