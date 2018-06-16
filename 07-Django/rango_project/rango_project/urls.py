"""rango_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.staticfiles.urls import static

from rango_project.settings import MEDIA_URL, MEDIA_ROOT

from rango import views

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'api/all_category', views.api_all_category)


urlpatterns = [
    url(r'^$', views.index, name='base_bootstrap'),
    url(r'^admin/', admin.site.urls),
    url(r'^rango/', include('rango.urls', namespace='rango')),
    url(r'^user/', include('user.urls', namespace='user')),
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)

urlpatterns += router.urls


