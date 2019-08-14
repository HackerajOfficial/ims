from django.shortcuts import render


def view_stock_details(request):
    return render(request, 'inventory/view_stock_details.html')