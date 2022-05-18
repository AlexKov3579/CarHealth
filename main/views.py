from django.shortcuts import render
from .models import *
from login.models import User
from .forms import *

def main(request):
    error = ''
    if 'user' in request.session:
        logged_user = User.objects.get(pk = request.session['user'])
        user_cars = Car.object.filter(logged_user)

    else:
        error = "You are not logged in"
        return render (request, "index.html", {'error' : error })

    return render (request, "index.html", {'error' : error, 'cars': user_cars})

def add_car(request):
    error = ''
    form = NewCarForm(request.POST)

def get_car(request):
    car_id = request.get['car_id']
    
    car =  Car.objects.Get(pk = car_id)
    if 'user' in request.session:
        logged_user = User.objects.get(pk = request.session['user'])
        if car.User.pk != logged_user:
            #user tries to acces car that is registered for another user
            return #TODO error
    #TODO response with json file with car and parts details
    pass
    

# Create your views here.
