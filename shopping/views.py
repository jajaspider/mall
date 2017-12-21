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

def category_ram(request):
    return render(request,'shopping/ram.html')

def category_mb(request):
    return render(request,'shopping/mb.html')

def category_vga(request):
    return render(request,'shopping/vga.html')

def category_ssdhdd(request):
    return render(request,'shopping/ssdhdd.html')

def category_case(request):
    return render(request,'shopping/case.html')

def category_power(request):
    return render(request,'shopping/power.html')

def category_inputdevices(request):
    return render(request,'shopping/inputdevices.html')
