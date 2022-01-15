from rest_framework.views import APIView

from evslocator.serializer import (
    EVScheduleSlotSerializer,
    EVStationInfoSerializer,
    EVStationSlotSerializer
)
from evslocator.utils import response_formatter


class EVScheduleSlotAPIView(APIView):
    def post(self, request):
        ev_station_id = request.data['evStationId']
        free_from = request.data['freeFrom']
        free_to = request.data['freeTo']

        ev_station = EVStationInfoSerializer.get_ev_station_info_by_id(ev_station_id)
        if not ev_station:
            # TODO: raise error
            pass

        ev_station_slots = EVStationSlotSerializer.get_ev_station_slots_by_evs(ev_station_id=ev_station.id)
        if not ev_station_slots:
            # TODO: raise error
            pass
        evs_slot_ids = set(evs_slot.id for evs_slot in ev_station_slots)

        scheduled_slots = EVScheduleSlotSerializer.check_evs_schedule_availability_for_slot(
            evs_slot_ids,
            free_from,
            free_to
        )
        scheduled_evs_slot_ids = set(scheduled_slot.ev_station_slot.id for scheduled_slot in scheduled_slots)
        available_evs_slots_ids = evs_slot_ids.difference(scheduled_evs_slot_ids)
        available_evs_info = [evs for evs in ev_station_slots if evs.id in available_evs_slots_ids]

        return response_formatter(
            status_code=200,
            message='Success!',
            response=dict(
                available_evs_slots_info=[
                    evs.prepare_ev_station_info(evs) for evs in available_evs_info
                ]
            )
        )