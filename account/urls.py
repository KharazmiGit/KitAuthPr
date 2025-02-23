from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet , auth_test


router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

app_name = 'account'

urlpatterns = [
    path('', include(router.urls)),
    path('test', auth_test),
]
