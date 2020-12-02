from django.contrib import admin
from django.urls import path,include
from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('rod.urls')),
    path('', include('users.urls')),
]
