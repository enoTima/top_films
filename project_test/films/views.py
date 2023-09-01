from django.shortcuts import render
from django.http import HttpResponse

from .models import *


def index(request):
    return render(
        request,
        template_name='films/index.html',
        context={
            'directors': Director.objects.order_by('last'),
            'films': Film.objects.order_by('title'),
            'actors': Actor.objects.order_by('first'),
        }
    )


def film_detail(request, pk):
    return render(
        request,
        template_name='films/film.html',
        context={
            'film': Film.objects.get(id__exact=pk),
        }
    )


def director_detail(request, pk):
    return render(
        request,
        template_name='films/director.html',
        context={
            'director': Director.objects.get(id__exact=pk),
        }
    )


def actor_list(request):
    return render(
        request,
        template_name='films/actors.html',
        context={
            'actors': Actor.objects.order_by('first')
        }
    )
