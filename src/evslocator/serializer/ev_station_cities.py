from rest_framework.serializers import (
    ModelSerializer, IntegerField, CharField, DateTimeField,
    RelatedField
)

from evslocator.models import EVCities,EVAreas


class EVCitiesSerializer(ModelSerializer):
    state_id = IntegerField(read_only=True, required=False)
    city_id = IntegerField(read_only=True, required=False)
    city_name = CharField(max_length=255)
    class Meta:
        model = EVCities
        field = (
            'state_id',
            'city_id',
            'city_name'
        )
    @classmethod
    def get_cities(cls, state_id):
        return EVCities.objects.filter(state_id=state_id)

class EVCityAreaSerializer(ModelSerializer):
    state_id = IntegerField(read_only=True, required=False)
    city_id = IntegerField(read_only=True, required=False)
    area_id = CharField(max_length=255)
    area_name = IntegerField(read_only=True, required=False)
    class Meta:
        model = EVAreas
        field = (
            'state_id',
            'city_id',
            'area_name',
            'area_id',
        )
    @classmethod
    def get_area(cls, state_id,city_id):
        return EVAreas.objects.filter(city_id=city_id,state_id=state_id)
