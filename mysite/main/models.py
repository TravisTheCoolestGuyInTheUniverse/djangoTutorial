from django.db import models

#/seems like each table in the database is modeled by a class like the one below.
class User(models.Model):
    userName = models.CharField(max_length=20)

