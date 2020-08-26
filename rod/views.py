from django.shortcuts import render

def home(request):
    return render(request,'rod/home.html')

def last_reports(request):
    return render(request,'rod/last_reports.html')

def drones(request):
    return render(request,'rod/drones.html')

def map(request):
    return render(request,'rod/map.html')

def shedule(request):
    return render(request,'rod/shedule.html')