from rest_framework.views import APIView

from evslocator.serializer import (
    EVScheduleSlotSerializer,
    EVStationInfoSerializer,
    EVStationSlotSerializer,
    CustomerSerializer
)
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_201_CREATED
from evslocator.utils import response_formatter, combine_date_and_time


class EVScheduleSlotAPIView(APIView):
    def get(self, request):
        ev_station_id = request.data['evStationId']
        free_from = request.data['freeFrom']
        free_to = request.data['freeTo']

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
        available_evs_info = [evs for evs in ev_station_slots if evs.id in available_evs_slots_ids]

        return response_formatter(
            status_code=HTTP_200_OK,
            message='Success!',
            response=dict(
                available_evs_slots_info=[
                    evs.prepare_ev_station_info(evs) for evs in available_evs_info
                ]
            )
        )

    def post(self, request):
        customer = request.data['customerId']
        evs_slot_id = request.data['evsSlotId']
        schedule_date = request.data['scheduleDate']
        free_from = combine_date_and_time(schedule_date, request.data['freeFrom'])
        free_to = combine_date_and_time(schedule_date, request.data['freeTo'])

        customer_obj = CustomerSerializer.get_customer_by_id(customer)
        if not customer_obj:
            # TODO: raise error
            pass

        evs_slot = EVStationSlotSerializer.get_evs_slot_by_id(evs_slot_id)
        if not evs_slot:
            # TODO: raise error
            pass

        evs_schedule = EVScheduleSlotSerializer.create_schedule(**dict(
            customer=customer_obj.id,
            ev_station_slot=evs_slot.id,
            free_from=free_from,
            free_to=free_to
        ))

        return response_formatter(
            status_code=HTTP_201_CREATED,
            message="created.!",
            response=dict(
                customer=customer_obj.display_name,
                customer_id=customer_obj.id,
                ev_station_slot_id=evs_slot.id,
                free_from=free_from,
                free_to=free_to,
                evs_schedule_slot_id=evs_schedule.id,
            )
        )


