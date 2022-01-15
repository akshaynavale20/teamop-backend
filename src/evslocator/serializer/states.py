from rest_framework import serializers

from evslocator.models import EVStates


class StatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EVStates
        fields = ('state_id', 'state_name')

    @classmethod
    def get_states(cls):
        return EVStates.objects.all()
