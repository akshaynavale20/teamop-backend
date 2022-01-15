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
                area=request.data.get('area_id')
            )
        ev_station_slots = EVStationSlotSerializer.get_ev_station_slots_by_evs

        data = []
        for ev_station in ev_stations:
            temp_ev_station = dict(
                evStationId=ev_station.id,
                evStationName=ev_station.ev_station_name,
                evStationAddress=ev_station.ev_address,
                rating=ev_station.rating,
                latitude=ev_station.latitude,
                longitude=ev_station.longitude,
                country=ev_station.country,
                state=ev_station.state,
                city=ev_station.city,
                areaCode=ev_station.area_code,
                phone=ev_station.phone,
                evStationSlots=[]
            )
            for ev_station_slot in ev_station_slots(ev_station.id):
                temp_ev_station['evStationSlots'].append(dict(
                    id=ev_station_slot.id,
                    isOccupied=ev_station_slot.is_occupied,
                    ChargesPerHour=ev_station_slot.charges_per_hour,
                    startHours=ev_station_slot.start_hours,
                    endHours=ev_station_slot.end_hours,
                    isAvailable24Hours=ev_station_slot.is_available_24_hours
                ))
            data.append(temp_ev_station)
        return response_formatter(200, "success", response=data)
