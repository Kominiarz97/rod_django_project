from django.shortcuts import render,redirect
from django.contrib.auth.models import  User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm
from django.views.generic import DeleteView

def login(request):
    if request.user.is_authenticated:
        return redirect('/home')
    else:
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                redirect('/home')
            else:
                messages.info(request,'Niepoprawne dane')
                return redirect('/')
            return render(request, 'rod/home.html')
        else:
            return render(request,'users/login.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('/home')
    else:
        if request.method=='POST':
            first_name=request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            username = request.POST.get('username')
            email = request.POST.get('email')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('password2')
            code = request.POST.get('code')
            if(password1==password2 and code=='code1234'):
                if User.objects.filter(username=username).exists():
                    messages.info(request,'Nazwa użytkownika zajęta')
                    return redirect('/register')
                elif User.objects.filter(email=email).exists():
                    messages.info(request,'Adres email zajęty')
                    return redirect('/register')
                else:
                    user=User.objects.create_user(username=username,email=email,password=password1,first_name=first_name,last_name=last_name)
                    user.save()
                    return redirect('/')
            else:
                messages.info(request,'Hasła nie pasują')
                return redirect('/register')
        else:
            return render(request,'users/register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Dane zostaly zmienione! ')
            return redirect('/profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
    context = {
        'u_form': u_form,
    }
    return render(request, 'users/profile.html', context)

def del_user(request, pk):
    if request.method == "POST":
        try:
            u = User.objects.get(id = pk)
            u.delete()
            messages.success(request, "Konto usunięte")
            return redirect('/')
        except User.DoesNotExist:
            messages.error(request, "Nie ma takiego użytkownika")
            return redirect('/')
        except Exception as e:
            return render(request, 'users/profile.html',{'err':e.message})
    return render(request, 'users/user_confirm_delete.html')
