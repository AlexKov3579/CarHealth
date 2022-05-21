from django.shortcuts import render
from django.http import JsonResponse
from .models import *
from login.models import User
from .forms import *

# Create your views here.
def main(request):
    error = ''
    if 'user' in request.session:
        logged_user = User.objects.get(pk = request.session['user'])
        user_cars = Car.objects.filter(userId = logged_user)
        print(user_cars.count)

    else:
        error = "You are not logged in"
        return render (request, "index.html", {'error' : error })

    return render (request, "index.html", {'error' : error, 'cars': user_cars})

def add_car(request):
    error = ''
    form = NewCarForm(request.POST)

def get_car(request):
    car_id = request.GET['car_id']
    
    car =  Car.objects.get(pk = car_id)
    if 'user' in request.session:
        logged_user = User.objects.get(pk = request.session['user'])
        if car.userId.pk != logged_user.pk:
            #user tries to acces car that is registered for another user
            return JsonResponse({'data': 'error'})
    return JsonResponse({'data': 'success'})
    #TODO response with json file with car and parts details
    pass
    


