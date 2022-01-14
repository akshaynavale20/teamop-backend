from django.db import models

from django.conf import settings


# Create your models here.
class User(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255, blank=True, null=True)
    inactive_flag = models.SmallIntegerField(blank=True, null=True, default=0)
    display_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(
        unique=True, max_length=255, blank=True, null=True
    )
    phone = models.CharField(max_length=255, blank=True, null=True)
    role = models.CharField(max_length=255, blank=True, null=True)

    date_created = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = settings.MANAGE_TABLES
        db_table = "analyst_usr"

