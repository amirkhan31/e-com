from django.shortcuts import render, redirect
from .form import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 


def user_form(request):
    if request.method == "POST":
        check = UserForm(request.POST)
        if check.is_valid():
            new_user = check.save()
            username = check.cleaned_data.get("username")
            messages.success(request, f"Hey {username}, your account successfully created")
            new_user = authenticate(username=check.cleaned_data['username'],password=check.cleaned_data['password1'])
            login(request,new_user)
            return redirect("core:home")  
         
    else:
        check = UserForm()
    context = {
        'check':check
    }
    return render(request,'page-register.html',context) 


def login_view(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                username = fm.cleaned_data.get("username")
                password = fm.cleaned_data.get("password")
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, f"{username} successfully log in")
                    return redirect("core:home")
                else:
                    messages.warning(request, f"{username} does not exist")
        else:
            fm = AuthenticationForm()
        return render(request,"login.html",{"fm":fm})
    else:
        return redirect ("core:home")
    

def logout_view(request):
    username = request.user.username
    logout(request)
    messages.success(request, f"Hey {username}, you have been logged out successfully.")
    return redirect('auth:login')





# Create your views here.
