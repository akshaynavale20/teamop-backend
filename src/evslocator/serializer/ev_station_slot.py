from rest_framework.serializers import (
    ModelSerializer, IntegerField, TimeField, BooleanField,
    FloatField
)

from evslocator.models import EVStationsSlot
from evslocator.serializer import EVStationInfoSerializer


class EVStationSlotSerializer(ModelSerializer):
    id = IntegerField(read_only=True, required=False)
    ev_station = EVStationInfoSerializer()
    is_occupied = BooleanField(default=False, required=False, allow_null=False)
    charges_per_hour = FloatField(required=True, allow_null=False)
    start_hours = TimeField(required=False, allow_null=True)
    end_hours = TimeField(required=False, allow_null=True)
    is_available_24_hours = BooleanField(default=True, required=False, allow_null=False)

    class Meta:
        model = EVStationsSlot
        fields = (
            'id',
            'ev_station',
            'is_occupied',
            'charges_per_hour',
            'start_hours',
            'end_hours',
            'is_available_24_hours'
        )

    @classmethod
    def get_ev_station_slots_by_evs(cls, ev_station_id):
        return EVStationsSlot.objects.filter(
            ev_station__id=ev_station_id,
            ev_station__is_deleted=False
        ).all()

    @classmethod
    def get_evs_slot_by_id(cls, evs_slot_id):
        return EVStationsSlot.objects.filter(
            id=evs_slot_id,
            is_deleted=False,
            ev_station__is_deleted=False
        ).select_related('ev_station')

