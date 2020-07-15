from django.urls import path
from . import views

app_name = 'BTTVapp'
urlpatterns = [
  path('', views.index, name='index'),
  path('region/<int:id>/', views.region_detail, name='region_detail'),
  path('stations/<int:id>/', views.station_detail, name='station_detail'),
]