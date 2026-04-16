"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Import Djangos build in admin site
from django.contrib import admin
# to connect url's
from django.urls import path, include
# import function 'home' from 'views.py'
from .views import home, signup_view, login_view, logout_view

urlpatterns = [
    # admin is for handing over control to Django
    path("admin/", admin.site.urls),
    # empty part emasn root URL, 'home' is function to run
    path("", home, name="home"),
    # link to 'games'
    path("games/", include("games.urls")),
    path("accounts/signup/", signup_view, name="signup"),
    path("accounts/login/", login_view, name="login"),
    path("accounts/logout/", logout_view, name="logout"),
    # built-in auth routes
    path("accounts/", include("django.contrib.auth.urls")),

]
