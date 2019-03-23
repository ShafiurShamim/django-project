from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User

from accounts.models import Profile


class TestModels(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='user', email='user@gm.nv', password='secret')
        self.profile = Profile.objects.get(user_id=self.user.id)

    def test_profile_creation(self):
        self.assertTrue(isinstance(self.profile, Profile))
        self.assertEqual(self.profile.user_id, self.user.id)
