from django.shortcuts import render
from category.models import Category
from django.views.generic.list import ListView





# def view_category(request):
#     categories            =   Category.objects.all()
#     return render(request,'category/view_category.html',{ 'categories': categories })

class CategoryList(ListView):
    model = Category
    context_object_name = 'categories'
    template_name='category/view_category.html'