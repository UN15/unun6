from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import Acc_registerForm

def acc_login(request):
    if request.method == 'POST':
        l_form = AuthenticationForm(request =request, data = request.POST)
        if l_form.is_valid():
            username = l_form.cleaned_data.get("username")
            password = l_form.cleaned_data.get("password")
            user = authenticate(request = request, username = username, password = password)
            if user is not None:
                login(request, user)

        return redirect("gamemain")
    else:
        l_form=AuthenticationForm()
        return render(request, 'acc_login.html', {'l_form':l_form})

def acc_logout(request):
    logout(request)
    return redirect('gamemain')

def acc_register(request):
    if request.method == "POST":
        l_form = Acc_registerForm(request.POST)
        if l_form.is_valid():
            user = l_form.save()
            login(request, user)
        return redirect("gamemain")
    else:   
        l_form = Acc_registerForm()
        return render(request,'acc_signup.html', {'l_form':l_form})