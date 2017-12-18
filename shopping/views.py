from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'shopping/index.html')

def category(request):
    return render(request,'shopping/category.html')

def photo(request):
    return render(request,'shopping/photo.html')

def item_detail(request,pk):
    boardList = get_object_or_404(Notice, pk=pk)
    return render(request, 'shopping/item_detail.html', {'boardList': boardList})
