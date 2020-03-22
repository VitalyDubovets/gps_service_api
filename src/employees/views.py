from rest_framework import permissions
from rest_framework import viewsets

from employees.models import Employee
from employees.serializers import EmployeeSerializer


__all__ = [
    'EmployeeViewSet',
]


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    Endpoint для получения, удаление, изменения работника
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.AllowAny]
