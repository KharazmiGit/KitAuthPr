from django.urls import path
from . import views

app_name = "robot_app"

urlpatterns = [
    path('save-actions/', views.SaveUserActions.as_view(), name='save-actions'),
    path('user-actions/', views.UserActionCreateView.as_view(), name='user-action-create'),
]
