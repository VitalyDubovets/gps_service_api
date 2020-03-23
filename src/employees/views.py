from django.db.models import Prefetch
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from employees.models import Employee
from employees.serializers import EmployeeSerializer, EmployeeLastLocationSerializer
from locations_history.models import LocationHistory


__all__ = [
    'EmployeeViewSet',
    'EmployeesLastLocationView',
]


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    Endpoint для получения, удаление, изменения работника
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.AllowAny]


class EmployeesLastLocationView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request, *args, **kwargs):
        employees = Employee.objects.all().prefetch_related(
            Prefetch('locations', LocationHistory.objects.all().order_by('-date_of_stay'))
        )
        for employee in employees:
            setattr(employee, 'last_location', employee.locations.all().first())
        serializer = EmployeeLastLocationSerializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
