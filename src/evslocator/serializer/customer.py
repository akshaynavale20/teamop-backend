from rest_framework.serializers import (
    ModelSerializer, IntegerField, CharField, EmailField
)

from evslocator.models import Customer


class CustomerSerializer(ModelSerializer):
    id = IntegerField(read_only=True, required=False)
    user_name = CharField(required=True, allow_null=False)
    first_name = CharField(required=True, allow_null=False)
    last_name = CharField(required=True, allow_null=False)
    display_name = CharField(required=False, allow_null=True)
    email = EmailField(required=True, allow_null=False)
    phone = CharField(required=True, allow_null=False)
    role = CharField(required=True, allow_null=False)

    class Meta:
        model = Customer
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'display_name',
            'email',
            'phone',
            'role'
        )

    @classmethod
    def get_customer_by_id(cls, customer_id):
        return Customer.objects.get(id=customer_id, is_delete=False)
