from django.shortcuts import render, redirect
from django.shortcuts import render
from appsignup.forms import UserRegisterForm

# Create your views here.

def sign_up(request):
    
    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)

        if formulario.is_valid():           
            formulario.save()

            return redirect("home")
        else:
            return render(request, "appsignup/sign_up.html", { "form": formulario, "errors": formulario.errors})

    formulario  = UserRegisterForm()
    return render(request, "appsignup/sign_up.html", { "form": formulario})