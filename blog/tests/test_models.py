from django.test import TestCase
from django.utils import timezone

from blog.models import Post


class TestModels(TestCase):
    def setUp(self):
        self.post1 = Post.objects.create(
            id=1, author_id=1, title='blog-post-1', body='post 1 body', date_created=timezone.now())

    def test_post_creation(self):
        self.assertTrue(isinstance(self.post1, Post))
        self.assertEqual(self.post1.title, 'blog-post-1')
