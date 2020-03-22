from datetime import datetime
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .filters import LocationHistoryFilter
from .models import LocationHistory
from .serializers import *
from .services import ServiceTestData


__all__ = [
    'LocationHistoryViewSet',
    'GeneratorTestDataView',
]


class LocationHistoryViewSet(viewsets.ModelViewSet):
    """
    Endpoint для создания и получения историй перемещений сотрудников/работников
    """
    queryset = LocationHistory.objects.all()
    serializer_class = LocationHistorySerializer
    permission_classes = [permissions.AllowAny]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = LocationHistoryFilter

    def create(self, request, *args, **kwargs):
        if isinstance(request.data, list):
            serializer = self.get_serializer(data=request.data, many=True)
        else:
            serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class GeneratorTestDataView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        service = ServiceTestData()
        serializer = GeneratorDataSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            starts_date = datetime.strptime(serializer.data['starts_date'], "%Y-%m-%dT%H:%M:%SZ")
            end_date = datetime.strptime(serializer.data['end_date'], "%Y-%m-%dT%H:%M:%SZ")
            data = service.form_test_data(
                serializer.data['employee_id'],
                starts_date,
                end_date,
                latitude=serializer.data['latitude'],
                longitude=serializer.data['longitude']
            )
            response = Response(data, status=status.HTTP_201_CREATED)
        else:
            response = Response({'detail': 'Incorrect data'})
        return response
