from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify


from ..models import Post


class PostTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='Some_user')

    def create_post(self, title='My post title', published=True):
        return Post.objects.create(title=title,
                                   author=self.user,
                                   published=published)

    def test_model_creation(self):
        post = self.create_post()
        self.assertIsInstance(post, Post)
        self.assertEqual(post.__unicode__(), post.title)
        self.assertEqual(post.slug, slugify(post.title))

    def test_model_absolute_url(self):
        post = self.create_post()
        self.assertEqual(post.get_absolute_url(),
                         reverse('blog:post-detail', kwargs={'slug': post.slug}))
