from django.db import models


class Vehicle(models.Model):
    # id is automatically created as PK
    plate = models.CharField(max_length=20, verbose_name="plate")

    def __str__(self):
        return self.plate


class NavigationRecord(models.Model):
    # id is automatically created as PK
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='vehicle', editable=True, verbose_name="plate")
    latitude = models.FloatField(default=0, verbose_name="latitude")
    longitude = models.FloatField(default=0, verbose_name="longitude")
    datetime = models.DateTimeField(auto_now_add=True, verbose_name="datetime", editable=False)

    def __str__(self):
        return str(self.datetime)
