from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, index
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')

app_name = 'account'

urlpatterns = [
    path('user/crud', include(router.urls)),
    path('', index , name='index_page'),
]
