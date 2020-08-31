from django.shortcuts import render


def login(request):
    if request.method=='POST':
        #email=request.POST['email']
        #password=request.POST['password']
        return render(request, 'rod/home.html')
    else:
        return render(request,'users/login.html')
