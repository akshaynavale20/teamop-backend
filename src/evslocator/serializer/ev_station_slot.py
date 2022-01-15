from rest_framework.serializers import (
    ModelSerializer, IntegerField, CharField, TimeField, BooleanField,
    RelatedField, FloatField
)

from src.evslocator.models import EVStationsSlot


class EVStationSlotSerializer(ModelSerializer):
    id = IntegerField(read_only=True, required=False)
    ev_station = RelatedField(many=True)
    is_occupied = BooleanField(default=False, required=False, allow_null=False)
    charges_per_hour = FloatField(default=0, required=True, allow_null=False)
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
    def get_ev_station_by_id(cls, ev_station_id):
        return EVStationsSlot.objects.get(ev_station__id=ev_station_id)
