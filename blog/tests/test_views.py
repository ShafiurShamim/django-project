from django.test import TestCase
from django.urls import reverse, resolve
from django.utils import timezone

from blog.models import Post


class TestViews(TestCase):

    def setUp(self):
        self.posts_url = reverse('blog-posts')
        self.post_url = reverse('blog-post', args=['1'])
        self.post_1 = Post.objects.create(
            id=1,
            author_id=1,
            title='blog-post-1',
            body='post 1 body',
            date_created=timezone.now()
        )

    def test_blog_posts_GET(self):
        response = self.client.get(self.posts_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/posts.html')

    def test_blog_single_post_GET(self):
        response = self.client.get(self.post_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post.html')
