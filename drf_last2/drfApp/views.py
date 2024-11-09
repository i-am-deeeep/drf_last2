from django.shortcuts import render
from .models import Movie, Platform
from .serializers import MovieSerializer, PlatformSerializer
from rest_framework.response import Response
from rest_framework import generics
from .paginations import MovieListPNPagination, MovieListLOPagination, PlatformListCPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
# Create your views here.


class MovieListCV(generics.ListAPIView):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer
    # pagination_class=MovieListCPagination

    # filter_backends=[DjangoFilterBackend]  # /movielist/?ott__name=Netflix
    # filterset_fields=['ott__name']

    # filter_backends=[filters.SearchFilter]  # /movielist/?search=the
    # search_fields=['ott__name','description', '=title']

    filter_backends=[filters.OrderingFilter] # /movielist/?ordering=-ott__name,-id
    ordering_fields=['id','ott__name']
    def get_queryset(self):
        qset=Movie.objects.filter(ott__name=self.request.query_params.get('ott'))
        if qset.exists():
            return qset
        return Movie.objects.all()

class MovieCreateCV(generics.CreateAPIView):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer

class MovieDetailCV(generics.RetrieveUpdateDestroyAPIView):
    queryset=Movie.objects.all()
    serializer_class=MovieSerializer


class PlatformListCV(generics.ListAPIView):
    queryset=Platform.objects.all()
    serializer_class=PlatformSerializer
    pagination_class=PlatformListCPagination

class PlatformCreateCV(generics.CreateAPIView):
    queryset=Platform.objects.all()
    serializer_class=PlatformSerializer

class PlatformDetailCV(generics.RetrieveUpdateDestroyAPIView):
    queryset=Platform.objects.all()
    serializer_class=PlatformSerializer