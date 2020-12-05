from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tutorial
#convenient form thats already created for us in django!
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# Create your views here.

def home(request):
    """
    Three things are passesd to render: the request, (get/post),
    the location of the template (html), 
    and the context (perhaps data from a database)

    why "main/templates/main/home" ? when we reference templates,
    django looks through all apps for templates directory, multiple 
    apps might have a "main.html" template, so there could be conflict without
    this distinction with the extra main directory in the templates folder.
    """
    #keep in mind that User model must be imported.
    #looks 
    return render(request=request, 
                  template_name="main/home.html",
                  context={"Tutorials": Tutorial.objects.all})


def register(request):
    #if the user clicks the register button, request is post (make changes to server)
    if request.method == "POST":
        #fill form with data that they inserted
        form = UserCreationForm(request.POST)
        if form.is_valid():
            #commit to the database
            user = form.save()

            #cleaned_data makes the data in the username field in a normalized format.
            username = form.cleaned_data.get('username')
            #this always goes to the exact user that is supposed to get this message.
            #site-wide notifications are done differently, maybe putting something in the header file.
            #this doesn't actually send a message, but it stores it.
            messages.success(request, f"New Account Created: {username}")
            #login the user
            login(request, user)
            messages.info(request, f"You are now logged in as {username}")
            #return them to the homepage
            #finds that app_name = 'home' in urls.py and then finds the path with name home and takes user there.
            return redirect('main:home')
        else:
            for msg in form.error_messages:
                #temporary way of handling error messages
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

    form = UserCreationForm
    return render(request, "main/register.html", context={"form":form})