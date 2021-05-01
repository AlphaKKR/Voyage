from django.shortcuts import render, redirect
from Accounts.models import UserAccount
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from .models import Room,Booking
from datetime import datetime
from Voyage.settings import EMAIL_HOST_USER
from django.core.mail import send_mail


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
            return redirect('/')
        return render(request, '/',)

def Login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return redirect('/login')
    return render(request, 'main/login.html')

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
        rooms = []
        for i in bookings.iterator():
            if i.start >= departure or i.end <= arrive:
                id = i.room_id
                if id not in rooms:
                    rooms.append(id)
                    param['objects'].append(Room.objects.get(room_id=id))
        return render(request, 'main/room_list.html', param)
    else:
        instance = Room.objects.all()
        param = {'objects': instance}
        print(param)
        return render(request, 'main/room_list.html', param)

@login_required(login_url='/login')



def Book(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        arrive = request.GET.get('arrive')
        departure = request.GET.get('departure')
        adults = request.GET.get('adults')
        arrive1 = arrive
        departure1 = departure
        arrive = datetime.date(datetime.strptime(arrive, '%Y-%m-%d'))
        departure = datetime.date(datetime.strptime(departure, '%Y-%m-%d'))

        instance = Room.objects.all()
        bookings = Booking.objects.filter(room_id = id)
        flag = 1
        for i in bookings.iterator():
            if not(i.start >= departure or i.end <= arrive):
                flag = 0
        if flag == 1:
            room = Room.objects.get(room_id = id)
            param = {'object' : room, 'start' : arrive1, 'end': departure1, 'adults': adults }
            return render(request,'main/book.html',param)
    return render(request,'main/book.html')

def Payment(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        arrive = request.GET.get('start')
        departure = request.GET.get('end')
        adults = request.GET.get('adults')
        print(40*"#", id,adults)
        Booking.objects.create(user = request.user , start = arrive, end = departure, room_id = id , adults = adults)

        subject = 'Voyage Booking Confirmation'
        message = f'{request.user.username} your booking from the dates {arrive} to {departure} for {adults} Adults has been confirmed'

        send_mail(subject, 
                  message, 
                  EMAIL_HOST_USER, 
                  [request.user.email], 
                  fail_silently = False)    
    
    return redirect('/')

def Logout(request):
    logout(request)
    return redirect('/')

def Advertise(request):
    if request.method == 'POST':
        if request.user.is_landlord:
            instance = Room(
                price=request.POST['price'], 
                details=request.POST['details'],
                room_desc=request.POST['room_desc'], 
                address=request.POST['address'], 
                cover_image=request.FILES['cover_image'],
                image_1=request.FILES['image_1'],
                image_2=request.FILES['image_2'],
                image_3=request.FILES['image_3'],
                image_4=request.FILES['image_4'],
                image_5=request.FILES['image_5'],
                image_6=request.FILES['image_6'],
                image_7=request.FILES['image_7'],
                image_8=request.FILES['image_8'],
                image_9=request.FILES['image_9'],
                image_10=request.FILES['image_10']
                )

            instance.save()
            
            return HttpResponse('Advertisement Submitted')
            
    return render(request, 'main/advertise.html')
