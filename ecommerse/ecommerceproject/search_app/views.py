from django.shortcuts import render
from shop.models import Product
from django.db.models import Q

# from django import forms
# Create your views here.


def SearchResult(request):
    products=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        products = Product.objects.all().filter(Q(name__contains=query)|Q(description__contains=query))
        return render(request, 'search.html',{'query':query,'products':products})







# def SearchResult(request):
#     if request.method == "POST":
#         query_name = request.POST.get('name', None)
#         if query_name:
#             results = Product.objects.filter(name__contains=query_name)
#             return render(request, 'search.html', {"results":results})
#     return render(request, 'search.html')