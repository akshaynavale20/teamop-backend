from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from evslocator.serializer import EVCitiesSerializer, EVCityAreaSerializer, StatesSerializer
from evslocator.utils import response_formatter


class EVStatesAPIView(APIView):

    def get(self, request):
        states_obj = StatesSerializer.get_states()
        if not states_obj:
            return response_formatter(HTTP_400_BAD_REQUEST, "Something went wrong.")
        return self._prepare_response(states_obj)

    def _prepare_response(self, states):
        return response_formatter(
            status_code='200',
            message="Success!",
            response={'states': [{
                'state_name': state.state_name,
                'state_id': state.state_id
            } for state in states]}
        )


class EVCitiesAPIView(APIView):

    def get(self, request, state_id=None):
        if state_id:
            cities = EVCitiesSerializer.get_cities_by_state(state=state_id)
        else:
            cities = EVCitiesSerializer.get_all_cities()
        if not cities:
            return response_formatter(HTTP_400_BAD_REQUEST, "Something went wrong.")
        return self._prepare_response(cities)

    def _prepare_response(self, cities):
        return response_formatter(
            status_code='200',
            message="Success!",
            response={'cities': [{
                'city_name': city.city_name,
                'state_id': city.state_id,
                'city_id': city.city_id
            } for city in cities]}
        )


class EVAreasAPIView(APIView):

    def get(self, request, state=None, city=None):
        if state and city:
            areas = EVCityAreaSerializer.get_area_by_state_and_city(state, city)
        elif state and not city:
            areas = EVCityAreaSerializer.get_area_by_state(state)
        else:
            areas = EVCityAreaSerializer.get_all_area()

        if not areas:
            return response_formatter(HTTP_400_BAD_REQUEST, "Something went wrong.")
        return self._prepare_response(areas)

    def _prepare_response(self, areas):
        return response_formatter(
            status_code='200',
            message="Success!",
            response={'areas': [{
                'area_name': area.area_name,
                'state_id': area.state_id,
                'city_id': area.city_id,
                'area_id': area.area_id
            } for area in areas]}
        )
