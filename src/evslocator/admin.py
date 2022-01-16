from django.contrib import admin

# Register your models here.

from evslocator.models import (
    Customer,
    EVStationInfo, EVScheduleSlot, EVStationsSlot
)


class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'created_at', 'modified_at', 'is_deleted',
        'user_name', 'first_name', 'last_name', 'display_name',
        'password', 'email', 'role'

    )
    search_fields = ('id', 'user_name', 'first_name', 'last_name', 'email', 'phone', 'role')


class EVStationInfoAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'created_at', 'modified_at', 'is_deleted',
        'ev_station_name', 'ev_address', 'rating',
        'latitude', 'longitude', 'country',
        'state', 'city', 'area_code', 'phone'
    )

    search_fields = ('id', 'state', 'city', 'country', 'area', 'phone', 'ev_address', 'ev_station_name')


class EVScheduleSlotAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'created_at', 'modified_at', 'is_deleted',
        'customer_id', 'ev_station_slot_id', 'free_from', 'free_to', 'payment_mode',
    )

    search_fields = (
        'id', 'customer_id', 'ev_station_slot_id', 'free_from', 'free_to', 'payment_mode',
    )


class EVStationSlotAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'created_at', 'modified_at', 'is_deleted',
        'ev_station', 'is_occupied', 'charges_per_hour', 'start_hours', 'end_hours'
    )
    search_fields = ('id', 'ev_station', 'is_occupied', 'charges_per_hour', 'start_hours', 'end_hours')


admin.site.register(Customer, CustomerAdmin)
admin.site.register(EVStationInfo, EVStationInfoAdmin)
admin.site.register(EVStationsSlot, EVStationSlotAdmin)
admin.site.register(EVScheduleSlot, EVScheduleSlotAdmin)


admin.site.site_header = "EVS Locator"
