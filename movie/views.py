from django.shortcuts import render
from .models import Movie

from rest_framework import viewsets
from rest_framework import permissions
from movie.serializers import MovieSerializer


class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAuthenticated]