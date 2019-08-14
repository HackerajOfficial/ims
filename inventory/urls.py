from django.urls import path
from . import views

urlpatterns = [
    # path('view_category', views.view_category, name='view_category'),
    path('view_stock_details', views.view_stock_details, name='view_stock_details'),
]