from django.urls import path
from . import views

app_name = 'BTTVapp'
urlpatterns = [
  path('', views.index, name='index'),
  path('<str:region_path_name>/', views.region_detail, name='region_detail'),
  path('<str:station_path_name>/', views.station_detail, name='station_detail'),
]