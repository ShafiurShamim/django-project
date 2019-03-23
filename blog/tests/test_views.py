from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.utils import timezone
from django.contrib.auth.models import User
from blog.models import Post


class TestViews(TestCase):

    def setUp(self):
        self.post_list_url = reverse('blog-home')
        self.post_detail_url = reverse('post-detail', args=['1'])
        self.post_1 = Post.objects.create(
            id=1, author_id=1, title='blog-post-1', body='post 1 body', date_created=timezone.now())
        self.client = Client()
        self.user = User.objects.create_user(
            'test_user', 'test@test.com', 'testPassword')

    def test_blog_list(self):
        response = self.client.get(self.post_list_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/home.html')

    def test_blog_post_detail(self):
        response = self.client.get(self.post_detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_detail.html')

    def test_blog_post_create(self):
        self.client.login(username='test_user', password='testPassword')
        response = self.client.get(reverse('post-create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_form.html')
