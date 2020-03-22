from rest_framework import routers

from .views import LocationHistoryViewSet


router = routers.DefaultRouter()
router.register('', LocationHistoryViewSet)

urlpatterns = router.urls
