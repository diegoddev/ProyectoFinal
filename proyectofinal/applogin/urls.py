from django.urls import path
from applogin.views import *



urlpatterns = [
    path("accounts/login/", log_in, name="login"),
]