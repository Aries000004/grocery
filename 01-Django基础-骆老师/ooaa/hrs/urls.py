from django.urls import path

from hrs import views


urlpatterns = [
    path('depts', views.depts, name='depts'),
    path('deldept/<int:no>', views.del_dept, name='ddel'),
    path('depts/emps/<int:no>', views.emps, name='empsindept'),
    path('add', views.add, name='add')
]