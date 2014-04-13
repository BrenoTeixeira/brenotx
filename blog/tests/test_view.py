from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model

from ..models import Post


class PostListViewTests(TestCase):

    def setUp(self):
        self.url = reverse('blog:post-list')
        self.user = get_user_model().objects.create(username='Some_user')
        self.resp = self.client.get(self.url)

    def create_post(self, title='1-post-title', content='1-post-content', published=True):
        post = Post.objects.create(title=title,
                                   content=content,
                                   author=self.user,
                                   published=published)
        return post

    def test_get_blog(self):
        self.assertEqual(self.resp.status_code, 200)

    def test_template_used(self):
        self.assertTemplateUsed(self.resp, 'blog/post_list.html')

    def test_has_a_post_list(self):
        self.assertIn(u'post_list',  self.resp.context)

    def test_no_post(self):
        self.assertContains(self.resp, 'There is no post yet.')

    def test_one_post(self):
        post = self.create_post()
        self.resp = self.client.get(self.url)
        self.assertContains(self.resp, '1-post-title')
        self.assertContains(self.resp, '1-post-content')
        self.assertContains(self.resp, post.get_absolute_url())

    def test_two_posts(self):
        self.create_post()
        self.create_post(title='2-post-title',
                         content='2-post-content')
        self.resp = self.client.get(self.url)
        self.assertContains(self.resp, '1-post-title')
        self.assertContains(self.resp, '1-post-content')
        self.assertContains(self.resp, '2-post-title')
        self.assertContains(self.resp, '2-post-content')

    def test_show_only_published_posts(self):
        self.create_post()
        self.create_post(title='My draft title',
                         published=False)
        response = self.client.get(reverse('blog:post-list'))
        self.assertContains(response, '1-post-title')
        self.assertNotContains(response, 'My draft title')


class PostDetailViewTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create(username='Some_user')
        self.post = self.create_post()
        self.url = reverse('blog:post-detail', kwargs={'slug': self.post.slug})
        self.resp = self.client.get(self.url)

    def create_post(self, title='1-post-title', content='1-post-content', published=True):
        return Post.objects.create(title=title,
                                   content=content,
                                   author=self.user,
                                   published=published)

    def test_detail_view(self):
        self.assertEqual(self.resp.status_code, 200)
        self.assertTemplateUsed(self.resp, 'blog/post_detail.html')
        self.assertContains(self.resp, self.post.title)
        self.assertContains(self.resp, self.post.author)
        self.assertContains(self.resp, self.post.content)

    def test_draft_view(self):
        draft_post = Post.objects.create(title='Draft post title',
                                         author=self.user,
                                         published=False)
        url = draft_post.get_absolute_url()
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 404)