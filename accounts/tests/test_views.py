from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse

from accounts.models import Profile


class TestViews(TestCase):

    def setUp(self):
        self.profile_url = reverse('profile')
        self.user = User.objects.create_user(
            username='test_user', email='test_user@gm.nv', password='secret')
        # self.profile = Profile.objects.create(user=self.user)

    def test_user_profile_view(self):
        response = self.client.get(self.profile_url)
        self.assertRedirects(
            response, '/accounts/login/?next=/accounts/profile/', 302)
        self.sign_in()
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/profile.html')

    def test_user_register_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')
        self.sign_in()
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/')

    def test_user_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')
        self.sign_in()
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/accounts/profile/')

    def sign_in(self):
        self.client.login(username='test_user', password='secret')
