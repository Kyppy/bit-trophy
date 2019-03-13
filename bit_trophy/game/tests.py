from django.test import TestCase
from django.test import Client

from .models import VideoGame


class RetrieveGameTestcase(TestCase):
    """This class defines the test suite for the 'VideoGame' model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.videogame_title = "Pokemon"
        self.videogame = VideoGame(title=self.videogame_title)
        self.game_entry_one = VideoGame(title="Doom", platform="PS3",
                                        genre="Action")
        self.game_entry_two = VideoGame(title="Overlord", platform="PS3",
                                        genre="RTS")
        self.game_entry_three = VideoGame(title="Skyrim", platform="PS3",
                                          genre="RPG")

    def test_can_save_a_game_entry(self):
        """Test to save a single game entry to the database."""
        old_count = VideoGame.objects.count()
        self.videogame.save()
        new_count = VideoGame.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_view_can_retrieve_null_entry(self):
        """Test to retrieve entries from an empty database."""
        response = Client().get('/api/games/')
        self.assertEqual(response.status_code, 200)
        data = response.json()['games']
        total_entries = len(data)
        self.assertEqual(total_entries, 0)

    def test_view_can_retrieve_all_game_entries(self):
        """Test to retrieve all of the game entries stored in database."""
        self.game_entry_one.save()
        self.game_entry_two.save()
        self.game_entry_three.save()
        response = Client().get('/api/games/')
        self.assertEqual(response.status_code, 200)
        data = response.json()['games']
        total_entries = len(data)
        self.assertEqual(total_entries, 3)
        
