from django.conf.urls import url,include
from cmdb import views
urlpatterns = [
    url(r'^login', views.login),
url(r'^orm/', views.orm),
url(r'^index/', views.index),
url(r'^user_info/', views.user_info),
url(r'^userdetail-(?P<nid>\d+)/', views.user_detail),
url(r'^userdel-(?P<nid>\d+)/', views.user_del),
url(r'^useredit-(?P<nid>\d+)/', views.user_edit),
]
