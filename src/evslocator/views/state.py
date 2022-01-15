from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from evslocator.serializer.states import StatesSerializer
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
