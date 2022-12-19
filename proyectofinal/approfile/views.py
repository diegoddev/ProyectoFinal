from django.shortcuts import render, redirect
from approfile.forms import UserEditForm, AvatarForm
from django.contrib.auth.decorators import login_required
from approfile.models import Avatar

@login_required
def edit_profile(request):

    usuario = request.user

    if request.method == "POST":
        formulario = UserEditForm(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            usuario.email = data["email"]
            usuario.first_name = data["first_name"]
            usuario.last_name = data["last_name"]

            usuario.save()

            return redirect("home")
        
        else:
            return render(request, "approfile/profile.html", {"form": formulario, "errors": formulario.errors})

    else:
        formulario = UserEditForm(initial={"email": usuario.email, "first_name": usuario.first_name, "last_name": usuario.last_name})
        pass

    return render(request, "approfile/edit_profile.html", {"form": formulario})

@login_required
def edit_avatar(request):

    if request.method == "POST":
        formulario = AvatarForm(request.POST, files=request.FILES)

        if formulario.is_valid():
            data = formulario.cleaned_data

            usuario = request.user

            avatar = Avatar(user=usuario, imagen=data["imagen"])
            avatar.save()

            return redirect("home")
        else:
            return render(request, "approfile/edit_avatar.html", {"form": formulario, "errors": formulario.errors})
    formulario = AvatarForm()

    return render(request, "approfile/edit_avatar.html", {"form": formulario})