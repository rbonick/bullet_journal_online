from django.contrib import admin
from entries.models import *


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('description', 'author', 'date')


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('description', 'author', 'date')


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('description', 'author', 'date')