"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from . import views

#this gives us a way of referencing paths without having the exact path. look in views.py to see how.
#ex. main:register, boom we have that path and we know what to show when redirected.
app_name = "main"

"""
at the URI of '' we want to display whatever is in views.home.
"""
urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name="register"),
    #we wouldn't wanna call this logout because it would overrride djangos logout function.
    path('logout/', views.logout_request, name="logout"),
    path("login/", views.login_request, name="login"),
]
