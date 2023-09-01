from django.urls import path
from . import views

app_name = 'films'

urlpatterns = [
    # http://127.0.0.1:8000/flm/
    path('', views.index, name='index'),
    # http://127.0.0.1:8000/flm/book/<>/
    path('film/<int:pk>/', views.film_detail, name='film-detail'),
    # http://127.0.0.1:8000/flm/director/<>/
    path('director/<int:pk>/', views.director_detail, name='director-detail'),
    # http://127.0.0.1:8000/flm/actors/
    path('actors/', views.actor_list, name='actor-list'),
]

