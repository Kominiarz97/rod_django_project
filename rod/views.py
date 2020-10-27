from django.shortcuts import render, redirect
from django.contrib.auth.models import  User, auth
from .models import Zagrozenia, Zgloszenia

def home(request):
    if request.user.is_authenticated:
        return render(request,'rod/home.html',{'title':'Strona główna'})
    else:
        return redirect('/')

def last_reports(request):
    if request.user.is_authenticated:
        zgloszenia = Zgloszenia.objects.all()

        return render(request, 'rod/last_reports.html', {'title' : 'Ostatnie zgłoszenia', 'zgloszenia':zgloszenia})
    else:
        return redirect('/')


def drones(request):
    if request.user.is_authenticated:
        return render(request,'rod/drones.html', {'title':'Drony'})
    else:
        return redirect('/')

def map(request):
    if request.user.is_authenticated:
        zgloszenia = Zgloszenia.objects.all()
        return render(request,'rod/map.html',{'title':'Mapa', 'zgloszenia':zgloszenia})
    else:
        return redirect('/')

def shedule(request):
    if request.user.is_authenticated:
        return render(request,'rod/shedule.html',{'title':'Rozkład jazdy'})
    else:
        return redirect('/')

def all_archive(request):
    if request.user.is_authenticated:
        return render(request,'rod/all_archive.html',{'tittle':'Wszystkie zgłoszenia'})
    else:
        return redirect('/')

def interv_archive(request):
    if request.user.is_authenticated:
        return render(request, 'rod/interv_archive.html',{'title':'Zgłoszenia niewymagające interwencji'})
    else:
        return redirect('/')

def noninterv_archive(request):
    if request.user.is_authenticated:
        return render(request,'rod/noninterv_archive.html',{'title':'Zgłoszenia wymagające interwencji'})
    else:
        return redirect('/')



