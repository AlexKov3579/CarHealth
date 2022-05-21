from django.contrib import admin
from django.urls import path
from . import views

app_name = 'main'

urlpatterns =  [path('index.html', views.main, name='main'),
                path('get_car', views.get_car, name='get_car')]
