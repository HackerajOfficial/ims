from django.shortcuts import render
from django.views import View
from customer.models import Customer
from django.core.paginator import Paginator
from .forms import AddCustomerDetailsForm
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


class AddCustomerDetails(LoginRequiredMixin, CreateView):
    login_url       = 'add_customer_details/'
    template_name   =   "customer/add_customer_details.html"
    form_class      =   AddCustomerDetailsForm
    queryset        =   Customer.objects.all()
    success_url     =   "/"

    def form_valid(self, form):
        print(form)
        customer    =   form.save(commit=False)
        customer.save()
        return super(AddCustomerDetails, self).form_valid(form)

    def form_invalid(self, form):
        print(form.errors)
        return super(AddCustomerDetails, self).form_invalid(form)

def viewCustomerDetails(request):
    customers   =   Customer.objects.all()

    query = request.GET.get("q")
    if query:
        customers = customers.filter(name__icontains=query)

    paginator = Paginator(customers,7)
    page = request.GET.get('page')
    customers = paginator.get_page(page)
    return render(request, 'customer/view_customer_details.html', { 'customers' : customers })