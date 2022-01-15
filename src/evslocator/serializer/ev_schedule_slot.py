from django.db.models import Q
from rest_framework.serializers import (
    ModelSerializer, IntegerField, CharField, DateTimeField
)

from evslocator.models import EVScheduleSlot
from evslocator.serializer import CustomerSerializer, EVStationSlotSerializer


class EVScheduleSlotSerializer(ModelSerializer):
    id = IntegerField(read_only=True, required=False)
    customer = CustomerSerializer(many=True)
    ev_station_slot = EVStationSlotSerializer(many=True)
    free_from = DateTimeField(required=True, allow_null=False)
    free_to = DateTimeField(required=True, allow_null=False)
    payment_mode = CharField()
    created_at = DateTimeField(read_only=True, required=False)

    class Meta:
        model = EVScheduleSlot
        field = (
            'id',
            'user',
            'ev_station_slot',
            'free_from',
            'free_to',
            'payment_mode',
            'created_at'
        )

    @classmethod
    def check_evs_schedule_availability_for_slot(cls, ev_station_ids, from_slot, to_slot):
        qs = Q(ev_station__id__in=ev_station_ids)
        qs.add(Q(is_deleted=False), Q.AND)
        qs.add(Q(free_from__gte=from_slot), Q.AND)
        qs.add(Q(free_to__lte=to_slot), Q.OR)
        return EVScheduleSlot.objects.filter(qs).all()

    @classmethod
    def create_schedule(cls, **create_data):
        return EVScheduleSlot.objects.create(**create_data)
