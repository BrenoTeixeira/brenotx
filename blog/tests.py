from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model

from .models import Post


class PostListViewTests(TestCase):

    def setUp(self):
        self.url = reverse('blog:post-list')
        self.user = get_user_model().objects.create(username='Some_user')
        self.resp = self.client.get(self.url)

    def test_GET_blog(self):
        self.assertEqual(self.resp.status_code, 200)

    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'blog/post_list.html')

    def test_has_a_post_list(self):
        self.assertTrue(u'post_list' in self.resp.context)

    def test_no_post(self):
        self.assertContains(self.resp, 'There is no post yet.')

    def test_one_post(self):
        Post.objects.create(title='My first post',
                            content='Content post',
                            author=self.user)
        self.resp = self.client.get(self.url)
        self.assertContains(self.resp, 'My first post')
        self.assertContains(self.resp, 'Content post')


