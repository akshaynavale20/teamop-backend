from rest_framework.views import APIView

from evslocator.serializer import EVStationInfoSerializer
from evslocator.utils import response_formatter


class EVStationInfoAPIView(APIView):
    def get(self, request):
        pass