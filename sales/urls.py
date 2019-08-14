from django.urls import path
from . import views

urlpatterns = [
    
    path('add_stock_sales', views.add_stock_sales, name='add_stock_sales'),
    path('view_stock_sales', views.view_stock_sales, name='view_stock_sales'),
]