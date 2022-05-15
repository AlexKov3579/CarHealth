from django.contrib import admin
from django.urls import path
from . import views
from main import views as mviews

app_name = 'login'

urlpatterns = [ path('', views.login),
                path('login.html', views.login),
                path('register.html', views.register)]
