
m json import dumps

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from car_no.models import Car


def car(request):

    ctx={'car_list': Car.objects.all()}
    return render(request, 'car.html', context=ctx)


def query(request):
    ctx = {'car_list': Car.objects.all()}
    return render(request, 'query.html', context=ctx)


def index(request):
    ctx = {
        'query': '/car_no/query',
        'car': '/car_no/car'
    }
    return render(request, 'index.html', context=ctx)



