from django.urls import path
from appblog.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("home/", home, name="home"),
    path("about/", about, name="about"),

    path("logout/", LogoutView.as_view(template_name="appblog/logout.html"), name="logout"),

    path("post/list/", PostList.as_view(), name="post-list"),
    path("post/detail/<pk>/", PostDetail.as_view(), name="post-detail"),
    path("post/create/", PostCreate.as_view(), name="post-create"),
    path("post/update/<pk>/", PostUpdate.as_view(), name="post-update"),
    path("post/delete/<pk>/", PostDelete.as_view(), name="post-delete")

]