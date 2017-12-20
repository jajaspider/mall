from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'shopping/index.html')

def category(request):
    return render(request,'shopping/category.html')

def photo(request):
    return render(request,'shopping/photo.html')

def contacts(request):
    return render(request,'shopping/contacts.html')


def category_cpu(request):
    return render(request,'shopping/cpu.html')
