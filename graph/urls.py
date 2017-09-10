from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.graph_list, name='graph_list'),
]