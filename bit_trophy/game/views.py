from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import VideoGame
from .models import User

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
        return Response(serializer.data)

    """Updates data of an existing post"""
    def put(self, request, pk):
        # print(VideoGame.objects.get(title="Halo").pk)
        saved_game = get_object_or_404(VideoGame.objects.all(), pk=pk)
        data = request.data.get('game')
        serializer = GameSerializer(instance=saved_game, data=data,
                                    partial=True)
        if serializer.is_valid(raise_exception=True):
            game_saved = serializer.save()
        return Response({"success": "Post for '{}' updated successfully"
                        .format(game_saved.title)})
