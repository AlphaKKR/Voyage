from django.shortcuts import render, redirect
from Accounts.models import UserAccount
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from .models import Room,Booking
from datetime import datetime

def Book(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        arrive = request.GET.get('arrive')
        departure = request.GET.get('departure')
        adults = request.GET.get('adults')
        
        arrive = datetime.date(datetime.strptime(arrive, '%Y-%m-%d'))
        departure = datetime.date(datetime.strptime(departure, '%Y-%m-%d'))

        print(id, arrive, departure, adults)

        room = Room.objects.get(room_id=id)
        param = {'object' : room}
    return render(request,'main/book.html',param)

def Description(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        room = Room.objects.get(room_id=id)
        param = {'object' : room}
    return render(request,'main/description.html',param)

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
        user = authenticate(email=email, password=password)
        if user is not None:
            return redirect('/home')
        return render(request, '/home',)

def Login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(40*'@', email, password)
        user = authenticate(email=email, password=password)
        print(40*'#', user)
        if user is not None:
            login(request, user)
            print('#####', user)
            return redirect('/home')
        else:
            return redirect('/home/login')
    return render(request, 'main/login.html')

def Logout(request):
    logout(request)
    return redirect('/home')

def Room_List(request):
    if request.method == 'POST':
        arrive = request.POST.get('arrive')
        departure = request.POST.get('departure')
        adults = request.POST.get('adults')

        arrive = datetime.date(datetime.strptime(arrive, '%Y-%m-%d'))
        departure = datetime.date(datetime.strptime(departure, '%Y-%m-%d'))
    
        instance = Room.objects.all()
        bookings = Booking.objects.all()
        param = {'objects': []}
        for i in bookings.iterator():
            if i.start >= departure or i.end <= arrive:
                id = i.room_id
                param['objects'].append(Room.objects.get(room_id=0))
        return render(request, 'main/room_list.html', param)
    else:
        instance = Room.objects.all()
        param = {'objects': instance}
        print(param)
        return render(request, 'main/room_list.html', param)


