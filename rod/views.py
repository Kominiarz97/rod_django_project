from django.shortcuts import render

def home(request):
    return render(request,'rod/home.html',{'title':'Strona główna'})

def last_reports(request):
    return render(request,'rod/last_reports.html',{'title':'Ostatnie zgłoszenia'})

def drones(request):
    return render(request,'rod/drones.html',{'title':'Drony'})

def map(request):
    return render(request,'rod/map.html',{'title':'Mapa'})

def shedule(request):
    return render(request,'rod/shedule.html',{'title':'Rozkład jazdy'})

def all_archive(request):
    return render(request,'rod/all_archive.html',{'tittle':'Wszystkie zgłoszenia'})

def interv_archive(request):
    return render(request, 'rod/interv_archive.html',{'title':'Zgłoszenia niewymagające interwencji'})

def noninterv_archive(request):
    return render(request,'rod/noninterv_archive.html',{'title':'Zgłoszenia wymagające interwencji'})