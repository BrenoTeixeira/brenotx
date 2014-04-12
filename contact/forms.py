from django import forms
from django.core.mail import send_mail

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.bootstrap import PrependedText, FormActions


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=False)
    email = forms.EmailField()
    body = forms.CharField(widget=forms.Textarea)

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.form_class = 'form-horizontal'
    helper.field_class = 'col-md-12'
    helper.form_show_labels = False
    helper.layout = Layout(
        PrependedText('name',
                      '<span class="glyphicon glyphicon-user"></span>',
                      placeholder='Your name',
                      css_class='form-control'),
        PrependedText('email',
                      '<span class="glyphicon glyphicon-envelope"></span>',
                      placeholder='Your email',
                      css_class='form-control'),
        Field('body', placeholder='Your message', css_class='form-control'),
    )
    helper.add_input(Submit('Send', 'Send', css_class='btn btn-primary btn-mg pull-right'))

    def send_mail(self):
        send_mail('[My Website contact]',
                  self.cleaned_data['body'],
                  self.cleaned_data['email'],
                  ['brenotx@gmail.com'],
                  fail_silently=False,)