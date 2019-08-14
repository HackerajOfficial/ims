from django.shortcuts import render
from .models import Supplier
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from supplier.forms import AddCustomerDetailsForm

def viewSupplierDetails(request):
    suppliers = Supplier.objects.all()

    query = request.GET.get("q")
    if query:
        suppliers = suppliers.filter(name__icontains=query)

    paginator = Paginator(suppliers,7)
    page = request.GET.get('page')
    suppliers = paginator.get_page(page)
    return render(request,'supplier/view_supplier_details.html', {'suppliers': suppliers})

class AddSupplierDetails(LoginRequiredMixin, CreateView):
    login_url           =   "add_supplier_details/"
    template_name       =   "supplier/add_supplier_details.html"
    form_class          =   AddCustomerDetailsForm
    queryset            =   Supplier.objects.all()
    success_url         =   "/"

    def form_valid(self, form):
        supplier        =   form.save(commit=False)
        supplier.save()
        return super(AddSupplierDetails, self).form_valid(form)

    def form_invalid(self, form):
        print(form.error)
        return super(AddSupplierDetails,self).form_invalid(form)