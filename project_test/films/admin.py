from django.contrib import admin
from .models import *


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ['first', 'last']

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ['title', 'director']


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    pass
