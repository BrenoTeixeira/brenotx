from django.test import TestCase
from django.core.urlresolvers import reverse
from django.core import mail

from .forms import ContactForm


class ContactTest(TestCase):

    def setUp(self):
        self.url = reverse('contact:form-view')
        self.resp = self.client.get(self.url)

    def test_GET_contact_page(self):
        self.assertEqual(self.resp.status_code, 200)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'contact/contact.html')

    def test_html_form(self):
        self.assertContains(self.resp, '<form')
        self.assertContains(self.resp, '<input', 5)
        self.assertContains(self.resp, 'type="text"', 2)
        self.assertContains(self.resp, 'type="email"')
        self.assertContains(self.resp, 'type="submit"')

    def test_csrf_token(self):
        self.assertContains(self.resp, 'csrfmiddlewaretoken')

    def test_as_contact_form(self):
        form = self.resp.context['form']
        self.assertIsInstance(form, ContactForm)


class ContactPostTest(TestCase):

    def setUp(self):
        url = reverse('contact:form-view')
        self.data = dict(name='Breno Teixeira',
                         body='My message',
                         email='brenotx@gmail.com',)

        self.resp = self.client.post(url, self.data)

    def test_redirect_valid_post(self):
        redirect_url = reverse('contact:thanks')
        self.assertRedirects(self.resp, redirect_url)


class ContactFormTest(TestCase):

    def test_send_email(self):
        mail.send_mail('Subject here',
                       'Body here',
                       'from@email.com',
                       ['brenotx@gmail.com'],
                       fail_silently=False)

        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Subject here')