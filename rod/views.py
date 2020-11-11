from django.shortcuts import render, redirect
from django.contrib.auth.models import  User, auth
from .models import *
from django.core.paginator import Paginator

def home(request):
    if request.user.is_authenticated:
        return render(request,'rod/home.html',{'title':'Strona główna'})
    else:
        return redirect('/')

def last_reports(request):
    if request.user.is_authenticated:
        zgloszenia = Zgloszenia.objects.get_queryset().order_by('-id_zgloszenia')
        paginator = Paginator(zgloszenia, 1)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'rod/last_reports.html', {'title' : 'Ostatnie zgłoszenia', 'zgloszenia':page_obj})
    else:
        return redirect('/')


def drones(request):
    if request.user.is_authenticated:
        drony = Drony.objects.get_queryset().order_by('-id_drona')
        paginator = Paginator(drony, 2)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'rod/drones.html', {'title': 'Drony', 'drony': page_obj})

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
def new_drone(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.POST.get('name'):
                dron = Drony()
                dron.nazwa = request.POST.get('name')
                dron.pojemnosc_akumulatora = int(request.POST.get('capacity'))
                dron.predkosc_przelotowa = int(request.POST.get('speed'))
                dron.oswietlenie = request.POST.get('lighting')
                dron.save()
        return render(request, 'rod/new_drone.html', {'title': 'Drony_nowe'})


