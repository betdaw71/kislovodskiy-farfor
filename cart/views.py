from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET
from django.contrib import messages

from shop.models import Product,Category
from .cart import Cart
from .forms import CartAddProductForm


@require_GET
def cart_add(request):
    cart = Cart(request)
    product = get_object_or_404(Product, id=int(request.GET.get('product_id')))
    print(int(request.GET.get('quantity')))
    # form = CartAddProductForm(request.POST)
    # if form.is_valid():
    #     cd = form.cleaned_data
    #     cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
    # if request.GET != {}:
    cart.add(product=product, quantity=int(request.GET.get('quantity')),update_quantity=True)
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    messages.success(request, 'Удалено')
    return redirect('cart:cart_detail')


def cart_detail(request):
    categories = Category.objects.all()
    cart = Cart(request)
    products = Product.objects.all()
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'], 'update': True})
    return render(request, 'cart/detail.html', {'cart': cart,'categories':categories,'products':products })