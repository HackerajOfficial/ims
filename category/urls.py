from django.urls import path
from category import views

urlpatterns = [
    path('view_category/', views.CategoryList.as_view(), name='view_category'),
    # path('view_customer_details/', views.viewCustomerDetails, name='view_customer_details'),
]