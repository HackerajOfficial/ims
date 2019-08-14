from django.urls import path
from supplier import views

urlpatterns = [
    
    path('view_supplier_details/', views.viewSupplierDetails, name='view_supplier_details'),
    path('add_supplier_details/', views.AddSupplierDetails.as_view(), name='add_supplier_details'),
    
]