from django.shortcuts import render, redirect, get_object_or_404
from .models import Product
from .forms import ProductForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
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
	product = get_object_or_404(Product, pk=pk)
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

@login_required
@require_POST
def delete(request, pk):
	product=Product.objects.get(pk=pk)
	product.delete()
    return redirect('products:products')

@login_required
@require_http_methods(["GET", "POST"])
def update(request, pk):
    product=Product.objects.get(pk=pk)
    if request.method == 'POST':
        form=ProductForm(request.POST, instance=product)
        if form.is_valid():
            product=form.save()
            return redirect("products:productDetail", product.pk)
    else:
        form=ProductForm(instance=product)
    context={'form':form, 'product':product,}
    return render(request, 'products/update.html', context)