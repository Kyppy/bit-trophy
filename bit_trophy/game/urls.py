from django.urls import path

from .views import GamesView


app_name = "game"


urlpatterns = [
    path('games/', GamesView.as_view()),
    path('games/<int:pk>', GamesView.as_view()),
]
