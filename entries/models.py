from django.contrib.auth.models import User
from django.db import models


class Entry(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date = models.DateField()
    author = models.ForeignKey(User)
    description = models.TextField()
    irrelevant = models.BooleanField(default=False)
    priority = models.BooleanField(default=False)

    class Meta:
        # Database table won't be created for this as it's meant to be an abstract class
        abstract = True

    def __str__(self):
        return self.description

    def get_class_name(self):
        return self.__class__.__name__

class Task(Entry):
    completed = models.BooleanField(default=False)


class Note(Entry):
    explore = models.BooleanField(default=False)
    inspiration = models.BooleanField(default=False)


class Event(Entry):
    pass
