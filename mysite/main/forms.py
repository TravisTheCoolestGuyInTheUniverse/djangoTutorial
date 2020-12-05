from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
    #this is how we extend a previously existing form. 
    #here we create a field for an email that is required
    #for the form to be valid.
    email = forms.EmailField(required=True)

    #i'm guessing that this is like "meta data" or in this case data about the form.
    class Meta:
        #i'm guessing that this connects this form to the database via the User model.
        model = User
        #these are the fields for the form
        fields = ("username", "email", "password1", "password2")
    #commit the data to the database (user registration data)
    def save(self, commit=True):
        #this is the user model object without the email
        user = super(NewUserForm, self).save(commit=False)
        #set the value of the email from the form
        user.email = self.cleaned_data['email']
        if commit:
            #commit it to the database
            user.save()
        return user