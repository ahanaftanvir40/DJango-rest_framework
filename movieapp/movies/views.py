from django.shortcuts import render
from rest_framework import viewsets #we need to import this for view
from .serializers import MovieSerializer
from .models import MovieData
# Create your views here.

class MovieViewSet(viewsets.ModelViewSet):

    queryset = MovieData.objects.all()
    serializer_class = MovieSerializer

class ActionViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(genre = 'action')
    serializer_class = MovieSerializer

class ComedyViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(genre = 'Comedy')
    serializer_class = MovieSerializer 
