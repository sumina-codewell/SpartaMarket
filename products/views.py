from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm
from django.http import HttpResponse

def index(request):
	return render(request, 'products/index.html')

def products(request):
	products = Product.objects.all().order_by('-created_at')
	context = {'products': products}
	return render(request, 'products/products.html', context)

# def login(request):
# 	return render(request, 'accounts/login.html')

def productDetail(request, pk):
	product = Product.objects.get(pk=pk)
	context = {'product': product}
	return render(request, 'products/productDetail.html', context)

def create(request):
	if request.method == 'POST':
		form = ProductForm(request.POST)
		if form.is_valid():
			product = form.save()
			return redirect("products:productDetail", product.pk)
	else:
		form = ProductForm()

	context = {'form': form}
	return render(request, 'products/create.html', context)

def delete(request, pk):
    if request.method == "POST":
        product=Product.objects.get(pk=pk)
        product.delete()
    return redirect('products:products')