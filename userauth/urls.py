from django.urls import path
from .views import *

app_name = 'auth'

urlpatterns = [
    path("check",user_form,name='check'),
    path("login",login_view,name='login'),
    path("logout",logout_view,name="logout")
]
