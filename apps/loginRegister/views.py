from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from django.contrib import messages
from .forms import CreateUserForm



def loginUser(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')


    context ={

    }
    return render(request, 'loginUser.html', context)

def logoutUser(request):
    logout(request)
    return redirect('loginUser')

def registerUser(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for '+user)
            return redirect('loginUser')

    context = {'form':form}

    return render(request, 'registerUser.html', context)



def myAccount(request):



    context ={

    }
    return render(request, 'myaccount.html', context)