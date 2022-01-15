from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from evslocator.serializer.ev_station_slot import EVStationSlotSerializer
from evslocator.serializer.states import StatesSerializer
from .utils import response_formatter


# Create your views here.
def index(self, request):
    return HttpResponse("Hello, Welcome to EVS Locator")


class EVSlots(APIView):

    def post(self, request):
        requested_data = request.data
        ev_station_slots = EVStationSlotSerializer.get_ev_station_by_id(
            ev_station_id=requested_data.get('ev_station_id'))
        if not ev_station_slots:
            return response_formatter(HTTP_400_BAD_REQUEST, "EV Station has no slot.")
        return self._prepare_response(requested_data['ev_station_id'], ev_station_slots)

    def _prepare_response(self, ev_station_id, slots):
        return Response(dict(
            status='success',
            data=dict(slots=dict(
                ev_station_id=ev_station_id,
                is_free=slots.is_free,
                charges_per_hour=slots.charges_per_hour,
                free_from=slots.free_from,
                free_until=slots.free_until,
                start_hours=slots.start_hours,
                end_hours=slots.end_hours,
                available_24_hour=slots.available_24_hour
            ))
        ))


class EVStates(APIView):

    def get(self, request):
        states_obj = StatesSerializer.get_states()
        if not states_obj:
            return response_formatter(HTTP_400_BAD_REQUEST, "Something went wrong.")
        return self._prepare_response(states_obj)

    def _prepare_response(self, states):
        return response_formatter(
            status_code='200',
            message="Success!",
            response={'states': [{
                'state_name': state.state_name,
                'state_id': state.state_id
            } for state in states]}
        )
