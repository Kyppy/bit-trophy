from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import VideoGame
from .serializers import GameSerializer


class GamesView(APIView):
    """Returns a list of all game posts from all users."""
    def get(self, request):
        games = VideoGame.objects.all()
        serializer = GameSerializer(games, many=True)
        return Response({"games": serializer.data})
