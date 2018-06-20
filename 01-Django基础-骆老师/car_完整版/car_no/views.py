import datetime
from json import dumps, JSONEncoder

from django.core.serializers.json import DjangoJSONEncoder
from django import forms
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from car_no.models import Car


class CarRecordForm(forms.ModelForm):

    carno = forms.CharField(max_length=7 ,label='车牌号', error_messages={})
    case = forms.CharField(max_length=50, label='违章原因')
    punish = forms.CharField(max_length=50, required=False, label='处罚方式') #required 属性False可以不填

    class Meta:
        model = Car
        fields = ('carno', 'case', 'punish')


def add(request):

    if request.method == 'GET':
        errors = []
        f = CarRecordForm()
    else:
        f = CarRecordForm(request.POST)
        if f.is_valid():
            f.save()
            f = CarRecordForm()
        # else:
        #     errors = f.errors.values()  # 所有的错误信息
    return render(request, 'add.html', context={'f': f})

# class CarRecordForm(forms.Form):
#
#     carno = forms.CharField(max_length=7 ,label='车牌号', error_messages={})
#     case = forms.CharField(max_length=50, label='违章原因')
#     punish = forms.CharField(max_length=50, required=False, label='处罚方式') #required 属性False可以不填
#
#
# def add(request):
#
#     if request.method == 'GET':
#         errors = []
#         f = CarRecordForm()
#     else:
#         f = CarRecordForm(request.POST)
#         if f.is_valid():
#             a = f.cleaned_data # 获得输入的纯数据, 字典样式
#             Car(**a).save()
#             f = CarRecordForm()
#         else:
#             errors = f.errors.values()  # 所有的错误信息
#     return render(request, 'add.html', context={'f': f, 'errors': errors})


class CarRecordEncoder(DjangoJSONEncoder):  # DjangoJSONEncoder
    # pass
    def default(self, o):

        del o.__dict__['_state']
        print('===========>>>>>>>>>', o.__dict__)
        # o.__dict__['cardate'] = o.happen_date
        return o.__dict__


def ajax_search(request):
    if request.method == "GET":
        return render(request, 'ajax_search.html')
    else:
        carno = request.POST['carno']
        record_list = list(Car.objects.filter(carno__icontains=carno))
        return JsonResponse(record_list,encoder=CarRecordEncoder ,safe=False)


# 调用Cookie, 添加最后访问时间
#cookie是一个字典, 拿到时间, 如果没有就设置默认值, 默认值必须和cookie的类型相同, 字符串
# .set_cookie()  max_age 存在时间
def ajax_search(request):
    current_time = datetime.ctime()
    last_vist_time = request.COOKIES.get('last_vist_time',
                                         current_time)
    if request.method == "GET":
        response =  render(request, 'ajax_search.html',
                           {'last_time': last_vist_time})
        response.set_cookie('last_vist_time', current_time, max_age=1209600)  # 默认是即时清除
        return response
    else:
        carno = request.POST['carno']
        record_list = list(Car.objects.filter(carno__icontains=carno))
        return JsonResponse(record_list,encoder=CarRecordEncoder ,safe=False)

        # return HttpResponse(json.dumps(record_list), content_type='application/json; charset=utf-8')


def search(request):
    current_time = datetime.datetime.now().ctime()
    last_vist_time = request.COOKIES.get('last_vist_time', current_time)

    if request.method == 'GET':
        ctx = {'show_result': False, 'last_time': last_vist_time}
        response = render(request, 'search.html', ctx)
        response.set_cookie('last_vist_time', current_time, max_age=1209600)
        return response

    else:
        carno = request.POST['carno']
        ctx = {'show_result': True,
            'record_list': list(Car.objects.filter(carno__contains=carno))} # contians 模糊查询

    return render(request, 'search.html', context=ctx)


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


