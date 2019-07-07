from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def indexx(request):
    return render(request, 'indexx.html')
