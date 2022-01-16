from rest_framework.views import APIView

from evslocator.serializer import EVStationInfoSerializer, EVStationSlotSerializer
from evslocator.utils import response_formatter


class EVStationInfoAPIView(APIView):
    def post(self, request, evs_id=None):
        if evs_id:
            ev_stations = []
            evs_obj = EVStationInfoSerializer.get_ev_station_info_by_id(evs_id)
            if evs_obj:
                ev_stations.append(evs_obj)
        else:
            ev_stations = EVStationInfoSerializer.get_filtered_ev_stations(
                state=request.data.get('state_id'),
                city=request.data.get('city_id'),
                area=request.data.get('area_code')
            )
        evs_slots = EVStationSlotSerializer.get_ev_station_slots_by_evs

        data = [
            EVStationInfoSerializer.prepare_ev_station_info(evs, evs_slots(evs.id)) for evs in ev_stations
        ]
        return response_formatter(200, "success", response=data)


