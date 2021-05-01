from django.shortcuts import render, redirect
from Accounts.models import UserAccount
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from .models import Room,Booking

def Book(request):
    
    if request.method == 'GET':
        id = request.GET.get('id')
        room = Room.objects.get(room_id=id)
        param = {'object' : room}
    return render(request,'main/book.html',param)

def Description(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        room = Room.objects.get(room_id=id)
        param = {'object' : room}
    return render(request,'main/description.html',param)

def Filtered(request):
     if request.method == 'POST':
        arrive = request.POST.get('arrive')
        departure = request.POST.get('departure')
        adults = request.POST.get('adults')
        print("#############", arrive)
        return render(request, 'main/room_list.html', param)

def Home(request):
    instance = Room.objects.all()
    instance = instance[0:4]
    param = {'objects': instance}
    return render(request,'main/home.html',param)

def Register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        contact = request.POST.get('contact')
        name = request.POST.get('name')
        user = UserAccount.objects.create_user(username=name, email = email, password = password, contact_no = contact)
        return HttpResponse("Registered")
        #return render(request, '/home',)

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

def Room_List(request):
    instance = Room.objects.all()
    param = {'objects': instance}
    return render(request, 'main/room_list.html', param)