import random

from datetime import datetime, timedelta


__all__ = [
    'ServiceTestData',
]


class ServiceTestData:
    """
    Класс, позволяющий генерировать тестовые данные для API
    """
    def form_test_data(self, employee_id: int, starts_date: datetime, end_date: datetime,
                       latitude=None, longitude=None) -> list:
        data = []
        if not latitude and not longitude:
            latitude, longitude = self._get_random_coordinates()
        date_of_stay = starts_date
        data.append({
            'employee': employee_id,
            'latitude': latitude,
            'longitude': longitude,
            'date_of_stay': date_of_stay.strftime("%Y-%m-%dT%H:%M:%SZ")
        })
        amount_data = self._get_difference_in_minutes(starts_date, end_date)
        for _ in range(amount_data):
            latitude, longitude = self._get_next_coordinates(latitude, longitude)
            date_of_stay = self._get_new_datetime(date_of_stay)
            data.append({
                'employee': employee_id,
                'latitude': latitude,
                'longitude': longitude,
                'date_of_stay': date_of_stay.strftime("%Y-%m-%dT%H:%M:%SZ")
            })
        return data

    @staticmethod
    def _get_difference_in_minutes(starts_date: datetime, end_date: datetime) -> int:
        """
        Данный метод предназначен для вычисления количества тестовых данных, которые должны будут
        сгенерироваться.
        Одна локация на одну минуту
        :param starts_date: Дата начала вреисчисления
        :param end_date: Дата конца времяисчисления
        :return: Разница в минутах между двумя промежутками времени
        """
        difference_between_two_date = end_date - starts_date
        difference_minute = difference_between_two_date.seconds // 60
        return difference_minute

    @staticmethod
    def _get_random_coordinates() -> (float, float):
        """
        Метод для получение рандомных координат
        :return: Возвращает широту и долготу
        """
        latitude = round(random.random() * (90 + 90) - 90, 6)
        longitude = round(random.random() * (180 + 180) - 90, 6)
        return latitude, longitude

    @staticmethod
    def _get_new_datetime(old_date: datetime) -> datetime:
        """
        Метод для получение даты, которая больше на 1 минуту
        :param old_date: Прошлая дата
        :return:
        """
        new_date = old_date + timedelta(minutes=1)
        return new_date

    @staticmethod
    def _get_next_coordinates(latitude: float, longitude: float) -> (float, float):
        """
        Метод рандомно создает новые координаты.
        Расстояние от точки не больше 100 метров
        :param latitude: Широта
        :param longitude: Долгота
        :return: Новые числа широты и долготы
        """
        latitude_new = round(latitude + round(random.random() * (0.0007 + 0.0007) - 0.0007, 6), 6)
        longitude_new = round(longitude + round(random.random() * (0.0007 + 0.0007) - 0.0007, 6), 6)
        return latitude_new, longitude_new
