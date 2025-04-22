from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EnzymeViewSet, UserViewSet


# Create a router and register our viewsets with it
router = DefaultRouter()
router.register('enzymes', EnzymeViewSet, basename='enzyme')
router.register('users', UserViewSet, basename='user')
# API endpoints
urlpatterns = router.urls


