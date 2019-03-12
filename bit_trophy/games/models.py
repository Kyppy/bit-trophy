from django.db import models


class VideoGame(models.Model):
    """This class represents the videogame model"""
    title = models.CharField(max_length=100, blank=False)
    
    def __str__(self):
        return "{}".format(self.name)
