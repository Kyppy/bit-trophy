from rest_framework import serializers
from .models import VideoGame


class GameSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    platform = serializers.CharField()
    genre = serializers.CharField()
    user_rating = serializers.IntegerField()
    is_playing = serializers.BooleanField()
    user = serializers.IntegerField()

    def create(self, validated_data):
        return VideoGame.objects.create(**validated_data)
