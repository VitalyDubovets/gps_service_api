from django.db import models


__all__ = [
    'Employee',
]


class Employee(models.Model):
    first_name = models.CharField(max_length=255, verbose_name='Имя')
    second_name = models.CharField(max_length=255, blank=True, verbose_name='Отчество')
    last_name = models.CharField(max_length=255, verbose_name='Фамилия')
    sex = models.CharField(max_length=50, blank=True,  verbose_name='Пол')
    birth_date = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'

    def __str__(self):
        if self.second_name:
            full_name = self.first_name + ' ' + self.second_name + ' ' + self.last_name
        else:
            full_name = self.first_name + ' ' + self.last_name
        return full_name
