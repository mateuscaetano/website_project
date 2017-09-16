from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^graph/', views.graph_list, name='graph_list'),
    url(r'^simple/', views.simple, name='simple'),
    url(r'^tableau/', views.tableau, name='tableau'),
]