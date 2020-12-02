from django.shortcuts import render
from django.http import HttpResponse
from .models import Tutorial
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
