from django.shortcuts import render
from .models import Manager
from rest_framework import generics
from .serializers import ManagerSerializer, ManagerListSerializer
from .pagination import ListPagination
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

class ManagerCreate(generics.CreateAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer


class ManagerListView(generics.ListAPIView):
    queryset = Manager.objects.all()
    serializer_class = ManagerListSerializer
    pagination_class = ListPagination
    lookup_field = 'pk'
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ('username',)
    search_fields = ('username',)