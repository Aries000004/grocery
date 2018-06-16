from django.http import HttpResponse
from django.shortcuts import render


def index(request):

    context_dict = {'blogmessage': 'creamy, cookie, candy, cupcake!'}

    return render(request, 'rango/index.html', context=context_dict)