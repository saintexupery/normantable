from django.shortcuts import render

from rest_framework import generics, permissions

from search.models import SearchWord
from search.serializer import SearchResultSerializer

class SearchResultAPIView(generics.CreateAPIView):
    serializer_class = SearchResultSerializer
    permission_classes = [permissions.AllowAny]
