import datetime

from django.conf import settings
from django.db import models


class BaseClass(models.Model):
    id = models.IntegerField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        abstract = True


# Create your models here.
class Customer(BaseClass):
    username = models.CharField(unique=True, max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    display_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(unique=True, max_length=255)
    phone = models.CharField(max_length=255, blank=True, null=True)
    role = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = settings.MANAGE_TABLES
        db_table = "customer"


class EVStationInfo(BaseClass):
    ev_station_name = models.CharField(max_length=255)
    ev_address = models.CharField(max_length=255)
    ev_pricing = models.FloatField(default=0)
    rating = models.SmallIntegerField(default=0)
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    area_code = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    class Meta:
        managed = settings.MANAGE_TABLES
        db_table = "ev_station_info"


class EVScheduleSlot(BaseClass):
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)
    ev_station = models.ForeignKey(EVStationInfo, on_delete=models.CASCADE)
    free_from = models.DateTimeField(auto_now_add=True, editable=True)
    free_to = models.DateTimeField(default=datetime.datetime.utcnow() + datetime.timedelta(hours=1), editable=True)
    payment_mode = models.CharField(max_length=255)

    class Meta:
        managed = settings.MANAGE_TABLES
        db_table = "ev_schedule_slot"


class EVStationsSlot(BaseClass):
    # ev_station = models.ForeignKey(EVStationInfo, on_delete=models.CASCADE)
    is_free = models.BooleanField(default=True)
    charges_per_hour = models.FloatField(default=0)
    start_hours = models.TimeField()
    end_hours = models.TimeField()
    available_24_hour = models.BooleanField(default=True)
    free_from = models.DateTimeField(auto_now_add=True, editable=True)
    free_until = models.DateTimeField(default=datetime.datetime.utcnow() + datetime.timedelta(hours=1), editable=True)
    ev_stationId = models.IntegerField()
    class Meta:
        managed = settings.MANAGE_TABLES
        db_table = "ev_station_slot"


class EVStates(BaseClass):
    state_id = models.IntegerField()
    state_name = models.CharField(max_length=255)
    class Meta:
        managed = settings.MANAGE_TABLES
        db_table = "states"

