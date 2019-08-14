from django.urls import path
from customer import views

urlpatterns = [
    path('add_customer_details/', views.AddCustomerDetails.as_view(), name='add_customer_details'),
    path('view_customer_details/', views.viewCustomerDetails, name='view_customer_details'),
]