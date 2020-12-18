from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='rod-home'),
    path('last-reports/', views.last_reports, name='rod-last-reports'),
    path('last-reports/submit/<str:pk>', views.report_submit, name='rod-report-submit'),
    path('last-reports/ignore/<str:pk>', views.report_ignore, name='rod-report-ignore'),
    path('drones/', views.drones, name='rod-drones'),
    path('drones/new', views.new_drone, name='rod-new_drone'),
    path('drones/update/<str:pk>', views.updateDron, name='rod-update_dron'),
    path('drones/delete/<str:pk>', views.delDron, name='rod-delete_dron'),
    path('routes/', views.routes, name='rod-routes'),
    path('routes/new', views.new_route, name='rod-new_route'),
    path('routes/update/<str:pk>', views.update_Route, name='rod-update_route'),
    path('routes/delete/<str:pk>', views.delRoute, name='rod-delete_route'),
    path('map/', views.map, name='rod-map'),
    path('all-archive/', views.all_archive, name='rod-all-archive'),
    path('interv-archive/', views.interv_archive, name='rod-interv-archive'),
    path('noninterv-archive/', views.noninterv_archive, name='rod-noninterv-archive'),
]