from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify


from ..models import Post


class PostTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username='Some_user')
        self.post = Post.objects.create(title='My post title',
                                        author=self.user)

    def test_model_creation(self):
        self.assertIsInstance(self.post, Post)
        self.assertEqual(self.post.__unicode__(), self.post.title)
        self.assertEqual(self.post.slug, slugify(self.post.title))

    def test_model_absolute_url(self):
        self.assertEqual(self.post.get_absolute_url(),
                         reverse('blog:post-detail', kwargs={'slug': self.post.slug}))

    def test_ordering_by_created_at(self):
        self.assertListEqual(self.post._meta.ordering, ['-created_at',])
