from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    re_path(r'^about/', views.about, name='about'),
    re_path(r'^data/', views.db_operations, name='db_operations'),
    re_path(r'^present/', views.data_visualization, name='data_visualization'),
]