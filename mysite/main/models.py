from django.db import models
import time

#/seems like each table in the database is modeled by a class like the one below.
#when making migrations on an actual database, must provide default value on new/added rows.
#so good database design off the bat is important.
class User(models.Model):
    userName = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    code = models.TextField(null=True)

    def __str__(self):
        return self.userName + " " + self.password

