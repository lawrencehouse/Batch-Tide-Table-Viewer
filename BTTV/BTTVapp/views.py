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

def region_detail(request, id):
    region = Region.objects.get(id=id)
    # template_name = f'BTTVapp/{region_name.lower().capitalize()}.html'
    # region_station = region.station_set.all
    stations = Station.objects.filter(region=region)
    context = {
        'stations': stations,
        # 'region_station': region_station
    }

    return render(request, 'BTTVapp/region.html', context)

def station_detail(request, id):
    station = Station.objects.get(id=id)
    context = {
        'station': station,
    }

    return render(request, 'BTTVapp/station.html', context)