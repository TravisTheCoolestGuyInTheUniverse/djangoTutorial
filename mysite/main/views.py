from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tutorial, TutorialCategory, TutorialSeries
#convenient form thats already created for us in django!
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
#this is the form that i extended from UserCreationForm
from .forms import NewUserForm
# Create your views here.
"""
slug is the url. single slug refers to showing different things at the same url rather than redirecting
to a new one. 
/cooking/
/tutorial-1-scrambled-eggs
"""
def single_slug(request, single_slug):
    #need to know: is this a category url or tutorial url?
    categories = [c.slug for c in TutorialCategory.objects.all()]
    if single_slug in categories:
        #category is foreign key in TutorialSeries, double underscore slug gets us the slug of a category.
        #returns list of series that are associated with a category that has a slug that matches the single_slug.
        matching_series = TutorialSeries.objects.filter(category__slug=single_slug)

        series_urls = {}
        for m in matching_series.all():
            #first series is foreign key in tutorials, second series is series attribute in TutorialSeries.
            #returns all tutorial objects that are a part of series m, and part 1 has the earliest published date.
            part_one = Tutorial.objects.filter(series__series=m.series).earliest("datePublished")
            #this will give us the tutorial object for the first tutorial in each series
            series_urls[m] = part_one.slug
        return render(request, "main/category.html", {"part_ones": series_urls})

    tutorials = [t.slug for t in Tutorial.objects.all()]
    if single_slug in tutorials:
        return HttpResponse(f"{single_slug} is a tutorial!!!")
    
    return HttpResponse(f"{single_slug} does not correspond to anything. 404")

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
                  template_name="main/categories.html",
                  context={"Categories": TutorialCategory.objects.all})


def register(request):
    #if the user clicks the register button, request is post (make changes to server)
    if request.method == "POST":
        #fill form with data that they inserted
        form = NewUserForm(request.POST)
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
            #finds that app_name = 'main' in urls.py and then finds the path with name home and takes user there.
            return redirect('main:home')
        else:
            for msg in form.error_messages:
                #temporary way of handling error messages
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

    form = NewUserForm
    return render(request, "main/register.html", context={"form":form})

def logout_request(request):
    #use djangos built in function to log the user out (also this is why you don't want your view to be called logout)
    logout(request)
    #create a message that says that the user logged out successfully
    messages.info(request, "Logged out successfully! WOOOO")
    #redirect to the path in main with the name home (urls.py)
    return redirect("main:home")

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            #we're getting the value of the 'username' field from the form
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            #if there is a user with the username and password in a database, this will not be None
            user = authenticate(username=username, password=password)
            if user is not None:
                #if the user is valid, log em in! (using djangos default login function)
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect("main:home")
            else:
                messages.info(request, f"invalid username or password!")
        else:
            messages.info(request, f"invalid username or password! (form)")

    #"pass form into the template"
    form = AuthenticationForm()
    return render(request, "main/login.html", {"form":form})


