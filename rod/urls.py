from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='rod-home'),
    path('last-reports/', views.last_reports, name='rod-last-reports'),
    path('drones/', views.drones, name='rod-drones'),
    path('map/', views.map, name='rod-map'),
    path('shedule/', views.shedule, name='rod-shedule'),
    path('all-archive/', views.all_archive, name='rod-all-archive'),
    path('interv-archive/', views.interv_archive, name='rod-interv-archive'),
    path('noninterv-archive/', views.noninterv_archive, name='rod-noninterv-archive'),
    path('drones/new', views.new_drone, name='rod-new_drone'),
]