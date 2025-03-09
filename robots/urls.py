from django.urls import path
from . import views

app_name = "robot_app"

urlpatterns = [
    path('login', views.hello_world, name='login_robot')
]
