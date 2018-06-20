from django.conf.urls import url

from dept import views

urlpatterns = [
    url(r'^depts$', views.depts, name='depts'),
    url(r'^del_dept$', views.del_dept, name='del_dept'),
    url(r'^depts/emps/(?P<no>[0-9]+)$', views.emps, name='empsindept'),
    url(r'^add$', views.add, name='add')
]
