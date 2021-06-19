from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import NavigationRecord, Vehicle


class NavigationRecordListSerializer(ModelSerializer):
    vehicle_plate = serializers.ReadOnlyField(source='vehicle.plate')

    class Meta:
        model = NavigationRecord
        fields = ('vehicle_plate', 'latitude', 'longitude', 'datetime')
