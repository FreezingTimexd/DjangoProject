from cart.forms import CartAddProductForm
from django.shortcuts import render, get_object_or_404

from .filters import ProductFilter
from .models import Product, Category


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    f = ProductFilter(request.GET, queryset=Product.objects.all())
    has_filter = any(field in request.GET for field in set(f.get_fields()))

    context = {
        'category': category,
        'categories': categories,
        'products': products,
        'filter': f,
        'has_filter': has_filter
    }
    return render(request,
                  'catalog/product/list.html',
                  context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'cart_product_form': cart_product_form
    }
    return render(request,
                  'catalog/product/detail.html',
                  context)
