from rest_framework import serializers


class GameSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    platform = serializers.CharField()
    genre = serializers.CharField()
    user_rating = serializers.IntegerField()
    is_playing = serializers.BooleanField()
