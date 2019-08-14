from django.shortcuts import render
from django.views.generic.edit import CreateView
from stock.models import StockDetails
from django.contrib.auth.mixins import LoginRequiredMixin



# def addStockDetails(request):
#     return render(request,'stock/add_stock_details.html')

class AddStockDetails(LoginRequiredMixin, CreateView):
    #model = StockDetails
    queryset        =   StockDetails.objects.all()
    template_name   =   "stock/add_stock_details.html"
    success_url     =   "/"

