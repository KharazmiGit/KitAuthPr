from django.urls import path
from .views import login_view, protected_view , LoginPageView , logout_view


app_name = 'auth_processor'
urlpatterns = [
    path("api/login/", login_view),
    path("api/protected/", protected_view),
    path("authentication/page" ,LoginPageView.as_view() , name="login_page") ,
    path("logout/" ,logout_view , name='logout')
]
