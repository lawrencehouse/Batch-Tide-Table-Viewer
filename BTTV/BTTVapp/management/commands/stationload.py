from django.core.management.base import BaseCommand
from BTTVapp.models import Station, Regions
import json
import requests
    
class Command(BaseCommand):
    def handle(self, *args, **options):
        Station.objects.all().delete()
        with open('stationswaterlevels.json', 'r') as file:
            text = file.read()
            data = json.loads(text)

            for info in data['stations']:
                state_id = info['state']
                station_id = int(info['id'])
                location_name = info['name']                

                add_station = Station(
                    state_id=state_id,
                    station_id=station_id,
                    location_name=location_name,
                )
                add_station.save()                   
            # print(info)