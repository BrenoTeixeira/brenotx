from django.test import TestCase
from django.core.urlresolvers import reverse

from ..forms import ContactForm


class ContactTest(TestCase):

    def setUp(self):
        self.url = reverse('contact:form-view')
        self.resp = self.client.get(self.url)

    def test_get_contact_page(self):
        self.assertEqual(self.resp.status_code, 200)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'contact/contact.html')

    def test_csrf_token(self):
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_has_contact_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, ContactForm)