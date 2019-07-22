from django.shortcuts import render
from rest_framework import viewsets
from .models import language,paradigm,programmer
from .serializers import languageserializer,paradigmserializer,programmerserializer

class languageview(viewsets.ModelViewSet):
        queryset = language.objects.all()
        serializer_class = languageserializer


class paradigmview(viewsets.ModelViewSet):
        queryset = paradigm.objects.all()
        serializer_class = paradigmserializer


class programmerview(viewsets.ModelViewSet):
        queryset = programmer.objects.all()
        serializer_class = programmerserializer