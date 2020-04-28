from django.shortcuts import render, redirect
from .forms import (
    EmployeeRegisterFormv1,
    EmployeeRegisterFormv2,
    EmployeeLoginForm )
# from .models import EmployeeProfile
# from passlib.hash import pbkdf2_sha256
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
def registraion(request):
    form1 = EmployeeRegisterFormv1(request.POST or None)
    form2 = EmployeeRegisterFormv2(request.POST or None)
    if form1.is_valid() and form2.is_valid():
        user = form1.save()
        employee_profile = form2.save(commit=False)
        employee_profile.user = user
        employee_profile.save()
        return redirect('login')
    return render(request, 'employee/register.html', {"form1":form1,'form2':form2})

def employee_login(request):
    context = {}
    form = EmployeeLoginForm(request.POST or None)
    if form.is_valid():
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user_info = authenticate(request, username=username, password=password)
        # print("ll", user_info.username)
        if user_info:
            login(request, user_info)
            return redirect('/viewprofile/')
        else:
            context.update({"error": "login credential is wrong"})
    context.update({"form": form})
    return render(request, 'employee/login.html', context)


def employee_logout(request):
    logout(request)
    return HttpResponse("<h1>logged out successfuly</h1> <h4 class='display-3'>for sign in your "
                        "account click "
                        "on "
                        "<a "
                        "href='/login/'>log in </a> </h4>")

@login_required(login_url='/login/')
def employee_profile(request):
    user = request.user
    return HttpResponse(f"""<h1>Hi this is my profile, My name is {user.username} and salary: 
            {user.employeeprofile.salary}</h1> <h4 class='h5'>for sign out your account click on <a 
            href='/logout/'>Log out</a></h4>""")

