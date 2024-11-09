from django.urls import path, include
from . import views

urlpatterns = [
    path("movielist/", views.MovieListCV.as_view()),
    path("moviecreate/", views.MovieCreateCV.as_view()),
    path("movie/<int:pk>", views.MovieDetailCV.as_view()),
    path("platformlist/", views.PlatformListCV.as_view()),
    path("platformcreate/", views.PlatformCreateCV.as_view()),
    path("platform/<int:pk>", views.PlatformDetailCV.as_view()),
]