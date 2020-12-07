from django.db import models
import time




class TutorialCategory(models.Model):
    category = models.CharField(max_length=200)
    categorySummary = models.CharField(max_length=200)
    categorySlug = models.CharField(max_length=200)

    class Meta:
        #this is for our admin page so it shows up as Catergories instead of Catergorys
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category

class TutorialSeries(models.Model):
    series = models.CharField(max_length=200)
    """
    a series is related to a category via category foreign key. 
    on delete tells what to do with related objects when a entity is deleted.
    For example, if a category was deleted, you could set it to cascade and delete all
    series related to that category. We obviously don't want to do that in this case so 
    we set it to the default category.
    """ 
    category = models.ForeignKey(TutorialCategory, default=1, verbose_name="Category", on_delete=models.SET_DEFAULT)
    summary = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Series"

    def __str__(self):
        return self.series


#/seems like each table in the database is modeled by a class like the one below.
#when making migrations on an actual database, must provide default value on new/added rows.
#so good database design off the bat is important.
class Tutorial(models.Model):
    title = models.CharField(max_length=50)
    datePublished = models.DateTimeField("date published")
    content = models.TextField(null=True)

    #this connects the Tutorial table with the TutorialSeries table. better documentation on what this does below.
    series = models.ForeignKey(TutorialSeries, default=1, verbose_name="Series", on_delete=models.SET_DEFAULT)
    #URL to first tutorial in a tutorial series.
    slug = models.CharField(max_length=200, default=1)
    def __str__(self):
        return self.title
