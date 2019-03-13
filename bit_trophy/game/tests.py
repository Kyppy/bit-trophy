from django.test import TestCase
from .models import VideoGame


class RetrieveGameTestcase(TestCase):
    """This class defines the test suite for the 'VideoGame' model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.videogame_title = "Pokemon"
        self.videogame = VideoGame(title=self.videogame_title)

    def test_model_can_create_a_bucketlist(self):
        """Test that the VideoGame model can create a single instance."""
        old_count = VideoGame.objects.count()
        self.videogame.save()
        new_count = VideoGame.objects.count()
        self.assertNotEqual(old_count, new_count)
