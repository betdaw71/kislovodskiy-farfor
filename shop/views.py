from django.shortcuts import render, get_object_or_404

from .models import Category, Product
from cart.forms import CartAddProductForm
from cart.cart import Cart
from django.views.generic import (
    ListView,
    DetailView
)
'''
class ProductListView(ListView):
    template_name = 'shop/product/list.html'
    queryset = Product.objects.all()
    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        return context
'''

def index(request):
    categories = Category.objects.all()
    cart = Cart(request)
    products = Product.objects.filter(available=True)[:4]
    context = {
        'categories': categories,
        'products': products,
        'cart':cart,
    }
    return render(request, 'shop/product/index.html', context)



def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()

    if request.GET != {}:
        a = int(request.GET.get('pricefrom'))
        b = int(request.GET.get('priceto'))
        if request.GET.get('search') == '':
            if request.GET.get('category') == 'all':
                products = Product.objects.filter(price__range=(a,b))
            else:
                products = Product.objects.filter(category__slug__contains=request.GET.get('category'),price__range=(a,b))
        else:
            if request.GET.get('category') == 'all':
                products = Product.objects.filter(name__icontains=request.GET.get('search'),price__range=(a,b))
            else:
                products = Product.objects.filter(name__icontains=request.GET.get('search'),category__slug__contains=request.GET.get('category'),price__range=(a,b))
    else:
        products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products,
        'categories': categories,
    }
    return render(request, 'shop/product/category.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    products1 = Product.objects.filter(available=True)[:4]
    products2= Product.objects.filter(available=True)[4:8]
    categories = Category.objects.all()
    # cart_product_form = CartAddProductForm()
    context = {
        'product': product,
        'categories': categories,
        'products1':products1,
        'products2':products2
        # 'cart_product_form': cart_product_form
    }
    return render(request, 'shop/product/detail.html', context)
