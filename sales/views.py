from django.shortcuts import render

def add_stock_sales(request):
    return render(request,'sales/add_stock_sales.html')

def view_stock_sales(request):
    return render(request,'sales/view_stock_sales.html')
