from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
# Create your views here.

def log_in(request):

    errors = ""

    if request.method == "POST":
        formulario = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            user = authenticate(username=data["username"], password=data["password"])
            
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                return render(request, "applogin/login.html", {"form": formulario, "errors": "Credenciales invalidas"})
        else:
            return render(request, "applogin/login.html", {"form": formulario, "errors": formulario.errors})

    formulario = AuthenticationForm()
    return render(request, "applogin/login.html", {"form": formulario, "errors": errors})
