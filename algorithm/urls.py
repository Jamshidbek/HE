from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.algorithm_list, name='algorithm_list'),
    url(r'^rsa/$', views.rsa_view, name='rsa'),
    url(r'^rsa/(?P<pk>\d+)/$', views.rsa_result, name='rsa_result'),
]