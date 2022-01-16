from rest_framework.views import APIView
from evslocator.serializer import (
    EVScheduleSlotSerializer,
    EVStationInfoSerializer,
    EVStationSlotSerializer,
    CustomerSerializer
)
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_201_CREATED
from evslocator.utils import response_formatter, combine_date_and_time


class EVGetSlotsAPI(APIView):
    def post(self, request):
        ev_station_id = request.data['evStationId']
        free_from = request.data['date']
        free_to = request.data['date']

        # get EV Station
        ev_station = EVStationInfoSerializer.get_ev_station_info_by_id(ev_station_id)
        if not ev_station:
            return response_formatter(
                status_code=HTTP_400_BAD_REQUEST,
                message='Please select valid EV Station.'
            )

        # get EV Station Slots
        ev_station_slots = EVStationSlotSerializer.get_ev_station_slots_by_evs(ev_station_id=ev_station.id)
        if not ev_station_slots:
            return response_formatter(
                status_code=HTTP_400_BAD_REQUEST,
                message=f'No available slots found for the EV Station {ev_station.ev_station_name}.'
            )
        evs_slot_ids = set(evs_slot.id for evs_slot in ev_station_slots)

        # check availability of the EV Station Slots by checking any scheduled slots between same time slot.
        scheduled_slots = EVScheduleSlotSerializer.check_evs_schedule_availability_for_slot(
            evs_slot_ids,
            free_from,
            free_to
        )
        scheduled_evs_slot_ids = set(scheduled_slot.ev_station_slot.id for scheduled_slot in scheduled_slots)
        available_evs_slots_ids = evs_slot_ids.difference(scheduled_evs_slot_ids)
        if not available_evs_slots_ids:
            return response_formatter(
                status_code=HTTP_400_BAD_REQUEST,
                message=f'No available slots found for the EV Station {ev_station.ev_station_name}.'
            )

        # Available EVS Slots * EVS Info
        available_evs_slots = [evs for evs in ev_station_slots if evs.id in available_evs_slots_ids]
        available_evs_slots_info = EVStationInfoSerializer.prepare_ev_station_info(ev_station, available_evs_slots)
        return response_formatter(
            status_code=HTTP_200_OK,
            message='Success!',
            response=dict(
                available_evs_slots_info=available_evs_slots_info
            )
        )

    

