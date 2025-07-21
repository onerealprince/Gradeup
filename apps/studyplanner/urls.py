from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudyEventViewSet

router = DefaultRouter()
router.register(r'study-events', StudyEventViewSet, basename='study-events')

urlpatterns = [
    path('api/', include(router.urls)),
]
