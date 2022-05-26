from dataclasses import fields
from django.shortcuts import render
from django.core import serializers
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
    if form.is_valid():
        fmanufacturer = form.cleaned_data.get('manufacturer')
        fmodel = form.cleaned_data.get('model')
        fengineType = form.cleaned_data.get('engineType')
        fengineVol = form.cleaned_data.get('engineVol')
        fyear = form.cleaned_data.get('year')
        flastCheck = form.cleaned_data.get('lastCheck')
        fnextCheck = form.cleaned_data.get('nextCheck')
        fkilometrage = form.cleaned_data.get('kilometrage')

        car = Car.objects.create(manufaturer = fmanufacturer,
                            model = fmodel,
                            engineType = fengineType,
                            engineVol = fengineVol,
                            year = fyear,
                            checkDate = flastCheck,
                            nextCheckDate = fnextCheck,
                            kilometrage = fkilometrage)
        
        part_types = PartsType.objects.all()
        for part in part_types:
            Part.objects.create(carId = car, typeId = part, currentCondition = 0)

def get_car(request):
    car_id = request.GET['car_id']
    
    car =  Car.objects.get(pk = car_id)
    if 'user' in request.session:
        logged_user = User.objects.get(pk = request.session['user'])
        if car.userId.pk != logged_user.pk:
            #user tries to acces car that is registered for another user
            return JsonResponse({'data': 'error'})
        car_parts = Part.objects.filter(carId = car_id)
        print(car_parts)
        serialized = serializers.serialize('json', car_parts,  use_natural_foreign_keys = True)
        print(serialized)
    return JsonResponse(serialized, safe=False)
    #TODO response with json file with car and parts details
    


