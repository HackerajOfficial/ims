from django.shortcuts import render

# Create your views here.
def test(request):
    return render(request,'test.html')


def view_category(request):
    return render(request,'inventory/view_category.html')