from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='users-login'),
    path('register/', views.register, name='users-register'),
    path('logout/', views.logout, name='users-logout'),
    path('profile/', views.profile, name='users-profile'),
    path('profile/delete/<str:pk>/', views.del_user, name='user-delete'),
]