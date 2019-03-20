from django.urls import path


from .views import GamesView
from .views import GameView

from rest_framework_swagger.views import get_swagger_view
swag = get_swagger_view(title='Test Title')

app_name = "game"


urlpatterns = [
    path('v1/games/', GamesView.as_view()),
    path('v1/game/<int:pk>/', GameView.as_view()),
    path('v1/swagger-docs/', swag)
]
