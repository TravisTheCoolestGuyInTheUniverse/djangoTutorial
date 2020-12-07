from django.contrib import admin
from .models import Tutorial, TutorialSeries, TutorialCategory
from tinymce.widgets import TinyMCE
from django.db import models
# Register your models here.

#this is the attributes of the Tutorial model that will appear 
#on the admin page as well as the order in which they will appear.
class TutorialAdmin(admin.ModelAdmin):

    fieldsets = [
        ("title/date published", {"fields": ["title", "datePublished"]}),
        ("content", {"fields": ["content"]}),
        #not that you would ever want to see/manually chage a foreign key but it's just nice to see.
        ("foreignKey/slug", {"fields": ["series", "slug"]})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }
#register a model

admin.site.register(TutorialCategory)
admin.site.register(TutorialSeries)
admin.site.register(Tutorial, TutorialAdmin)

