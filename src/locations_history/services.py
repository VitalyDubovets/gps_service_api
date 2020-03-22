import random
import json

from datetime import datetime, timedelta


__all__ = [
    'ServiceTestData',
]


class ServiceTestData:
    def form_test_data(self, amount_data: int) -> list:
        data = []
        latitude, longitude = self._get_random_coordinates()
        date_of_stay = datetime.now()
        data.append({'latitude': latitude, 'longitude': longitude, 'date_of_stay': date_of_stay.isoformat()})
        for _ in range(amount_data - 1):
            latitude, longitude = self._get_next_coordinates(latitude, longitude)
            date_of_stay = self._get_new_datetime(date_of_stay)
            data.append({'latitude': latitude, 'longitude': longitude, 'date_of_stay': date_of_stay.isoformat()})
        return data

    @staticmethod
    def _get_random_coordinates() -> (float, float):
        latitude = round(random.random() * (90 + 90) - 90, 6)
        longitude = round(random.random() * (180 + 180) - 90, 6)
        return latitude, longitude

    @staticmethod
    def _get_new_datetime(date):
        new_date = date + timedelta(minutes=1)
        return new_date

    @staticmethod
    def _get_next_coordinates(latitude: float, longitude: float) -> (float, float):
        latitude_new = round(latitude + round(random.random() * (0.0008 + 0.0008) - 0.0008, 6), 6)
        longitude_new = round(longitude + round(random.random() * (0.0008 + 0.0008) - 0.0008, 6), 6)
        return latitude_new, longitude_new
