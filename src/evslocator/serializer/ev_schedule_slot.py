from rest_framework.serializers import (
    ModelSerializer, IntegerField, CharField, DateTimeField,
    RelatedField
)

from evslocator.models import EVScheduleSlot
from evslocator.serializer import CustomerSerializer


class EVScheduleSlotSerializer(ModelSerializer):
    id = IntegerField(read_only=True, required=False)
    customer = CustomerSerializer(many=True)
    ev_station = RelatedField(many=True)
    free_from = DateTimeField(required=True, allow_null=False)
    free_to = DateTimeField(required=True, allow_null=False)
    payment_mode = CharField()
    created_at = DateTimeField(read_only=True, required=False)

    class Meta:
        model = EVScheduleSlot
        field = (
            'id',
            'user',
            'ev_station',
            'free_from',
            'free_to',
            'payment_mode',
            'created_at'
        )
