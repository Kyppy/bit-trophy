from django.test import TestCase
from django.test import Client

from rest_framework.test import APIClient

from .models import VideoGame
from .models import User


class RetrieveGameTestcase(TestCase):
    """This class defines the test suite for the 'VideoGame' model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.user_entry = User(username="Bob", email="mail@demo.com")
        self.game_entry_one = VideoGame(title="Doom", platform="PS3",
                                        genre="Action", user_id=1)
        self.game_entry_two = VideoGame(title="Overlord", platform="PS3",
                                        genre="RTS", user_id=1)
        self.game_entry_three = VideoGame(title="Skyrim", platform="PS3",
                                          genre="RPG", user_id=1)
        self.new_post = {"game":
                         {
                                "title": "Skyrim",
                                "platform": "PS3",
                                "genre": "RPG",
                                "user_rating": 100,
                                "is_playing": False,
                                "user_id": 1
                         }
                         }

    def test_can_save_a_game_entry(self):
        """Test to save a single game entry to the database."""
        old_count = VideoGame.objects.count()
        self.game_entry_one.save()
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

    def test_view_can_post_game_entry(self):
        """Test to post game entry to database."""
        old_count = VideoGame.objects.count()
        response = self.client.post('/api/games/', self.new_post,
                                    format='json')
        self.assertEqual(response.status_code, 200)
        new_count = VideoGame.objects.count()
        self.assertEqual(new_count, 1)

    def test_view_can_edit_game_entry(self):
        """Test to update two attributes of a game entry."""
        self.game_entry_one.save()
        old_title = VideoGame.objects.get(pk=1).title
        old_genre = VideoGame.objects.get(pk=1).genre
        response = self.client.put('/api/games/1', self.new_post,
                                   format='json')
        self.assertEqual(response.status_code, 200)
        new_title = VideoGame.objects.get(pk=1).title
        new_genre = VideoGame.objects.get(pk=1).genre
        self.assertEqual(new_title, "Skyrim")
        self.assertEqual(new_genre, "RPG")

    def test_view_can_delete_game_entry(self):
        """Test to delete a game entry."""
        self.game_entry_one.save()
        self.game_entry_two.save()
        response = self.client.delete('/api/games/1', format='json')
        self.assertEqual(response.status_code, 204)
        count = VideoGame.objects.count()
        self.assertEqual(count, 1)
        entry_id = VideoGame.objects.get(pk=2).pk
        self.assertEqual(entry_id, 2)
    