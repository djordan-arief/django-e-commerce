from django.shortcuts import render, get_object_or_404
from .models import Category, Product

# Create your views here.
def all_products(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})

def categories(request):
    return {
        'categories': Category.objects.all()
    }

def category_list(request, slug):
    category = get_object_or_404(Category, slug= slug)
    product = Product.objects.filter(category = category)
    return render(request, 'store/category.html', {'category': category, 'product': product})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/product_detail.html', {'product': product})