from django.urls import path
from . import views

app_name = 'BTTVapp'
urlpatterns = [
  path('', views.index, name='index'),
]