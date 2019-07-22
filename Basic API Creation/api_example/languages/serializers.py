from rest_framework import serializers
from .models import language,paradigm,programmer

class languageserializer(serializers.ModelSerializer):
    class Meta:
        model = language
        fields = ('id','name','paradigm')

class paradigmserializer(serializers.ModelSerializer):
    class Meta:
        model = paradigm
        fields = ('id','name')
        
class programmerserializer(serializers.ModelSerializer):
    class Meta:
        model = programmer
        fields = ('id','name','language')
