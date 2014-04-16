from django.test import TestCase
from django.core.urlresolvers import reverse
from django.core import mail

from ..forms import ContactForm


class ContactFormTest(TestCase):

    def setUp(self):
        self.url = reverse('contact:form-view')
        self.data = self.create_data()
        self.resp = self.client.post(self.url, self.data)

    def create_data(self,
                    name='Breno Teixeira',
                    body='My message',
                    email='brenotx@gmail.com'):
        return dict(name=name, body=body, email=email)

    def test_form_is_valid(self):
        form = ContactForm(data=self.data)
        self.assertTrue(form.is_valid())

    def test_redirect_valid_post(self):
        redirect_url = reverse('contact:thanks')
        self.assertRedirects(self.resp, redirect_url)

    def test_invalid_form(self):
        invalid_data = self.create_data(email='breno#gmail.com')
        invalid_form = ContactForm(data=invalid_data)
        self.assertFalse(invalid_form.is_valid())

    def test_invalid_form_must_not_redirect(self):
        invalid_data = self.create_data(email='breno#gmail.com')
        resp = self.client.post(self.url, invalid_data)
        self.assertEqual(resp.status_code, 200)

    def test_invalid_form_must_display_errors(self):
        invalid_data = self.create_data(email='breno#gmail.com')
        resp = self.client.post(self.url, invalid_data)
        ContactForm(data=invalid_data)
        self.assertTrue(resp.context['form'].errors)


class SendMailPostTest(TestCase):
    
    def test_send_email(self):
        mail.send_mail('Subject here',
                       'Body here',
                       'from@email.com',
                       ['brenotx@gmail.com'],
                       fail_silently=False)

        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Subject here')