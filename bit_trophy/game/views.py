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
    
    """Creates a game post using data from the request"""
    def post(self, request):
        game = request.data.get('game')
        serializer = GameSerializer(data=game)
        if serializer.is_valid(raise_exception=True):
            save_game = serializer.save()
        return Response({"success": "Your '{}' post was successful"
                        .format(save_game.title)})
