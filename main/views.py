from django.shortcuts import render, redirect
from .models import *
from login.models import User
from .forms import *

# Create your views here.
def main(request):
    error = ''
    if 'user' in request.session:
        car_details = get_cars_details(request)
        context = {'error' : error} | car_details
        # forms = {}
        # for car in car_details.get('cars'):
        #     forms[car.pk] = UpdatePartForm(kilometrage = car.kilometrage, carId = car.pk)
        # context = context | {'forms': forms}
        context = context | {'update_form': UpdatePartForm()}
    else:
        error = "You are not logged in"
        return render (request, "index.html", {'error' : error })
    return render (request, "index.html", context)

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

def get_cars_details(request):
    if 'user' in request.session:
        logged_user = User.objects.get(pk = request.session['user'])
        cars = Car.objects.filter(userId = logged_user)
        parts = Part.objects.filter(carId__in = cars)
        part_types = PartsType.objects.all()
        return {'cars' : cars, 'parts' : parts, 'part_types': part_types}

def update(request):
    form = UpdatePartForm(request.POST)
    if form.is_valid():
        part_id = form.cleaned_data.get('partId')
        form_value = form.cleaned_data.get('newValue')
        car_id = form.cleaned_data.get('carId')
        if form.cleaned_data.get('updateAll') == 1:
            car = Car.objects.get(pk = car_id)
            for part in Part.objects.filter(carId = car):
                difference = form_value - car.kilometrage 
                new_value = part.currentCondition + difference
                updatePart(part.pk, new_value)
            car.kilometrage = form_value
            car.save()
            return main(request)
        updatePart(part_id, new_value)
    return redirect('main:main')


#private methods
def updatePart(part_id, new_value):
    part = Part.objects.get(pk = part_id)
    if part.currentCondition < new_value:
            part.currentCondition = new_value
    part.save()



    


