from django.db import models
from django.utils import timezone

from employees.models import Employee

__all__ = [
    'LocationHistory',
]


class LocationHistory(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, verbose_name='Работник', related_name='locations')
    latitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name='Широта')
    longitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name='Долгота')
    date_of_stay = models.DateTimeField(default=timezone.now(), verbose_name='Дата нахождения в заданной точке')

    class Meta:
        verbose_name = 'История местонахождения'
        verbose_name_plural = 'Истории местонахождений'

    def __str__(self):
        return str(self.latitude) + ', ' + str(self.longitude)