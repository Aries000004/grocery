from json import dumps

from django.core.exceptions import ObjectDoesNotExist
from django import forms
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.utils.datastructures import MultiValueDictKeyError

from hrs.models import Dept, Emp

def index(request):
    ctx = {'gretting': '你好世界'}
    return render(request, 'index.html', context=ctx)


def depts(request):
    # DRY Don't Repeat Yourself
    # ORM Object Relation Mapping
    ctx = {'dept_list': Dept.objects.all()}
    return render(request, 'dept.html', context=ctx)


def del_dept(request, no='0'):
    try:
        # no = request.GET['no']
        Dept.objects.get(pk=no).delete()
        ctx = {'code': 200}    #  Ajax
    except (ObjectDoesNotExist, ValueError, MultiValueDictKeyError):
        ctx = {'code':404}
    return HttpResponse(dumps(ctx),
                        content_type='application/json; '
                                     'charset=utf-8')

def emps(request, no='0'):
    # dno = request.GET['no']
    dno = no
    emp_list = list(Emp.objects.filter(dept__no=dno).select_related('dept'))  # 联查, 关联对象字段名, models的class Dept
    ctx = {
        'emp_list': emp_list,
        'dept_name': emp_list[0].dept.name
    } if len(emp_list) > 0 else {}
    return render(request, 'emp.html', context=ctx)


class DeptForm(forms.Form):

    no = forms.IntegerField(label='部门编号')
    name = forms.CharField(max_length=20, label='部门名称')
    location = forms.CharField(max_length=20, label='部门所在地')


def add(request):
    if request.method == 'GET':
        f = DeptForm()
    else:
        f = DeptForm(request.POST)
        if f.is_valid():
            a = f.cleaned_data
            print(a)
            Dept(**a).save()
            f = DeptForm()
    return render(request, 'add.html', context={'f':f})