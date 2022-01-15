from rest_framework.serializers import (
    ModelSerializer, IntegerField, CharField
)

from evslocator.models import EVCities, EVAreas


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
    def get_cities_by_state(cls, state):
        return EVCities.objects.filter(state_id=state).all()

    @classmethod
    def get_all_cities(cls):
        return EVCities.objects.all()


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
    def get_area(cls, area_id):
        return EVAreas.objects.get(area_id=area_id)

    @classmethod
    def get_area_by_state(cls, state):
        return EVAreas.objects.filter(state_id=state).all()

    @classmethod
    def get_area_by_state_and_city(cls, state, city):
        return EVAreas.objects.filter(state_id=state, city_id=city).all()

    @classmethod
    def get_all_area(cls):
        return EVAreas.objects.all()
