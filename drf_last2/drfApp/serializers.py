from .models import Platform,Movie
from rest_framework import serializers

class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model=Movie
        fields="__all__"
    ott=serializers.StringRelatedField()

class PlatformSerializer(serializers.ModelSerializer):

    class Meta:
        model=Platform
        fields="__all__"
    movies=serializers.StringRelatedField(many=True, read_only=True)
    
