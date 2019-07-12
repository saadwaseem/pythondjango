from django.http import Http404
from django.shortcuts import render, get_object_or_404

from .forms import ProductForm

from .models import Product

# Create your views here.
def product_list_view(request):
	#handles both found and missing objects
	queryset = Product.objects.all()
	context = {
		"object_list": queryset
	}
	return  render(request, "products/product_list.html", context)

def product_detail_view(request, id):
	#handles both found and missing objects
	#obj = get_object_or_404(Product, id=id)
	#handle missing object alternate
	try:
		obj = Product.objects.get(id=id)
	except Product.DoesNotExist:
		raise Http404
	context = {
		"object": obj
	}
	return  render(request, "products/product_detail.html", context)
def product_create_view(request):
	form = ProductForm(request.POST or None)
	if form.is_valid():
		form.save()
		#re render form
		form = ProductForm()

	context = {
		'form': form
	}
	return render(request, 'products/product_create.html',context)