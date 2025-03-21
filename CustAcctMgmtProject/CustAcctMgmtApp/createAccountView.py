from django.http import HttpResponseRedirect
from django.views.generic import CreateView

from .customerForms import ContactModelForm
from .models import Contact, Customer


class CreateContactGCView(CreateView):
    template_name = "create_contact.html"

    model = Contact
    form_class = ContactModelForm
    pk_url_kwarg = 'fk'
    success_url = '/index/'
    fk = 0
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #self.fk = kwargs[super.pk_url_kwarg]
        print ("Creating a Contact for Customer  = " + str(self.fk))
        return context

    def form_valid(self, form):
        self.fk = self.kwargs['fk']
        print ("Creating a Contact for Customer  = " + str(self.fk))
        customer = Customer.objects.get(id=self.fk)
        self.object = form.save(commit=False)
        self.object.customer = customer
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())

