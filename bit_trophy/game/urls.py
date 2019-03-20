from django.urls import path

from .views import GamesView
from .views import GameView


app_name = "game"


urlpatterns = [
    path('v1/games/', GamesView.as_view()),
    path('v1/games/<int:pk>', GamesView.as_view()),
    path('v1/game/<int:pk>', GameView.as_view()),
]
