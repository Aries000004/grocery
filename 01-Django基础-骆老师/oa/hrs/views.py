from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
import pymysql
from django.urls import reverse
from django.utils.datastructures import MultiValueDictKeyError

from hrs.models import Dept, Emp
import random
from json import dumps


def depts(request):
    # DRY Don't Repeat Yourself
    # ORM Object Relation Mapping
    ctx = {'dept_list': Dept.objects.all()}
    return render(request, 'dept.html', context=ctx)


# def emps(request):
#     dno = request.GET['no']
#     print(dno)
#     dept = Dept.objects.get(pk=dno)
#     ctx = {'emp_list': Emp.objects.filter(dept=dept)}
#     return render(request, 'emp.html', context=ctx)


# 方法1
# def emps(request):
#     dno = request.GET['no']
#     emp_set = Emp.objects.filter(dept__no=dno)
#     ctx = {
#         'emp_list': emp_set,
#         'dept_name': emp_set[0].dept.name
#     } if emp_set.count() > 0 else {}
#     return render(request, 'emp.html', context=ctx)


# # 方法2 , 用设置的关联名, 反查
# def emps(request):
#     no = request.GET['no']
#     dept = Dept.objects.get(no=no)
#     emps_list = dept.emp_set.all()   # 反查, 系统默认的related_name 是emp_set,自定义修改为 empsd
#     ctx = {
#         'emp_list': emps_list,
#         'dept_name': emps_list[0].dept.name
#     } if emps_list.count() > 0 else {}
#     return render(request, 'emp.html', context=ctx)


# 方法3 连接查询
def emps(request, no='0'):
    # dno = request.GET['no']
    dno = no
    emp_list = list(Emp.objects.filter(dept__no=dno).select_related('dept'))  # 联查, 关联对象字段名, models的class Dept
    ctx = {
        'emp_list': emp_list,
        'dept_name': emp_list[0].dept.name
    } if len(emp_list) > 0 else {}
    return render(request, 'emp.html', context=ctx)


# 重定向
def del_dept(request, no='0'):
    try:
        # no = request.GET['no']
        Dept.objects.get(pk=no).delete()
        ctx = {'code': 200}    #  Ajax
    except (ObjectDoesNotExist, ValueError, MultiValueDictKeyError):
        ctx = {'code':404}
    return HttpResponse(dumps(ctx),
                        content_type='application/json; '
                                     'charset=utf-8') # 返回类型
    # return HttpResponseRedirect(reverse('depts'))
    # return redirect(reverse('depts'))  # reverse  重定向



def AllEmps(request):
    ctx = {'emp_list': Emp.objects.all()}
    return render(request, 'dons.html', context=ctx)


def index(request):
    ctx = {'gretting': '你好世界'}
    return render(request, 'index.html', context=ctx)