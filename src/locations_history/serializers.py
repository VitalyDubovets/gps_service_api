from rest_framework import serializers

from .models import LocationHistory


__all__ = [
    'LocationHistorySerializer',
]


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
