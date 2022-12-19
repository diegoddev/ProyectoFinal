from django.urls import path
from appsignup.views import *



urlpatterns = [
    path("accounts/signup/", sign_up, name="signup"),
]