from django.test import TestCase
from django.urls import reverse, resolve
from accounts.views import register, profile


class TestUrls(TestCase):

    def assertUrl(self, path, name, func):
        url = reverse(name)
        self.assertEqual(url, '/accounts/'+path+'/')
        if(func):
            self.assertEqual(resolve(url).func, func)

    def test_accounts_url_resolves(self):
        self.assertUrl('register', 'register', register)
        self.assertUrl('login', 'login', None)
        self.assertUrl('logout', 'logout', None)
        self.assertUrl('profile', 'profile', profile)
