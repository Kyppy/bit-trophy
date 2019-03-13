from django.db import models


class VideoGame(models.Model):
    """This class represents the videogame model"""
    title = models.CharField(max_length=100, blank=False)
    platform = models.CharField(max_length=15)
    genre = models.CharField(max_length=25)
    user_rating = models.DecimalField(max_digits=3, decimal_places=1)
    is_playing = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.name)
