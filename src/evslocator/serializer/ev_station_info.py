from rest_framework.serializers import (
    ModelSerializer, IntegerField, CharField
)

from evslocator.models import EVStationInfo


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
    area = CharField(required=True, allow_null=False)
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
            'area',
            'phone'
        )

    @classmethod
    def get_ev_station_info_by_id(cls, ev_station_id):
        return EVStationInfo.objects.get(id=ev_station_id)

    @classmethod
    def get_ev_station_all(cls):
        return EVStationInfo.objects.all()

    @classmethod
    def get_filtered_ev_stations(cls, state, city, area):
        ev_station_qs = EVStationInfo.objects
        if state:
            ev_station_qs.filter(state=state)
        if city:
            ev_station_qs.filter(city=city)
        if area:
            ev_station_qs.filter(area_code=area)
        return ev_station_qs.all()

    @classmethod
    def prepare_ev_station_info(cls, ev_station, evs_slots):
        temp_evs_info = dict(
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

        for evs_slot in evs_slots:
            temp_evs_info['evStationSlots'].append(dict(
                id=evs_slot.id,
                isOccupied=evs_slot.is_occupied,
                ChargesPerHour=evs_slot.charges_per_hour,
                startHours=evs_slot.start_hours,
                endHours=evs_slot.end_hours,
                isAvailable24Hours=evs_slot.is_available_24_hours
            ))
        return temp_evs_info

