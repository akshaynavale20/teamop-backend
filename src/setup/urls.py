"""setup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from evslocator.views import (
    EVStationInfoAPIView, EVStatesAPIView, EVSlotsAPIView,
    index, EVCitiesAPIView, EVAreasAPIView, EVScheduleSlotAPIView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/evslocator/slots/', EVSlotsAPIView.as_view(), name='Slots'),

    path('health/', index, name='index'),
    path('v1/evslocator/evstation/info', EVStationInfoAPIView.as_view(), name='ev-station-info'),

    # get state
    path('v1/evslocator/state', EVStatesAPIView.as_view(), name='get-all-state'),

    # get city
    path('v1/evslocator/state/city', EVCitiesAPIView.as_view(), name='get-all-cities'),
    path('v1/evslocator/state/<state_id>/city', EVCitiesAPIView.as_view(), name='get-cities-by-state'),

    # get area
    path('v1/evslocator/state/city/area', EVAreasAPIView.as_view(), name='get-all-area'),
    path(
        'v1/evslocator/state/<state>/city/<city>/area',
        EVAreasAPIView.as_view(),
        name='get-all-area-by-state-and-city'
    ),
    path(
        'v1/evslocator/state/<state>/city/area',
        EVAreasAPIView.as_view(),
        name='get-all-area-by-state'
    ),

    path('v1/evslocator/evs/info/', EVStationInfoAPIView.as_view(), name='get-all-filtered-evs'),
    path('v1/evslocator/evs/info/<evs_id>', EVStationInfoAPIView.as_view(), name='get-evs'),
    path('v1/evslocator/evs/slot/schedule', EVScheduleSlotAPIView.as_view(), name='schedule-evs-slot')
]
