from django.urls import path

from hrs import views


urlpatterns = [
    path('depts', views.depts, name='depts'),
    path('depts/emps/<int:no>', views.emps, name='empsindept'),  # 访问hrs/depts  给视图为 depts
    path('allemps', views.AllEmps, name='allemps'),
    path('deldept/<int:no>', views.del_dept, name='ddel')
]