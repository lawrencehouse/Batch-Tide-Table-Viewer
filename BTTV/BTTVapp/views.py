from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Station, Region

# Create your views here.

def index(request):
    region_info = Region.objects.all()
    context = {
        'regions': region_info,
    }

    return render(request,'BTTVapp\index.html', context)

def region_detail(request, region_path_name):
    region = Region.objects.get(path_name=region_path_name)
    # template_name = f'BTTVapp/{region_name.lower().capitalize()}.html'
    region_station = region.station_set.all
    context = {
        'region': region,
        'region_station': region_station
    }

    return render(request, 'BTTVapp/region.html', context)

def station_detail(request, station_path_name):
    station = Station.objects.get(station_id=station_path_name)
    context = {
        'station': station,
    }

    return render(request, 'BTTVapp/station.html', context)