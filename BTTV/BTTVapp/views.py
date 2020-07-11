from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Station, Regions

# Create your views here.

def index(request):
    region_info = Regions.objects.all()
    context = {
        'regions': region_info,
    }

    return render(request,'BTTVapp\index.html', context)

def region_detail(request, region_name):
    template_name = f'BTTVapp/{region_name.lower().capitalize()}.html'

    return render(request, template_name)