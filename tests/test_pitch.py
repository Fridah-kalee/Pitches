import unittest
from app.models import Pitch

class PitchModelTest(unittest.TestCase):

    def setUp(self):
        self.new_pitch = Pitch(id = 1, title = 'sales', pitch_content = 'Focus on your end goal', category = 'interview', upvote = 1, downvote = 1, username = 'fridah')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pitch, Pitch))