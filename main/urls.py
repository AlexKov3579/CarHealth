from django.contrib import admin
from django.urls import path
from . import views

app_name = 'main'

urlpatterns =  [path('index.html', views.main, name='main'),
                path('add_car', views.add_car, name='add_car'),
                path('update', views.update, name='update')]
