from json import dumps

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from car_no.models import Car


def ajax_search(request):
    if request.POST == "GET":
        return render(request, 'search2.html')
    else:
        carno = request.POST['carno']
        record_list = list(Car.objects.filter(carno__icontains=carno))
        return JsonResponse(record_list)