from rest_framework import serializers

from evslocator.models import EVStationsSlot



class SlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = EVStationsSlot
        fields = ('id')

    @classmethod
    def get_ev_station_by_id(cls, ev_station_id):
        return EVStationsSlot.objects.get(ev_stationId=ev_station_id)
