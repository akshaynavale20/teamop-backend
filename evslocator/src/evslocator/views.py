
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from evslocator.models import EVScheduleSlot
from evslocator.serializer.slots import SlotSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
def index(self,request):
    return HttpResponse("Hello, Welcome to EVS Locator")

class EVSlots(APIView): 

    def post(self, request):
        requested_data = request.data  
        wallet_obj = SlotSerializer.get_ev_station_by_id(ev_station_id=requested_data.get('ev_station_id'))
        if not wallet_obj:
            return response_formatter(HTTP_400_BAD_REQUEST, "Something went wrong.")
        return self._prepare_response(requested_data['ev_station_id'], wallet_obj)
        
    def _prepare_response(self, ev_station_id, slots):
        return Response(dict(
            status='success',
            data=dict(slots=dict(
                ev_station_id=ev_station_id,
                is_free = slots.is_free,
                charges_per_hour=slots.charges_per_hour,
                free_from=slots.free_from,
                free_until=slots.free_until,
                start_hours = slots.start_hours,
                end_hours = slots.end_hours,
                available_24_hour = slots.available_24_hour
            ))
        ))