from django.urls import path, include
from rest_framework import routers

from employees.views import EmployeeViewSet, EmployeesLastLocationView


router = routers.DefaultRouter()
router.register('', EmployeeViewSet)

urlpatterns = [
    path('last-locations/', EmployeesLastLocationView.as_view()),
    *router.urls
]
