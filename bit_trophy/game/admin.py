from django.contrib import admin

from .models import VideoGame
from .models import User

admin.site.register(VideoGame)
admin.site.register(User)
