from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class VideoGame(models.Model):
    """This class represents the videogame model"""
    title = models.CharField(max_length=100, blank=False)
    platform = models.CharField(max_length=15, default='Add PC or Console')
    genre = models.CharField(max_length=25, default='Add genre')
    user_rating = models.IntegerField(default=0, validators=[
                                     MaxValueValidator(100),
                                     MinValueValidator(0)])
    is_playing = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.title)
