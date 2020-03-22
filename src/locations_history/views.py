from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, status, viewsets
from rest_framework.response import Response

from .filters import LocationHistoryFilter
from .models import LocationHistory
from .serializers import LocationHistorySerializer


__all__ = [
    'LocationHistoryViewSet',
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
