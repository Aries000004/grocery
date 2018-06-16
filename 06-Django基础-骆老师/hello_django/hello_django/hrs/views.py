from django.shortcuts import render

from random import randrange


from datetime import datetime


# Create your views here.
def home(request):
    fruit_list = ['苹果', '草莓', '葡萄', '香蕉', '蓝莓', '西瓜', '榴莲', '香梨']
    start = randrange(len(fruit_list))
    end = randrange(len(fruit_list))
    start, end = (start, end) if end > start else (end, start)
    fruits = fruit_list[start:end]
    ctx = {
    'gretting': 'Hello,Django!',
    'current_time': datetime.now(),
    'num': len(fruits),
    'fruits': fruits
    }
    return render(request, 'index.html', ctx)
