from django.urls import path
from stock import views

urlpatterns = [
    
    path('add_stock_details/', views.AddStockDetails.as_view(), name='add_stock_details'),
    
]