from django.shortcuts import render, redirect
from appblog.models import Post
from approfile.models import Avatar
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

def home(request):
    if request.user.is_authenticated:
        imagen_model = Avatar.objects.filter(user= request.user.id).order_by("-id")[0]
        if imagen_model == "":
            pass
        imagen_url = imagen_model.imagen.url
    else:
        imagen_url = ""
    return render(request, "appblog/home.html", {"imagen_url": imagen_url})

def about(request):                   

    return render(request, "appblog/about.html")

class PostList(ListView):

    model = Post
    template_name = "appblog/post_list.html"

class PostDetail(DetailView):

    model = Post
    template_name = "appblog/post_detail.html"

class PostCreate(LoginRequiredMixin, CreateView):

    model = Post
    success_url = "/post/list/"
    fields = ["titulo", "subtitulo", "autor", "contenido", "imagen"]

class PostUpdate(LoginRequiredMixin, UpdateView):

    model = Post
    success_url = "/post/list/"
    fields = ["titulo", "subtitulo", "autor", "contenido"]

class PostDelete(LoginRequiredMixin, DeleteView):

    model = Post
    success_url = "/post/list/"

