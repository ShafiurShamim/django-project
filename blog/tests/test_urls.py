from django.test import TestCase
from urllib.parse import urlparse
from django.urls import reverse, resolve
from blog.views import (
    post_list_view, post_detail_view, post_create_view, post_update_view, post_delete_view,
)


class TestUrls(TestCase):
    def assertUrl(self, path, name, func):
        parse_url = urlparse(name)
        if parse_url.query:
            url = reverse(parse_url.path, args=parse_url.query)
        else:
            url = reverse(name)
        full_path = '/blog'
        if(path):
            full_path += path
        self.assertEqual(url, full_path)
        if(func):
            self.assertEqual(resolve(url).func, func)

    def test_blog_url_resolves(self):
        self.assertUrl('/', 'blog-home', post_list_view)
        self.assertUrl('/post/1/', 'post-detail?1', post_detail_view)
        self.assertUrl('/post/create/', 'post-create', post_create_view)

    #  def test_blog_home_url_resolves(self):
        # url = reverse('blog-home')
        # self.assertEqual(resolve(url).func, post_list_view)
        # self.assertEqual(url, '/blog/')

    # def test_blog_post_detail_url_resolves(self):
    #     url = reverse('post-detail', args=['1'])
    #     self.assertEqual(resolve(url).func, post_detail_view)
    #     self.assertEqual(url, '/blog/post/1/')

    # def test_blog_post_create_url_resolves(self):
    #     url = reverse('post-create')
    #     self.assertEqual(resolve(url).func, post_create_view)
    #     self.assertEqual(url, '/blog/post/create/')
