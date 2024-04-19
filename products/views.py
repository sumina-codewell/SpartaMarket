from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request, 'products/index.html')

def products(request):
	return render(request, 'products/products.html')

# def login(request):
# 	return render(request, 'accounts/login.html')

def productDetail(request, pk):
	product = Product.objects.get(pk=pk)
	context = {'product': product}
	return render(request, 'productDetail.html', context)