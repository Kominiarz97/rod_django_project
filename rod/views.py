from django.shortcuts import render, redirect
from django.contrib.auth.models import  User, auth
from .models import *
from django.core.paginator import Paginator
from .forms import DronUpdateForm, RouteUpdateForm
from base64 import b64encode

def home(request):
    if request.user.is_authenticated:
        return render(request,'rod/home.html',{'title':'Strona główna'})
    else:
        return redirect('/')

def map(request):
    if request.user.is_authenticated:
        zgloszenia = Zgloszenia.objects.all()
        return render(request,'rod/map.html',{'title':'Mapa', 'zgloszenia':zgloszenia})
    else:
        return redirect('/')

# -----------------------------------------------------------------------------ZGŁOSZENIA------------------------------------------------------------
def last_reports(request):
    if request.user.is_authenticated:
        zgloszenia = Zgloszenia.objects.filter(zarejestrowane=False).order_by('-id_zgloszenia')
        for row in zgloszenia:
            row.zdjecie = b64encode(row.zdjecie).decode('ascii')

        paginator = Paginator(zgloszenia, 1)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'rod/last_reports.html', {'title' : 'Ostatnie zgłoszenia', 'zgloszenia':page_obj})
    else:
        return redirect('/')


def report_submit(request, pk):
    if request.user.is_authenticated:
        zgloszenie = Zgloszenia.objects.get(id_zgloszenia=pk)
        if request.method == 'POST':
            zgloszenie.zarejestrowane = True
            zgloszenie.uzytkownik_id = request.user.id
            zgloszenie.zgloszenie_sluzbom = True
            zgloszenie.save()
            return redirect('/last-reports')
        return render(request, 'rod/report_submit.html', {'zgloszenie':zgloszenie})

    else:
        return redirect('/')


def report_ignore(request, pk):
    if request.user.is_authenticated:
        zgloszenie = Zgloszenia.objects.get(id_zgloszenia=pk)
        if request.method == 'POST':
            zgloszenie.zarejestrowane = True
            zgloszenie.uzytkownik_id = request.user.id
            zgloszenie.zgloszenie_sluzbom = False
            zgloszenie.save()
            return redirect('/last-reports')
        return render(request, 'rod/report_ignore.html', {'zgloszenie': zgloszenie})

    else:
        return redirect('/')
# -----------------------------------------------------------------------------TRASY-------------------------------------------------------------

def routes(request):
    if request.user.is_authenticated:
        trasy = Trasy.objects.get_queryset().order_by('id_trasy')
        paginator = Paginator(trasy, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'rod/routes.html',{'trasy':page_obj})
    else:
        return redirect('/')

def new_route(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.POST.get('name'):
                trasa = Trasy()
                trasa.nazwa_trasy = request.POST.get('name')
                trasa.stacja_poczatek = request.POST.get('first')
                trasa.stacja_koniec = request.POST.get('last')
                trasa.dlugosc_trasy = request.POST.get('length')
                trasa.save()
        return render(request, 'rod/new_route.html')

def update_Route(request, pk):
    if request.user.is_authenticated:
        trasa = Trasy.objects.get(id_trasy = pk)
        form = RouteUpdateForm(instance = trasa)

        if request.method == 'POST':
            form = RouteUpdateForm(request.POST, instance=trasa)
            if form.is_valid():
                form.save()
                return redirect('/routes')
        context = {'form':form}
        return render(request, 'rod/route_update.html', context)
    else:
        return redirect('/')


def delRoute(request, pk):
    if request.user.is_authenticated:
        trasa = Trasy.objects.get(id_trasy = pk)
        if request.method == 'POST':
            trasa.delete()
            return redirect('/')
        context = {'trasa': trasa}
        return render(request, 'rod/route_confirm_delete.html', context)



# -----------------------------------------------------------------------------DRONY-------------------------------------------------------------
def drones(request):
    if request.user.is_authenticated:
        drony = Drony.objects.get_queryset().order_by('-id_drona')
        paginator = Paginator(drony, 5)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'rod/drones.html', {'title': 'Drony', 'drony': page_obj})

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
                dron.udzwig = request.POST.get('weight')
                dron.oswietlenie = request.POST.get('lighting')
                dron.save()
        return render(request, 'rod/new_drone.html', {'title': 'Drony_nowe'})



def updateDron(request, pk):
    if request.user.is_authenticated:
        dron = Drony.objects.get(id_drona = pk)
        form = DronUpdateForm(instance = dron)

        if request.method == 'POST':
            form = DronUpdateForm(request.POST, instance=dron)
            if form.is_valid():
                form.save()
                return redirect('/drones')
        context = {'form':form}
        return render(request, 'rod/dron_update.html', context)
    else:
        return redirect('/')


def delDron(request,pk):
    if request.user.is_authenticated:
        dron = Drony.objects.get(id_drona = pk)
        if request.method == "POST":
                dron.delete()
                return redirect('/')
        context = {'dron':dron}
        return render(request, 'rod/dron_confirm_delete.html', context)
    else:
        return redirect('/')


##-----------------------------------------------------------------------------ARCHIWUM-------------------------------------------------------------
def all_archive(request):
    if request.user.is_authenticated:
        zgloszenia = Zgloszenia.objects.filter(zarejestrowane=True).order_by('-id_zgloszenia')
        for row in zgloszenia:
            row.zdjecie = b64encode(row.zdjecie).decode('ascii')
        paginator = Paginator(zgloszenia, 1)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request,'rod/all_archive.html',{'tittle':'Wszystkie zgłoszenia', 'zgloszenia':page_obj})
    else:
        return redirect('/')

def interv_archive(request):
    if request.user.is_authenticated:
        zgloszenia = Zgloszenia.objects.filter(zgloszenie_sluzbom=True, zarejestrowane=True).order_by('-id_zgloszenia')
        for row in zgloszenia:
            row.zdjecie = b64encode(row.zdjecie).decode('ascii')
        paginator = Paginator(zgloszenia, 1)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'rod/interv_archive.html',{'title':'Zgłoszenia wymagające interwencji', 'zgloszenia':page_obj})
    else:
        return redirect('/')

def noninterv_archive(request):
    if request.user.is_authenticated:
        zgloszenia = Zgloszenia.objects.filter(zgloszenie_sluzbom=False, zarejestrowane=True).order_by('-id_zgloszenia')
        for row in zgloszenia:
            row.zdjecie = b64encode(row.zdjecie).decode('ascii')
        paginator = Paginator(zgloszenia, 1)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request,'rod/noninterv_archive.html',{'title':'Zgłoszenia niewymagające interwencji','zgloszenia':page_obj})
    else:
        return redirect('/')



