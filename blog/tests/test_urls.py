from django.test import TestCase
from django.urls import reverse, resolve
from blog.views import home, posts, post


class TestUrls(TestCase):

    def test_blog_home_url_resolves(self):
        url = reverse('blog-home')
        self.assertEqual(resolve(url).func, home)
        self.assertEqual(url, '/blog/')

    def test_blog_posts_url_resolves(self):
        url = reverse('blog-posts')
        self.assertEqual(resolve(url).func, posts)
        self.assertEqual(url, '/blog/posts/')

    def test_blog_single_post_url_resolves(self):
        url = reverse('blog-post', args=['1'])
        self.assertEqual(resolve(url).func, post)
        self.assertEqual(url, '/blog/post/1/')
