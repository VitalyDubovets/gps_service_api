from rest_framework import serializers

from employees.models import Employee
from locations_history.serializers import LocationHistorySerializer


__all__ = [
    'EmployeeSerializer',
    'EmployeeLastLocationSerializer'
]


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            'id',
            'first_name',
            'second_name',
            'last_name',
            'sex',
            'birth_date',
        ]


class EmployeeLastLocationSerializer(serializers.ModelSerializer):
    last_location = LocationHistorySerializer()

    class Meta:
        model = Employee
        fields = [
            'id',
            'first_name',
            'second_name',
            'last_name',
            'last_location',
        ]
