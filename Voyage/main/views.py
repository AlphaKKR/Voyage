from django.shortcuts import render, redirect
from Accounts.models import UserAccount
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse

def Login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(40*'@', email, password)
        user = authenticate(email=email, password=password)
        print(40*'#', user)
        if user is not None:
        
            return HttpResponse('User Authenticated')
        else:
            return HttpResponse('User does not exist')
    return render(request, 'main/login.html')