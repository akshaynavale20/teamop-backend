from django.db import models


class BaseClass(models.Model):
    id = models.IntegerField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


# Create your models here.
class Customer(BaseClass):
    user_name = models.CharField(unique=True, max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    display_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(unique=True, max_length=255)
    phone = models.CharField(max_length=255, blank=True, null=True)
    role = models.CharField(max_length=255, blank=True, null=True)

    objects = models.Manager()

    class Meta:
        db_table = "customer"


class EVStationInfo(BaseClass):
    ev_station_name = models.CharField(max_length=255)
    ev_address = models.CharField(max_length=255)
    rating = models.SmallIntegerField(default=0)
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)

    objects = models.Manager()

    class Meta:
        db_table = "ev_station_info"


class EVStationsSlot(BaseClass):
    ev_station = models.ForeignKey(EVStationInfo, on_delete=models.CASCADE)
    is_occupied = models.BooleanField(default=True)
    charges_per_hour = models.FloatField(default=0)
    start_hours = models.TimeField(blank=True, editable=True, null=True)
    end_hours = models.TimeField(blank=True, editable=True, null=True)
    is_available_24_hours = models.BooleanField(default=True)

    objects = models.Manager()

    class Meta:
        db_table = "ev_station_slot"


class EVScheduleSlot(BaseClass):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    ev_station_slot = models.ForeignKey(EVStationsSlot, on_delete=models.CASCADE)
    free_from = models.DateTimeField(auto_now_add=True, editable=True)
    free_to = models.DateTimeField(editable=True)
    payment_mode = models.CharField(max_length=255)

    objects = models.Manager()

    class Meta:
        db_table = "ev_schedule_slot"


class EVStates(BaseClass):
    state_id = models.IntegerField()
    state_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = "states"


class EVCities(BaseClass):
    city_id = models.IntegerField()
    state_id = models.IntegerField()
    city_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = "cities"


class EVAreas(BaseClass):
    city_id = models.IntegerField()
    state_id = models.IntegerField()
    area_id = models.IntegerField()
    area_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = "area"
