from datetime import datetime

from rest_framework import serializers

from .models import LocationHistory


__all__ = [
    'LocationHistorySerializer',
    'GeneratorDataSerializer',
]


class GeneratorDataSerializer(serializers.Serializer):
    employee_id = serializers.IntegerField(required=True)
    starts_date = serializers.DateTimeField(required=True)
    end_date = serializers.DateTimeField(required=True)
    latitude = serializers.FloatField(max_value=90.0, min_value=-90.0)
    longitude = serializers.FloatField(max_value=180.0, min_value=-180.0)


class LocationHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationHistory
        fields = [
            'id',
            'employee',
            'latitude',
            'longitude',
            'date_of_stay',
        ]
