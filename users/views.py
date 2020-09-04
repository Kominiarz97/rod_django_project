from django.shortcuts import render,redirect
from django.contrib.auth.models import  User,auth

def login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        return render(request, 'rod/home.html')
    else:
        return render(request,'users/login.html')

def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        code = request.POST['code']
        if(password1==password2 and code=='code1234'):
            user=User.objects.create_user(username=username,email=email,password=password1,first_name=first_name,last_name=last_name)
            user.save()
            print('Konto utworzone')
        else:
            print('hasla nie pasujo')
        return redirect('')
    else:
        print('nie działa')
        return render(request,'users/register.html')

