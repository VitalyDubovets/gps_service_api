from django.urls import path
from rest_framework import routers

from .views import *


router = routers.DefaultRouter()
router.register('', LocationHistoryViewSet)

urlpatterns = [
    path('generator-test-data/', GeneratorTestDataView.as_view()),
    *router.urls
]