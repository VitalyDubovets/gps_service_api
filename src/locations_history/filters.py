from django_filters import FilterSet, IsoDateTimeFilter

from .models import LocationHistory


__all__ = [
    'LocationHistoryFilter',
]


class LocationHistoryFilter(FilterSet):
    start_date = IsoDateTimeFilter(field_name='date_of_stay', lookup_expr='gte')
    end_date = IsoDateTimeFilter(field_name='date_of_stay', lookup_expr='lte')

    class Meta:
        model = LocationHistory
        fields = [
            'employee',
            'date_of_stay',
            'start_date',
            'end_date',
        ]
