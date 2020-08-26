from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='rod-home'),
    path('last-reports/', views.last_reports, name='rod-last-reports'),
    path('drones/', views.drones, name='rod-drones'),
    path('map/', views.map, name='rod-map'),
    path('shedule/', views.shedule, name='rod-shedule')
]