from django.apps import AppConfig


class EvslocatorConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'evslocator'


class SetupConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'setup'
