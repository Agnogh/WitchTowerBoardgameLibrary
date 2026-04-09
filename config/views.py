# helper module
# render takes request + tempalte and combines. Then returns html in browser
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignUpForm

# defining function named 'home' with object 'request'


def home(request):
    return render(request, "home.html")


def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = SignUpForm()

    return render(request, "registration/signup.html", {"form": form})
