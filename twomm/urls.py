"""twomm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.conf.urls import url,include
from cmdb import views
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^cmdb/', include("cmdb.urls")),
]




# urlpatterns = [
#     path('admin/', admin.site.urls),
#     # path('indexjjjjjjj/(\d+)/', views.index,name='indexxx'),
#     path('login', views.login),
#     path('home', views.Home.as_view()),
#     # path('detail/', views.detail),
# # path(r'detail-(\d+).html/', views.detail),
# # url(r'^detail-(\d+)-(\d+).html', views.detail),
# url(r'^detail-(?P<nid>\d+).html', views.detail),
# # url(r'^detail-(?P<nid>\d+).html', views.detail,name='indexx'),
# url(r'^indexjjjjjjj/(d+)', views.index,name='indexxx'),
# ]
