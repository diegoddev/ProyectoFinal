from django.urls import path
from approfile.views import *

urlpatterns = [
    path("accounts/profile/", edit_profile, name="profile-edit"),
    path("accounts/avatar/", edit_avatar, name="avatar-edit"),
]