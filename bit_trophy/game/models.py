from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from .choice_list.choices import Choices


class User(models.Model):
    """This class represents the model for users"""
    username = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return "{}".format(self.username)


class VideoGame(models.Model):
    """This class represents the videogame model"""
    title = models.CharField(max_length=100, help_text='Enter the name of the '
                             'game.')
    platform = models.CharField(max_length=30, choices=Choices()
                                .platform_choices,
                                help_text='Select the console that you play '
                                'the game on.')
    genre = models.CharField(max_length=30, choices=Choices().genre_choices,
                             help_text='Select the game genre.')
    user_rating = models.IntegerField(default=0, validators=[
                                     MaxValueValidator(10),
                                     MinValueValidator(0)])
    is_playing = models.BooleanField(default=False)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return "{}".format(self.title)
