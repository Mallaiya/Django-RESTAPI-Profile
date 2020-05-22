from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import TestAPIView, TestViewSet, UserViewSet


router = DefaultRouter()
router.register('test-viewset', TestViewSet, basename='test-viewset')
router.register('profile', UserViewSet)


urlpatterns = [
    path('test/', TestAPIView.as_view()),
    path('', include(router.urls))
]
