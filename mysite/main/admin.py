from django.contrib import admin
from .models import User
from tinymce.widgets import TinyMCE
from django.db import models
# Register your models here.

#this is the attributes of the User model that will appear 
#on the admin page as well as the order in which they will appear.
class UserAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Username/password", {"fields": ["userName", "password"]}),
        ("code", {"fields": ["code"]}),
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }
#register a model
admin.site.register(User, UserAdmin)
