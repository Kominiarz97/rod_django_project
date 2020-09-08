from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='users-login'),
    path('register/', views.register, name='users-register'),
    path('logout/', views.logout, name='users-logout'),
]