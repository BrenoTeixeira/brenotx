from django import forms
from django.core.mail import send_mail


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    body = forms.CharField(widget=forms.Textarea)

    def send_mail(self):
        send_mail('[My Website contact]',
                  self.cleaned_data['body'],
                  self.cleaned_data['email'],
                  ['brenotx@gmail.com'],
                  fail_silently=False,)