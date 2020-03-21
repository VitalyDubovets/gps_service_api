from django.urls import path, include
from rest_framework import routers

from employees.views import EmployeeViewSet


router = routers.DefaultRouter()
router.register('', EmployeeViewSet)

urlpatterns = router.urls
