from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class User(models.Model):
    """This class represents the model for users"""
    username = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return "{}".format(self.username)


class VideoGame(models.Model):
    """This class represents the videogame model"""
    title = models.CharField(max_length=100)
    platform = models.CharField(max_length=15, default='Add PC or Console')
    genre = models.CharField(max_length=25, default='Add genre')
    user_rating = models.IntegerField(default=0, validators=[
                                     MaxValueValidator(10),
                                     MinValueValidator(0)])
    is_playing = models.BooleanField(default=False)
    user = models.ForeignKey('User', related_name='user',
                             on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.title)
