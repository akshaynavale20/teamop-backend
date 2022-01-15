
from rest_framework.serializers import  (
    ModelSerializer, IntegerField, BooleanField, CharField
)
from src.evslocator.models import EVStationInfo


class EVStationInfoSerializer(ModelSerializer):
    id = IntegerField(read_only=True, required=False)
    ev_station_name = CharField(required=True, allow_null=False)
    ev_address = CharField(required=True, allow_null=False)
    rating = IntegerField(required=True, max_value=10, min_value=1)
    latitude = CharField(required=True, allow_null=False)
    longitude = CharField(required=True, allow_null=False)
    country = CharField(required=True, allow_null=False)
    state = CharField(required=True, allow_null=False)
    city = CharField(required=True, allow_null=False)
    area_code = CharField(required=True, allow_null=False)
    phone = CharField(required=True, allow_null=False)
    
    class Meta:
        model = EVStationInfo
        fields = (
            'id',
            'ev_station_name',
            'ev_address',
            'rating',
            'latitude',
            'longitude',
            'country',
            'state',
            'city',
            'area_code',
            'phone'
        )



