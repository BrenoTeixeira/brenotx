from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.core.urlresolvers import reverse_lazy

from .forms import ContactForm


class ContactView(FormView):
    form_class = ContactForm
    template_name = 'contact/contact.html'
    success_url = reverse_lazy('contact:thanks')

    def form_valid(self, form):
        form.send_mail()
        return super(ContactView, self).form_valid(form)


class ThanksView(TemplateView):
    template_name = 'contact/thanks.html'