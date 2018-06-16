from django.conf.urls import url, include

from rango import views

urlpatterns = [
    url('^$', views.rango_index, name='rango_index'),
    url('^add_category/$', views.add_category, name='add_category'),
    url(r'^(?P<category_name_slug>[\w-]+)/$', views.show_category, name='show_category'),
]