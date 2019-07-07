from django.urls import path
from . import views

urlpatterns = [
    path('test', views.test, name='test'),
    path('view_category', views.view_category, name='view_category'),
]