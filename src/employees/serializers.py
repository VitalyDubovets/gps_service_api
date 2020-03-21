from rest_framework import serializers

from employees.models import Employee


__all__ = [
    'EmployeeSerializer',
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
