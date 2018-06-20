from django.http import HttpResponse
from django.shortcuts import render

from rango.models import Category, Page


def proj_index(request):

    return render(request, 'proj_index.html')


def rango_index(request):
    category_like = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_like}
    return render(request, 'rango/index.html', context_dict)


def add_category(request):

    return render(request, 'rango/add_category.html')


def run_query():
    pass


def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)   # 用前面在models-category中得到要查找的category, 然后在models-page中找打该类里面的所有页面
        context_dict['pages'] = pages
        context_dict['category'] = category

    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None

    context_dict['query'] = Category.name

    result_list = []
    if request.method == 'POST':
        query = request.POST['query'].strip()
        if query:
            result_list = run_query(query)
            context_dict['query'] = query
    context_dict['result_list'] = result_list

    return render(request, 'rango/category.html', context_dict)