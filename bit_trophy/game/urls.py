from django.urls import path

from .views import GamesView


app_name = "game"

# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('games/', GamesView.as_view()),
]
