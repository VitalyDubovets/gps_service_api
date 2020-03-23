# В проекте используется менеджер зависимостей poetry
pip3 install --user poetry - установка менеджера зависимостей
poetry shell - активация виртуального окружения
poetry install - установка пакетов

# Для успешного запуска проекта также понадобится файл .env

##### Admin info
ADMIN_INFO=VITALY dubovetsvitaly@gmail.com (пример)

##### Database main store
DATABASE_NAME=gsa
DATABASE_USER=test_user
DATABASE_PASSWORD=test_user
DATABASE_HOST=localhost
DATABASE_PORT=5000 (или 5432, в зависимости от того, какой порт доступен)

##### Redis cache store
REDIS_HOST=localhost
REDIS_PORT=6000

После добавления файла нужно запустить docker-compose
docker-compose -f docker-compose.yml up -d

# Эндпоинты API
#### Энпоинт для получения, удаления, изменения, создания сотрудника
/api/v1/employees/{id} - GET, PATCH, DELETE
/api/v1/employees/ - POST
POST запросом отправляется json c форматом 

{
	"first_name": "Лев",
	"second_name": "Николаевич",
	"last_name": "Толстой",
	"sex": "М",
	"birth_date": "1828-09-09"
}

#### Эндпоинт для получения и создания истории перемещния сотрудника
/api/v1/locations-history/
POST запросом отправляется json c форматом 

[
	{
		"employee": {empolyee_id},
		"latitude": 63.9364,
		"longitude": 45.231453,
		"date_of_stay": "2020-03-23 15:18" 
	},
	{
		"employee": 2,
		"latitude": 63.987334,
		"longitude": 45.231253,
		"date_of_stay": "2020-03-23 15:20"
	}
]

либо
 
{
    "employee": {empolyee_id},
    "latitude": 63.9364,
    "longitude": 45.231453,
    "date_of_stay": "2020-03-23 15:18" 
}

Оба запроса пройдут успешно
При получении истории перемещений нужно указать GET Параметры

/api/v1/locations-history/?start_date=2020-03-15 00:00&end_date=2020-03-23 21:20&employee=3

employee - id работника
start_date - начало временного промежутка
end_date - конец временного промежутка

#### Эндопинт для генерации тестовых данных истории перемещений
Отправляется POST запрос на адрес /api/v1/locations-history/generator-test-data/
POST запросом отправляется json в формате 

{
	"employee_id": 3,
	"starts_date": "2020-03-23 10:41",
	"end_date": "2020-03-23 20:59",
	"latitude": 65.098345,
	"longitude": 45.123453
}

employee_id - id сотрудника
starts_date - начало временного промежутка
end_date - конец временного промежутка
latitude - широта
longitude - долгота

#### Эндопинт для получения данных о последнем местоположении всех сотрудников
Отправляется GET запрос на адрес /api/v1/employees/last-locations/



