from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import VideoGame
from .models import User

from .serializers import GameSerializer


class GamesView(APIView):
    def get(self, request):
        """Returns a list of all game posts from all users."""
        games = VideoGame.objects.all()
        serializer = GameSerializer(games, many=True)
        return Response({"games": serializer.data})

    def post(self, request):
        """Creates a game post using data from the request"""
        game = request.data.get('game')
        serializer = GameSerializer(data=game)
        if serializer.is_valid(raise_exception=True):
            save_game = serializer.save()
            return Response(serializer.data)
        return serializer.errors


class GameView(APIView):
    def get(self, request, pk):
        """Returns a single game entry"""
        game = get_object_or_404(VideoGame.objects.all(), pk=pk)
        serializer = GameSerializer(game, many=False)
        return Response({"game": [serializer.data]}, status=200)

    def put(self, request, pk):
        """Updates data of an existing post"""
        saved_game = get_object_or_404(VideoGame.objects.all(), pk=pk)
        data = request.data.get('game')
        serializer = GameSerializer(instance=saved_game, data=data,
                                    partial=True)
        if serializer.is_valid(raise_exception=True):
            game_saved = serializer.save()
            return Response({"success": "Post for '{}' updated successfully"
                            .format(game_saved.title)})
        return serializer.errors

    def delete(self, request, pk):
        """Delete a single game entry"""
        game = get_object_or_404(VideoGame.objects.all(), pk=pk)
        game.delete()
        return Response({"message": "Game entry with id `{}` has been deleted."
                        .format(pk)}, status=204)
