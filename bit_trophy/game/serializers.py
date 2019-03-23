from django.core.validators import MaxValueValidator, MinValueValidator
from rest_framework import serializers

from .models import VideoGame
from .choice_list.choices import Choices


class GameSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    platform = serializers.ChoiceField(Choices()
                                       .platform_choices)
    genre = serializers.ChoiceField(Choices().genre_choices)
    user_rating = serializers.IntegerField(default=0, validators=[
                                     MaxValueValidator(10),
                                     MinValueValidator(0)])
    is_playing = serializers.BooleanField(default=False)
    user_id = serializers.IntegerField()

    def create(self, validated_data):
        return VideoGame.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.platform = validated_data.get('platform', instance.platform)
        instance.genre = validated_data.get('genre', instance.genre)
        instance.user_rating = validated_data.get('user_rating',
                                                  instance.user_rating)
        instance.is_playing = validated_data.get('is_playing',
                                                 instance.is_playing)
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.save()
        return instance
